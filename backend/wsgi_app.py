import json
import os

import xmltodict
from urllib.parse import parse_qs
from flask import Flask, request, render_template, jsonify, Response


STATIC_PATH = 'static'

app = Flask(__name__)


def convert(xml_file, xml_attribs=True):
	with open(xml_file, "rb") as f:  # notice the "rb" mode
		return xmltodict.parse(f, xml_attribs=xml_attribs)


@app.route('/')
def index():
	return "<span style='color:red'>I am app 1 and the request is: {}</span>".format(request.method)


@app.route('/app')
def the_app():
	return '<br/>'.join(open(__file__, 'r').readlines())


@app.route('/files', methods=['GET'])
@app.route('/files/<file_name>', methods=['GET'])
def files(file_name=None):
	if file_name:
		if file_name.endswith('.json'):
			return jsonify(json.load(open(f'{STATIC_PATH}/json/{file_name}', 'r', encoding='utf-8')))
		return Response(
			open(f'{STATIC_PATH}/xml/{file_name}', 'r', encoding='utf-8').read(),
			content_type='text/plain'
		)
	xml_files = os.listdir(f'{STATIC_PATH}/xml')
	json_files = os.listdir(f'{STATIC_PATH}/json')
	return render_template('files.html', xml_files=xml_files, json_files=json_files)


@app.route('/test/<file_name>')
def test(file_name):
	return jsonify(convert(STATIC_PATH + '/json/' + file_name))


@app.route('/save_json', methods=['POST', 'DELETE'])
def save_json():
	file_name = request.data.decode('utf-8')

	print(file_name)

	if request.method == 'DELETE':
		os.remove(f'{STATIC_PATH}/json/{file_name}')
		return Response(status=410)

	with open(f'{STATIC_PATH}/json/{file_name}.json', 'w') as out:
		json.dump(convert(f'{STATIC_PATH}/xml/{file_name}'), out)
	return Response(status=205)


if __name__ == '__main__':
	app.run(port=2222, debug=True)

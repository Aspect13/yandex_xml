import json
import os

import xmltodict
from urllib.parse import parse_qs

STATIC_PATH = 'static'

from flask import Flask, request, render_template

app = Flask(__name__)

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
		return open(STATIC_PATH + '/' + file_name, 'r').read()
	file_list = os.listdir(STATIC_PATH)
	return render_template('files.html', files=file_list)



def convert(xml_file, xml_attribs=True):
	with open(xml_file, "rb") as f:  # notice the "rb" mode
		d = xmltodict.parse(f, xml_attribs=xml_attribs)
		return json.dumps(d, indent=4)


def application(env, start_response):
	qs = parse_qs(env['QUERY_STRING'])

	if qs.get('file', [''])[0].lower() == 'log':
		start_response('200 OK', [('Content-Type', 'text/plain')])
		return open(r'/home/ad/yandex_xml/log/uwsgi.log', 'rb').readlines()[::-1]

	if qs.get('file'):
		xml_filename = qs['file'][0]
		json = convert('/mnt/c/Users/AD/WebstormProjects/yandex_xml/static/{}.xml'.format(xml_filename))
		start_response('200 OK', [('Content-Type', 'application/json')])
		return bytes(json, encoding='utf-16')

	start_response('200 OK', [('Content-Type', 'text/html')])
	return b"DAAAAAAM son where'd u got this?"


if __name__ == '__main__':
	app.run(port=2222, debug=True)
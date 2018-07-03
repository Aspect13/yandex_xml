import json
import xmltodict
from urllib.parse import parse_qs


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

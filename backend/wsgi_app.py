def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return b"DAAAAAAM son where'd u got this?"

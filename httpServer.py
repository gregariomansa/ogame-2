import cherrypy

class HttpServer(object):
	exposed = True

	@cherrypy.expose
	def index(self):
		return "Ogame Registration Server."

	@cherrypy.expose
	def register(self):
		#TODO handle a POST request with regID
		return "Here you must post your regId from GCM"

if __name__=='__main__':
	cherrypy.quickstart(HttpServer())

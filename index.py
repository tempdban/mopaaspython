import web
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        if not name: 
            name = 'Mopaas'
        return 'Hello, ' + name + '!'

application = app.wsgifunc()

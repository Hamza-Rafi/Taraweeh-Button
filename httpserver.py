from http.server import HTTPServer, BaseHTTPRequestHandler

class WebServer(BaseHTTPRequestHandler):

    print('Server Online...')

    def do_GET(self):
        # changes the path to index.html if a '/' was put in the browser
        if self.path == '/':
            self.path = '/index.html'

        try:
            # tries to find and open the file after the '/'
            file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            # if there was no file found send a 404 error to the server
            file = 'Page not found!'
            self.send_response(404)

        self.end_headers()
        # writes the file to the browser
        self.wfile.write(bytes(file, 'utf-8'))


server = HTTPServer(('192.168.1.128', 8000), WebServer) #change this IP address to your local one
server.serve_forever()
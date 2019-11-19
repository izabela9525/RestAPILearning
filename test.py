import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser

DEFAULT_OAUTH_URL = 'https://allegro.pl/auth/oauth'
DEFAULT_REDIRECT_URI = 'http://localhost:8000'

def get_access_code(client_id, api_key, redirect_uri=DEFAULT_REDIRECT_URI, oauth_url=DEFAULT_OAUTH_URL):
    auth_url = '{}/authorize' \
               '?response_type=code' \
               '&client_id={}' \
               '&api-key={}' \
               '&redirect_uri={}'.format(oauth_url, client_id, api_key, redirect_uri)

    parsed_redirect_uri = requests.u

    ls.urlparse(redirect_uri)

    server_address = parsed_redirect_uri.hostname, parsed_redirect_uri.port

    class AllegroAuthHandler(BaseHTTPRequestHandler):
        def __init__(self, request, address, server):
            super().__init__(request, address, server)

        def do_GET(self):
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            self.server.path = self.path
            self.server.access_code = self.path.rsplit('?code=', 1)[-1]

    print('server_address:', server_address)

    webbrowser.open(auth_url)

    httpd = HTTPServer(server_address, AllegroAuthHandler)
    print('Waiting for response with access_code from Allegro.pl (user authorization in progress)...')

    httpd.handle_request()

    httpd.server_close()

    _access_code = httpd.access_code

    print('Got an authorize code: ', _access_code)

    return _access_code

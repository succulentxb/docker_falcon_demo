import os
from wsgiref.simple_server import make_server

import falcon


class HelloWorldResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = "Hello World!\n"


app = falcon.App()

app.add_route("/", HelloWorldResource())


if __name__ == "__main__":
    port = 80
    try:
        port = int(os.environ["PORT"])
    except:
        pass
    with make_server('', port, app) as httpd:
        print(f"Serving on port {port}...")
        httpd.serve_forever()

import tornado.web
import tornado.ioloop
import tornado.httpclient
import requests

apiurl = "https://api.lyrics.ovh/v1/"


class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


def make_app():
    return tornado.web.Application([
        (r"/", HomePage),
    ],
        debug=True,
        autoreload=True,
        static_path="static"
    )


if __name__ == "__main__":
    app = make_app()
    port = 8881
    app.listen(port)
    print(f"I'm listening on localhost:{port}")
    tornado.ioloop.IOLoop.current().start()

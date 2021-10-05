import tornado.web
import tornado.ioloop
import tornado.httpclient
import requests

apiurl = "https://api.lyrics.ovh/v1/"


class HomePage(tornado.web.RequestHandler):
    def get(self):
        # artist_name = self.get_body_argument("artist_name")
        # song_name = self.get_body_argument("song_name")
        # response = requests.get(f"{apiurl}/{artist_name}/{song_name}")
        # data = response.json()
        # lyrics = data["lyrics"]
        # print(lyrics)
        self.render("templates/index.html")

    def post(self):
        artist_name = self.get_body_argument("artist_name")
        song_name = self.get_body_argument("song_name")
        response = requests.get(f"{apiurl}/{artist_name}/{song_name}")
        data = response.json()
        lyrics = data["lyrics"]
        print(lyrics)
        self.render("templates/index.html", lyrics=lyrics, song_name=song_name, artist_name=artist_name)

def make_app():
    return tornado.web.Application([
        (r"/", HomePage),
        # (r"/lyrics", LyricsPage)
    ],
        debug=True,
        autoreload=True,
        static_path="static",
    )


if __name__ == "__main__":
    app = make_app()
    port = 8881
    app.listen(port)
    print(f"I'm listening on localhost:{port}")
    tornado.ioloop.IOLoop.current().start()

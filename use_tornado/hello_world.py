#!/usr/bin/env python
# -*- coding=utf-8 -*-

from tornado import ioloop, web, wsgi


class MainHandler(web.RequestHandler):
    def initialize(self):
        pass

    def get_user_locale(self):
        pass

    def get_login_url(self):
        pass

    def get(self, *args, **kwargs):
        self.write("Hello, world")
        self.write("You requested the main page")
        self.write('<html><body><form action="/" method="post">'
                   '<input type="file" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))


class StoryHandler(web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)


# application = web.Application([
#     (r"/", MainHandler),
#     (r"/story/([0-9]+)", StoryHandler)
# ])

application = wsgi.WSGIApplication(

)

if __name__ == '__main__':
    application.listen(8888)
    ioloop.IOLoop.instance().start()

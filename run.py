import falcon
from api.resources.kafka import KafkaResource

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote

def create():
    api = falcon.API()
    api.add_route('/quote', QuoteResource())
    api.add_route('/kafka', KafkaResource())
    return api

quote = create()

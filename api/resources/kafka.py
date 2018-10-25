import falcon
import json

class KafkaResource:
    def on_post(self, req, resp):
        raw_json = req.bounded_stream.read()
        request_json = json.loads(raw_json.decode('utf-8'))
        resp.status = falcon.HTTP_CREATED

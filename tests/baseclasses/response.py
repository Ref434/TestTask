
class Response:
    def __init__(self, response):
        self.response = response
        try:
            self.response_json = response.json()
        except:
            self.response_json = None
        self.response_status = response.status_code

    def validate(self, schema):
        schema.parse_obj(self.response_json)
        return self

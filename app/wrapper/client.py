import requests
from flask import jsonify


class RijksmusemApi(object):
    def __init__(self, key, language, object_number):
        self.url = "https://www.rijksmuseum.nl/api/{}/collection/{}?key={}".format(language, object_number, key)

    def create_json_response(self, json_response):
        payload = {
            "status": "success",
            "data": {
                "object_title": json_response["artObject"]["title"],
                "object_image_url": json_response["artObject"]["webImage"]["url"],
                "object_colors": json_response["artObject"]["colors"],
                "object_plaqueDescriptionDutch": json_response["artObject"]["plaqueDescriptionDutch"],
                "object_plaqueDescriptionEnglish": json_response["artObject"]["plaqueDescriptionEnglish"],
                "object_principalMaker": json_response["artObject"]["principalMaker"],
                "object_presentingDate": json_response["artObject"]["dating"]["presentingDate"],
                "object_url": "https://www.rijksmuseum.nl/nl/collectie/{}".format(json_response["artObject"]["objectNumber"])
            }
        }

        response = jsonify(payload)

        return response

    def create_error_response(self, status_code):
        payload = {
            "status": "error",
            "message": "An error has occured with status code: {}".format(status_code)
            }
        response = jsonify(payload)

        return response

    def get_object_data(self):
        r = requests.get(self.url)

        if r.status_code != 200:
            return self.create_error_response(r.status_code)

        return self.create_json_response(r.json())

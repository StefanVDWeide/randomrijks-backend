from flask import current_app, jsonify

from app.main import bp
from app.models import Object
from app.wrapper import client
from app.errors.handlers import bad_request

@bp.route("/")
def test():
    return jsonify(hello="world")


@bp.route("/get/random-object/<language>")
def get_random_object(language):

    if language not in ["en", "nl"]:
        return bad_request("Language ISO code not supported")

    object_number = Object.get_random_object()

    c = client.RijksmusemApi(current_app.config["RIJKSMUSEUM_KEY"], language, object_number)
    payload = c.get_object_data()

    return payload

#!/usr/bin/python3
""" Index module """
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns a json"""
    return jsonify({"status": "OK"})
    
@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    a_class = {
            "amenities": "Amenity",
            "cities": "City",
            "places": "Place",
            "reviews": "Review",
            "states": "State",
            "users": "User"
            }

    a_obj = {}

    for key, value in a_class.items():
        count = storage.count(value)
        a_obj[key] = count
    return jsonify(a_obj)

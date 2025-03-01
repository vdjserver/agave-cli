"""
    postits_endpoints.py

CLI integration tests for "postits-*" cli commands.
"""
import json
from flask import jsonify, request
from flask_restful import Resource
from .response_templates import response_template_to_json


# Sample response for "postits-list" cli command.
postits_list_response = response_template_to_json("postits-list.json")



class AgavePostits(Resource):
    """ Test postits-* cli commands
    """

    def get(self):
        """ Test postits-list utility

        This test emulates the Agave API endpoint "/postits/v2/" for GET
        requests. To test it:

        curl -sk -H "Authorization: Bearer xxx" 'https://localhost:5000/postits/v2/?pretty=true'
        """
        pretty_print = request.args.get("pretty", "")
        return jsonify(postits_list_response)

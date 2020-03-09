
from flask import Blueprint, request, jsonify, make_response, current_app as app, render_template
from bson.objectid import ObjectId
from utility.mongo_dao import *

question_blueprint = Blueprint('question', __name__)


@question_blueprint.route('/random_question')
def random_question(complexity="Simple", size=1):
	data = get_random_record("question_bank", {"complexity": complexity}, size)
	return jsonify(
		status='Random check'
	)
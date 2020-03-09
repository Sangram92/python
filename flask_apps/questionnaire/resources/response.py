
from flask import Blueprint, request, jsonify, make_response, current_app as app, redirect, url_for, render_template
from bson.objectid import ObjectId
from utility.mongo_dao import *
import datetime

response_blueprint = Blueprint('response', __name__)

@response_blueprint.route('/update_response')
def update_response(data):
	try:
		question = get_by_id("question_bank", data.get("que_id"))
		data.pop("idx")
		response_data = {
			"question_id": data.pop("que_id"),
			"participant_id": data.pop("participant"),
			"start_time": datetime.date.today().strftime("%d-%m-%Y"),
			"end_time": datetime.date.today().strftime("%d-%m-%Y"),
			"result": 0
		}

		if list(data.values())[0] == question["correct_answer"]:
			response_data.update({"result": 1})
		insert("response_set", response_data)
		return "Success"
	except Exception as e:
		raise e

@response_blueprint.route("/result")
def result():
	try:
		participant_id = request.args.get("participant_id")
		responses = get_all("response_set", "participant_id", participant_id)
		total_res = len(responses)
		correct_answer = len([ res for res in responses if res.get("result") ])
		incorrect_answer = total_res - correct_answer

		percentage = correct_answer/total_res*100
		percentage = float("{0:.2f}".format(percentage))
		data = {
			"correct": correct_answer,
			"incorrect": incorrect_answer,
			"total": total_res,
			"percentage": percentage
		}
		return render_template("result.html", data=data)
	except Exception as e:
		raise e
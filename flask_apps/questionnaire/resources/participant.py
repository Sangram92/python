
from flask import Blueprint, request, jsonify, make_response, current_app as app, redirect, url_for, render_template
from bson.objectid import ObjectId
import datetime
from utility.mongo_dao import *
from .exam import *

participant_blueprint = Blueprint('participant', __name__)

@participant_blueprint.route('/check')
def check():
	return jsonify(
		status='Running check'
	)

@participant_blueprint.route('/', methods=['POST', 'GET'])
@participant_blueprint.route('/login', methods=['POST', 'GET'])
def login():
	try:
		if request.method == "GET":
			return render_template("login.html")
		elif request.method == "POST":
			data = request.form.to_dict()
			existing_partipant = search_one("participant", {"email_id":data.get("email_id")})
			participant_id = ""
			attempts = 1
			if not existing_partipant:
				participant = insert("participant", data)
				participant = get_by_id("participant", participant)
				participant_id = str(participant["_id"])
				evalution_status_data = {
					"participant_id": participant_id,
					"has_completed_course": False,
					"assessment_date": "",
					"attempts": attempts
				}
				evalution_status = insert("evalution_status", evalution_status_data)
			else:
				participant_id = existing_partipant["_id"]
				evalution_status = search_one("evalution_status", {"participant_id": str(existing_partipant["_id"])})
				if evalution_status:
					# update attempts
					attempts = int(evalution_status["attempts"]) + 1
					update("evalution_status", str(evalution_status["_id"]), {"attempts": attempts})
				else:
					evalution_status_data = {
						"participant_id": str(existing_partipant["_id"]),
						"has_completed_course": False,
						"assessment_date": "",
						"attempts": attempts
					}
					evalution_status = insert("evalution_status", evalution_status_data)
			session_id = insert("session", {
				"participant_id": participant_id,
				"attempts": attempts,
				"date": datetime.datetime.now()
			})
			print("session ..............", session_id)
			return redirect(url_for('exam.exam', participant_id=participant_id, session_id=session_id))
	except Exception as e:
		raise e

@participant_blueprint.route('/upload')
def upload():
	import pandas as pd
	df = pd.read_excel("data.xlsx", "Question")
	question_bank = df.to_dict()
	record_len = len(question_bank)

	for i in range(record_len+1):
		row_data = {}
		for k in question_bank.keys():
			if k != "Sr.No.":
				row_data[k.lower().replace(" ", "_")] = question_bank[k][i]
		insert("question_bank", row_data)
	return jsonify(status="Success")

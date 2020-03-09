from flask import Blueprint, request, jsonify, make_response, current_app as app, redirect, url_for, render_template
from bson.objectid import ObjectId
from utility.mongo_dao import *
from .response import *

exam_blueprint = Blueprint('exam', __name__)

@exam_blueprint.route('/exam')
def exam():
	try:
		participant = request.args.get("participant_id")
		session_id = request.args.get("session_id")

		no_of_questions = 10
		simple_que_len = int(no_of_questions*70/100)
		medium_que_len = int(no_of_questions*20/100)
		hard_que_len = int(no_of_questions*10/100)

		simple_questions = get_random_record("question_bank", {"complexity": "Simple"}, simple_que_len)
		medium_questions = get_random_record("question_bank", {"complexity": "Medium"}, medium_que_len)
		hard_questions = get_random_record("question_bank", {"complexity": "Hard"}, hard_que_len)
		question_list = simple_questions + medium_questions + hard_questions

		update_many("evalution_status", {"participant_id": str(participant)}, {"question_set": question_list})
		return redirect(url_for('exam.question', participant_id=str(participant)))
	except Exception as e:
		raise e
	


@exam_blueprint.route("/question", methods=['POST', 'GET'])
def question():
	try:	
		# here render question template with current question and participant id
		if request.method == "GET":
			idx = request.args.get("idx", 0)
			participant = request.args.get("participant_id")
			question = get_question(participant, idx)
			question["_id"] = str(question["_id"])
			question["idx"] = idx
			question["participant"] = participant
			return render_template("question_paper.html", question=question)
		elif request.method == "POST":
			data = request.form.to_dict()
			idx = data.get("idx")
			participant_id = data.get("participant")
			update_response(data)
			if not int(idx) >= 2:
				idx = int(idx) + 1
				participant = request.form.get("participant")
				question = get_question(participant, idx)
				question["_id"] = str(question["_id"])
				question["idx"] = idx
				question["participant"] = participant
				return render_template("question_paper.html", question=question)
			else:
				return redirect(url_for('response.result', participant_id=str(participant_id)))
	except Exception as e:
		raise e


def get_question(participant, idx):
	try:
		# check curent_state from session
		# total_que
		# question distribution
		# decde question_level - simple/medium/hard

		# collect asked questions from response set
		
		evalution_status = search_one("evalution_status", {"participant_id": participant})
		if evalution_status:
			question_set = evalution_status["question_set"]
			return question_set[idx]
	except Exception as e:
		raise e
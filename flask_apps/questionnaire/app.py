from flask import Flask
from flask_cors import CORS

from resources.participant import participant_blueprint
from resources.question_bank import question_blueprint
from resources.exam import exam_blueprint
from resources.response import response_blueprint

app = Flask(__name__)
app.config['TESTING'] = True
app.register_blueprint(participant_blueprint)
app.register_blueprint(question_blueprint)
app.register_blueprint(exam_blueprint)
app.register_blueprint(response_blueprint)


if __name__ == '__main__':
	app.run(debug=True)
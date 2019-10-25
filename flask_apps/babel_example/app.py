from flask import Flask, render_template
from flask_babel import Babel, numbers, dates, format_date, gettext
from datetime import date


#1. to extract all required translation phrases. 
# It collects words/phrases from the paths mentioned in babel.cfg file.
# -> pybabel extract -F babel.cfg -o messages.pot .
# The last . (dot) shows the file directory to create .pot file

#2. to add new language for translation 
# e.g. for spanish (es) language -> pybabel init -i messages.pot -d translations -l es

#3.  compile after adding actual translation in lnaguge specific file (*.po) -> 
# -> pybabel compile -d translations 

## reference video - https://www.youtube.com/watch?v=7Zfp2s1JBWw

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = "en"
babel = Babel(app)

@babel.localeselector
def get_locale():
    return "es"

@app.route('/')
def hello():
    hello_text = gettext("Hello World")
    us_no = numbers.format_decimal('12345', locale='en_US')
    se_no = numbers.format_decimal('12345', locale='sv_SE')
    de_no = numbers.format_decimal('12345', locale='de_DE')

    d = date(2019, 10, 10)
    us_date = dates.format_date(d, locale="en_US")
    dt = format_date(d)
    data = {"us_no": us_no, "se_no": se_no, "de_no": de_no, "us_date": us_date, "text": hello_text}
    return render_template("translation_check.html", data=data)

if __name__ == '__main__':
    app.run()
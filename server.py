import os
from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route("/")
@view("predictions")
def index():
	now = dt.now()
	x = random()
	return {
		"date": f"{now.year}-{now.month}-{now.day}",
		"predictions": generate_prophecies(total_num = 5, num_sentences = 3),
    	"special_date": x > 0.5,
    	"x": x,
	}
	
if os.environ.get('APP_LOCATION') == 'heroku':
	run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
	run(host='localhost', port=8080, debug=True)
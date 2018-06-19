from configparser import ConfigParser

import json
import requests
from flask import Blueprint, request

config = ConfigParser()
config.read("credentials.cfg")
HEADERS = {
	"X-RosetteAPI-Key": config.get("rosette", "APIKEY"),
	"Content-Type": "application/json",
	"Accept": "application/json"
}

rosette_blueprint = Blueprint("rosette", __name__)


#################
# ROSETTE INDEX #
#################
@rosette_blueprint.route("/")
def index():
	return json.dumps({
		"tokenization": "/rosette/tokens",
		"part of speech": "/rosette/part-of-speech",
		"language detection": "/rosette/language",
		"entities extraction": "/rosette/entities",
		"topic extraction": "/rosette/topics",
		"sentiment analysis": "rosette/sentiment",
		"categories extraction": "/rosette/categories"

	})


##########
# TOKENS #
##########
@rosette_blueprint.route("/tokens", methods=[ "POST" ])
def tokens():
	if request.form.get("content"):
		try:
			data = json.dumps({
				"content": request.form.get("content")
			})
			res = requests.post("https://api.rosette.com/rest/v1/tokens", headers=HEADERS, data=data)
			return json.dumps(res.json())
		except Exception as e:
			print(e)
			return "Internal server error: %s" % str(e), 500

	return "Bad request: 'content' (multipart/form-data) required.", 400


##################
# PART OF SPEECH #
##################
@rosette_blueprint.route("/part-of-speech", methods=[ "POST" ])
def partofspeech():
	if request.form.get("content"):
		try:
			data = json.dumps({
				"content": request.form.get("content")
			})
			res = requests.post("https://api.rosette.com/rest/v1/morphology/parts-of-speech", headers=HEADERS, data=data)
			return json.dumps(res.json())
		except Exception as e:
			print(e)
			return "Internal server error: %s" % str(e), 500

	return "Bad request: 'content' (multipart/form-data) required.", 400


######################
# LANGUAGE DETECTION #
######################
@rosette_blueprint.route("/language", methods=[ "POST" ])
def language():
	if request.form.get("content"):
		try:
			data = json.dumps({
				"content": request.form.get("content")
			})
			res = requests.post("https://api.rosette.com/rest/v1/language", headers=HEADERS, data=data)
			return json.dumps(res.json())
		except Exception as e:
			print(e)
			return "Internal server error: %s" % str(e), 500

	return "Bad request: 'content' (multipart/form-data) required.", 400


#######################
# ENTITIES EXTRACTION #
#######################
@rosette_blueprint.route("/entities", methods=[ "POST" ])
def entities():
	if request.form.get("content"):
		try:
			data = json.dumps({
				"content": request.form.get("content")
			})
			res = requests.post("https://api.rosette.com/rest/v1/entities", headers=HEADERS, data=data)
			return json.dumps(res.json())
		except Exception as e:
			print(e)
			return "Internal server error: %s" % str(e), 500

	return "Bad request: 'content' (multipart/form-data) required.", 400


####################
# TOPIC EXTRACTION #
####################
@rosette_blueprint.route("/topics", methods=[ "POST" ])
def topics():
	if request.form.get("content"):
		try:
			data = json.dumps({
				"content": request.form.get("content")
			})
			res = requests.post("https://api.rosette.com/rest/v1/topics", headers=HEADERS, data=data)
			return json.dumps(res.json())
		except Exception as e:
			print(e)
			return "Internal server error: %s" % str(e), 500

	return "Bad request: 'content' (multipart/form-data) required.", 400


######################
# SENTIMENT ANALYSIS #
######################
@rosette_blueprint.route("/sentiment", methods=[ "POST" ])
def sentiment():
	if request.form.get("content"):
		try:
			data = json.dumps({
				"content": request.form.get("content")
			})
			res = requests.post("https://api.rosette.com/rest/v1/sentiment", headers=HEADERS, data=data)
			return json.dumps(res.json())
		except Exception as e:
			print(e)
			return "Internal server error: %s" % str(e), 500

	return "Bad request: 'content' (multipart/form-data) required.", 400


#########################
# CATEGORIES EXTRACTION #
#########################
@rosette_blueprint.route("/categories", methods=[ "POST" ])
def categories():
	if request.form.get("content"):
		try:
			data = json.dumps({
				"content": request.form.get("content")
			})
			res = requests.post("https://api.rosette.com/rest/v1/categories", headers=HEADERS, data=data)
			return json.dumps(res.json())
		except Exception as e:
			print(e)
			return "Internal server error: %s" % str(e), 500

	return "Bad request: 'content' (multipart/form-data) required.", 400
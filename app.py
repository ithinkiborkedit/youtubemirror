from flask import Flask, request, send_from_directory
from pytube import YouTube
import uuid
import sys, os

app = Flask(__name__)


@app.route('/kagami/<string:videoID>', methods=['GET'])
def get_kagami(videoID):
    videoFile = videoID+'.webm'
    return send_from_directory(directory='.',filename=videoFile)
    
@app.route('/kagami', methods=['GET'])
def get_hello():
    return("This is a mirror service to save videos from YouTube!")

@app.route('/kagami/<string:youTubeID>', methods=['POST'])
def post_kagami(youTubeID):
    randID = str(uuid.uuid4())
    YouTube('https://youtube.com/watch?v='+youTubeID).streams.first().download(filename=randID)
    return 'uploaded video: '+randID


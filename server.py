from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session, jsonify, g
from flask_debugtoolbar import DebugToolbarExtension

from get_video_info import get_video_info
import os

from model import connect_to_db, db, User

app = Flask(__name__)
app.secret_key = 'abc123'


@app.route("/")
def home():
    """This is home page"""

    return render_template("index.html")

@app.route("/dubIt/api/postrecording", methods=["POST"]):
def store_voice_over():
    """ grab voice recording and store in db"""

    

@app.route("/dubIt/api/recording", methods=["GET"])
def get_recording():
    # get the recording file from db return the file source
    # return 

# @app.route("/videoID", methods=["POST"]):
# def pull_video_id():
#     vid_id = request.form.get("id")
#     # 8028026
    
#     vid_info_json = get_video_info(vid_id, 'faces')





if __name__ == "__main__":
    connect_to_db(app)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)

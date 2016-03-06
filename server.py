from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session, jsonify, g, send_from_directory
from flask_debugtoolbar import DebugToolbarExtension

from get_video_info import get_video_info
import os

from model import connect_to_db, db, User
from gp_to_mp3 import gp_to_mp3

app = Flask(__name__)
app.secret_key = 'abc123'


@app.route("/")
def home():
    """This is home page"""

    return render_template("index.html")

@app.route("/<user_name>")
def user_page(user_name = None):

    return render_template("users.html")    
#    return user_name

@app.route("/dubIt/api/postrecording", methods=["POST"])
def store_voice_over():
    """ grab voice recording and store in db"""
    pass

@app.route("/dubIt/api/recording", methods=["GET"])
def get_recording():
    '''
    get the recording file from db return the file source
    '''
    pass

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
       f = request.files['files']
       f.save('./uploads/'+f.filename)
       gp_to_mp3(f.filename)
       return '200'
    elif request.method == 'GET':
       user_id = request.args.get('user_id','NULL0')
       user_name = request.args.get('user_name','NULL0')
       audio_file = request.args.get('audio_file','NULL0')
       url = request.args.get('url','NULL0')
       twitter_handle = request.args.get('twitter_handle','NULL0')
       user = User(user_id, user_name, audio_file, url, twitter_handle)
       print user

       db.session.add(user)
       db.session.commit()


       return '200' 
    else:
       return 'Upload Page'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('./uploads/', filename)


#if __name__ == '__main__':
#   app.debug = True
#   app.run(host="0.0.0.0",
#           port=8080)

if __name__ == "__main__":
    connect_to_db(app)
    port = 8080  #int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0",debug=True, port=port)

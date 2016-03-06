from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session, jsonify, g, send_from_directory
from flask_debugtoolbar import DebugToolbarExtension

from get_video_info import get_video_info
import os
import json

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
    try:
    #q = db.query(User).filter(User.user_name == user_name)
        q = User.query.filter_by(user_name = user_name).all()[0]
        print q.user_name, q.audio_file, q.url
        return render_template("users.html")    
    except:
        return 'User ' + user_name + ' not in DB'


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
       #json_data = json.loads(request.data)
       if 'files' in request.files.keys():
           f = request.files['files']
           f.save('./uploads/'+f.filename)
           gp_to_mp3(f.filename, session.get('audio_file', 'tmp'))
           return '200. Uploaded files'
       else:
           json_data = json.loads(request.data)
           user_id = json_data.get('user_id','NULL0')
           user_name = json_data.get('user_name','NULL0')
           audio_file = json_data.get('audio_file','NULL0')
           url = json_data.get('url','NULL0')
           twitter_handle = json_data.get('twitter_handle','NULL0')
           session['audio_file'] = audio_file
           user = User(user_id, user_name, audio_file, url, twitter_handle)
           try:
               db.session.add(user)
               db.session.commit()
               return '200. User Added'
           except:
               pass
               return '200. Error Duplicate user' 
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

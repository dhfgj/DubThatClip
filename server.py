from flask import Flask, request, render_template, redirect, flash
from get_video_info import get_video_info
import os

app = Flask(__name__)
app.secret_key = 'abc123'


@app.route("/")
def home():
    """This is home page"""



    return render_template("")

@app.route("/getvoiceover", methods=["POST"]):
def store_voice_over():
    """ grab voice recording and store in db"""

    voice_over_id = request.form.get("voiceTrackId")


@app.route("/videoID", methods=["POST"]):
def pull_video_id():
    vid_id = request.form.get("id")
    # 8028026
    
    vid_info_json = get_video_info(vid_id, 'faces')





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)

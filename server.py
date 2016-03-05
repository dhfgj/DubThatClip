from flask import Flask, request, render_template, redirect, flash

import os

app = Flask(__name__)
app.secret_key = 'abc123'


@app.route("/")
def home():
    """This is home page"""

    return render_template("")

@app.route("/getvoiceover", methods=["Post"]):
def store_voice_over():
    """ grab voice recording and store in db"""







if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)

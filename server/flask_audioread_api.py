# Flask API code to receive and process audio data
from flask import Flask, request, render_template

app = Flask(__name__)

# ------------------------------------------------


@app.route("/")
def index1():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_text = request.form.get("input_text")
    return "You entered: " + input_text

# -------------------------------
@app.route("/default")
def index():
    return render_template("default.html")

@app.route("/audio", methods=["POST"])
def receive_audio():
  audio_file = request.files["audio_data"]
  # process the audio file here
  return "Audio received successfully"

if __name__ == "__main__":
  app.run()

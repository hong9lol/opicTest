import json
import os
import random
import shutil

import pandas as pd
from flask import Flask, render_template

from TTS import create_audio
from config import sources_path, audio_path

raw_sources = []
source_index = -1

app = Flask(__name__)


@app.route('/')
def home():
    # Reset
    try:
        shutil.rmtree(audio_path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(audio_path)

    global source_index, raw_sources
    source_index = -1
    raw_sources.clear()
    raw_sources = pd.read_excel(sources_path).values.tolist()
    random.shuffle(raw_sources)
    return render_template('index.html')


@app.route('/opic')
def opic():
    return render_template('opic.html')


@app.route('/next', methods=['GET'])
def next_question():
    global source_index
    hint = "None"
    answer = "None"
    source_index += 1
    if source_index >= len(raw_sources):
        print("마지막 문제")
        return ""
    source = raw_sources[source_index]
    create_audio(source[0], source[1])
    if len(source) >= 3:
        hint = source[2]
    if len(source) >= 4:
        answer = source[3]

    return json.dumps({"title": source[0], "question": source[1], "hint": hint, "answer": answer})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

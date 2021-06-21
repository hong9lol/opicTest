import pandas as pd

from TTS import create_audio
from config import questions_path

raw_questions = pd.read_excel(questions_path)

for question in raw_questions.values.tolist():
    create_audio(question[0], question[1])


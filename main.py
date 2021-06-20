import pandas as pd

from TTS import create_audio

raw_questions = pd.read_excel('/home/jake/workspace/2021/Opic/opic_questions_jake.xlsx')

for question in raw_questions.values.tolist():
    create_audio(question[0], question[1])


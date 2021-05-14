import speech_recognition as sr 
import argparse

parser = argparse.ArgumentParser(description='Test')
parser.add_argument('--audio_dir',default='1.wav',type=str, help='audio path')
opt = parser.parse_args()

path = opt.audio_dir


r = sr.Recognizer() 

sound = sr.AudioFile(path)
with sound as source:
    audio = r.record(source)


equation=r.recognize_google(audio)
print(equation)

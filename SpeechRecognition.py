import speech_recognition as sr
audiofile=("MelNet - Audio Samples.wav") #taken as source file

#initialise recognizer
r=sr.Recognizer()

#read the audio file
with sr.AudioFile(audiofile) as source:
    audio=r.record(source)
try:
    print("===============",r.recognize_google(audio))
except sr.UnknownValueError:
    print("Can't Understand")
except sr.RequestError:
    print("couldn't get the result")

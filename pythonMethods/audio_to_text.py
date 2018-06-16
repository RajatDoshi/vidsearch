import speech_recognition
from pathlib import Path
import moviepy.editor as mp
import imageio
import os
from pydub import AudioSegment
imageio.plugins.ffmpeg.download()

def videoconv(fileName):
	fileName = str(fileName)
	clip = mp.VideoFileClip(fileName).subclip(0,15)
	clip.audio.write_audiofile("theaudio1.mp3")
	audioConversion("theaudio1.mp3")

def audioConversion(fileName):
	fileName = str(fileName)
	path = Path(fileName).resolve()
	path = str(path)
	sound = AudioSegment.from_mp3(path)
	exportPath = os.path.abspath("C:/Users/Doshi/Desktop/hackathon/file.wav")
	exportPath = str(exportPath)
	sound.export(exportPath, format="wav")
	audconv("file.wav")

# Rohan, you must pip install speech_recognition
def audconv(fileName):
	recognizer = speech_recognition.Recognizer()
	formatFileName = str(fileName)
	path = Path(formatFileName).resolve()
	aud = str(path)
	with speech_recognition.AudioFile(aud) as source:
	    audio = recognizer.record(source)
	try:
	    text = recognizer.recognize_google(audio,"AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw", language='en-US')
	    print (text)
	except Exception as e:
		print (e)

#Make initial call with the video file
videoconv("quick.mp4")
#audconv("theaudio1.mp3")
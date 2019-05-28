#step 1-> Use webrtc to make a triparty video conference.
#step 2-> Save the conference video at a local system disk.
#step 3-> Now convert the video file to audio file and extract text out of it to do sentiment analysis over it.
#step 4-> As mentioned to use spacy.io API to classify the sentiments.
#step 5-> Relax we r done.


'''
import moviepy.editor as mp
clip = mp.VideoFileClip("conf.mp4").subclip(0,20)
clip.audio.write_audiofile("audio.wav")


import speech_recognition as sr 
r = sr.Recognizer() 
file = sr.AudioFile('audio.wav')

with file as source:
	audio = r.record(source)

text = r.recognize_google(audio)
'''
text = "I want to be the first to welcome you and what I like to do now is actually go back to our video conferencing sweet and bring up some of our associate you are from other parts of the world and allow some of them to also share on webcam great to see everyone here with us and thank you so much for broadcast"

#Parallel Dots API used. 
import paralleldots
paralleldots.set_api_key("Q6hg3AsjPpyejLgpkF041xQvGdvZm4UsrvFImWcfyLs")


# for single sentence
lang_code="en"
response=paralleldots.sentiment(text,lang_code)
print(response)

'''
# for multiple sentence as array
text=["Come on,lets play together","Team performed well overall."]
response=paralleldots.batch_sentiment(text)
print(response)
'''
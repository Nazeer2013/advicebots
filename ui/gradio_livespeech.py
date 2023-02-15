import gradio as gr
import speech_recognition as sr

def recognize_speech(audio):
    # set up recognizer
    # recognizer = sr.Recognizer()
    
    # recognize speech using Google Speech Recognition
    text = recognizer.recognize_google(audio)
    
    return text

def live_audio_input():
    # set up microphone
    mic = sr.Microphone()
    
    # listen to live audio
    with mic as source:
        audio = recognizer.listen(source)
        
    return audio

# create the Gradio interface
inputs = live_audio_input
outputs = recognize_speech

# set up recognizer
recognizer = sr.Recognizer()

iface = gr.Interface(live_audio_input, inputs, outputs, title="Speech Recognition", capture_session=True)
iface.launch()

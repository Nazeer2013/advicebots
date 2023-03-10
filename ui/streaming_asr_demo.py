import gradio as gr
# import speech_recognition as p
from transformers import pipeline

p = pipeline("automatic-speech-recognition")


def transcribe(audio, state=""):
    text = p(audio)["text"]
    state += text + " "
    return state, state

# Set the starting state to an empty string

gr.Interface(
    fn=transcribe, 
    inputs=[
        gr.Audio(source="microphone", type="filepath", streaming=True), 
        "state" 
    ],
    outputs=[
        "textbox",
        "state"
    ],
    live=True).launch()

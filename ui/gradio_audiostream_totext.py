import speech_recognition as sr
import gradio as gr

def transcribe_microphone_stream(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_stream = recognizer.listen(source)
    return recognizer.recognize_google(audio_stream)

def microphone_to_text():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    return transcribe_microphone_stream(recognizer, microphone)

def main():
    output = microphone_to_text()
    return output

if __name__ == "__main__":
    gr.Interface(main, "audio", "text").launch()

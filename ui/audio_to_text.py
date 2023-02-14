import gradio as gr
import speech_recognition as sr

# Define a function to recognize speech from the live audio stream
def recognize_speech():
    # Initialize the recognizer
    r = sr.Recognizer()
    
    # Start the microphone and listen for speech
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    
    # Convert speech to text
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand you.")
        return ""
    except sr.RequestError as e:
        # print(f"Sorry, I couldn't request results from Google Speech Recognition service: {e}")
        return ""

# Create a Gradio interface to capture the live audio stream and display the text output
iface = gr.Interface(fn=recognize_speech, inputs=None, outputs="text", title="Live Speech-to-Text Converter")
iface.launch()

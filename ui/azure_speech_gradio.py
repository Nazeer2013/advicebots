import gradio as gr
import azure.cognitiveservices.speech as speechsdk

# Define the function that performs sentiment analysis on speech input
def analyze_sentiment(audio_file):
    # Set up the Speech SDK configuration
    speech_config = speechsdk.SpeechConfig(subscription="your_subscription_key", region="your_region")
    audio_config = speechsdk.AudioConfig(filename=audio_file)

    # Create a speech recognizer and perform sentiment analysis on the input
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        sentiment = analyze_text_sentiment(result.text)
        return f"Sentiment analysis result: {sentiment}"
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "Sorry, I didn't catch that. Please try again."
    elif result.reason == speechsdk.ResultReason.Canceled:
        return "Sorry, there was an error. Please try again."

# Define the function that performs sentiment analysis on text input using Azure Cognitive Services Text Analytics API
def analyze_text_sentiment(text):
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.credentials import AzureKeyCredential
    
    # Set up the Text Analytics API configuration
    key = "your_api_key"
    endpoint = "https://your_region.api.cognitive.microsoft.com/"
    credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint, credential)

    # Perform sentiment analysis on the input text
    documents = [text]
    response = client.analyze_sentiment(documents=documents)[0]
    return response.sentiment

# Create a Gradio interface for speech input and sentiment analysis output
iface = gr.Interface(analyze_sentiment, inputs=gr.inputs.Audio(label="Speak into your microphone"), outputs="text", title="Speech Sentiment Analysis")
iface.launch()

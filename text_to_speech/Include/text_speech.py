import pyttsx3
import pandas

def speak_text(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the voice (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Input sentence
    sentence = input("hello how are u jaanu")

    # Speak the input sentence
    speak_text(sentence)

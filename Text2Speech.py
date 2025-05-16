import pyttsx3

def text_to_speech(text):

        # Converts text to speech on Windows

    try:
        engine = pyttsx3.init()  # Initialize the engine
        engine.say(text)        # Say the text
        engine.runAndWait()    # Wait until speech is complete
    except Exception as e:
        print(f"An error occurred: {e}")

input_text = input("Enter text: ")
text_to_speech(input_text)
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    response = f"You said: {command}"
    say(response)
    return response

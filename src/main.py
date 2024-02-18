import speech_recognition as sr
import pyttsx3
import spacy

# Initiating the speech engine.
speech_engine = pyttsx3.init()
speech_engine.setProperty("rate", 150)
voices = speech_engine.getProperty('voices')
speech_engine.setProperty("voice", voices[1].id)

# Initiating spacy for natural language processing, using en-core-web-md model.
nlp = spacy.load('en_core_web_md')

# Initializing the speech recognition.
r = sr.Recognizer()


def speak(phrase):
    """Uses pyttsx3 to convert input text to speech.

    Parameters
    ----------
    phrase : str
        A string for text-to-speech conversion.
    """

    speech_engine.say(phrase)
    speech_engine.runAndWait()


def listen():
    """Uses speech_recognition to recognise a spoken phrase from the microphone with pyaudio.

    Returns
    -------
    str
        If speech is successfully recognised, returns recognised speech;
        If speech is not recognised, returns "Speech not recognised.";
        If speech recognition service causes an issue, returns "Could not request results from service; <error message>".
    """

    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Speech not recognized."
        except sr.RequestError as e:
            return f"Could not request results from service; {e}"


def get_person(phrase):
    """Returns a person (if found) in a phrase

    Parameters
    ----------
    phrase : str
        A phrase or sentence in english.

    Returns
    -------
    str or None
        If a person is found in the phrase, returns person as str;
        If no person is found in the phrase, returns None.
    """

    doc = nlp(phrase)
    ent_found = False

    for entity in doc.ents:
        if entity.label_ == "PERSON":
            ent_found = True
            return entity

    if not ent_found:
        return None


def get_city(phrase):
    """Returns a city (if found) in a phrase

    Parameters
    ----------
    phrase : str
        A phrase or sentence in english.

    Returns
    -------
    str or None
        If a city is found in the phrase, returns city as str;
        If no city is found in the phrase, returns None.
    """
    
    doc = nlp(phrase)
    ent_found = False

    for entity in doc.ents:
        if entity.label_ == "GPE":
            ent_found = True
            return entity

    if not ent_found:
        return None


if __name__ == "__main__":
    # Getting name from user.
    speak("Hello, I'm called Aurora, and my job is to get to know you better. Let's start with your name. "
          "What is it?")
    while True:
        name = get_person(listen())
        if name is None:
            speak("I didn't catch that. Do you mind telling me again?")
            continue
        else:
            speak(f"It's lovely to meet you {name}")
            break

    # Getting city from user.
    speak("It would also be lovely to know what city you live in. Where do you live?")
    while True:
        city = get_city(listen())
        if city is None:
            speak("I didn't catch that. Do you mind telling me again?")
            continue
        else:
            speak(f"{city} is a lovely city. I want to go there one day!")
            break

    # Saying goodbye to user.
    speak(f"It was nice meeting you {name}. Goodbye!")

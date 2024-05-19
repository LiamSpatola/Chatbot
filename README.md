# Chatbot
Chatbot is a Python script designed to interact with a user through voice prompts, taking in user input with speech recognition, and using natural language processing to process the user's inputs.

## Features
- Interacts with the user through voice prompts using `pyttsx3`
- Takes input from the user through speech recognition with `SpeechRecognition`
- Uses natural language processing with `spaCy` and the `en_core_web_md` model to process user input, and recgnise the user's name and city.

## Prerequisites
Ensure you have the following installed:

- Python 3.x
- Required Python libraries specified in requirements.txt.
- The `en_core_web_md` model for `spaCy`

## Installation
- Clone the repository:

```commandline
git clone https://github.com/LiamSpatola/Chatbot.git
```

- Navigate to the project directory:
```commandline
cd Chatbot/src
```

- Install dependencies using pip:
```commandline
pip install -r requirements.txt
```

- Download the `en_core_web_md` model for `spaCy`:
```commandline
python -m spacy download en_core_web_md
```

- Run `main.py`:
```commandline
python main.py
```

## Usage
 - Run the script `main.py`.
 - Follow the voice prompts.
 - Speak into your microphone to answer the questions.

## Function Usage
If you want to use specific functions from the Chatbot script in your own projects, follow these guidelines:

- `speak(phrase)`: 

Uses pyttsx3 to convert input text to speech.

```text
Parameters
----------
phrase : str
    A string for text-to-speech conversion.
```
    

Example:
```python
from main import speak


speak("Hello, how are you?")
```

- `listen()`:

Uses speech_recognition to recognise a spoken phrase from the microphone with pyaudio.
```text
Returns
-------
str
    If speech is successfully recognised, returns recognised speech;
    If speech is not recognised, returns "Speech not recognised.";
    If speech recognition service causes an issue, returns "Could not request results from service; <error message>".
```

Example:
```python
from main import listen


text = listen()
```

- `get_person(phrase)`:
Returns a person (if found) in a phrase

```text
Parameters
----------
phrase : str
    A phrase or sentence in english.

Returns
-------
str or None
    If a person is found in the phrase, returns person as str;
    If no person is found in the phrase, returns None.
```
    
Example:
```python
from main import get_person


person = get_person("My name is John.")
```

- `get_city(phrase)`:
Returns a city (if found) in a phrase

```text
Parameters
----------
phrase : str
    A phrase or sentence in english.

Returns
-------
str or None
    If a city is found in the phrase, returns city as str;
    If no city is found in the phrase, returns None.
```
    
Example:
```python
from main import get_city


city = get_city("I live in New York.")
```

## Security
This project will no longer recieve security updates. Please ensure you check all dependencies for updates and security.


## Author
[LiamSpatola](https://github.com/LiamSpatola)

## License
This project is licensed under the GNU GPLv3.

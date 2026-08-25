import speech_recognition as sr
import pyttsx3


class VoiceManager:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)

    def listen(self):
        """
        Listen to microphone and convert speech to text.
        """

        with sr.Microphone() as source:

            print("Navi: Listening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

                text = self.recognizer.recognize_google(
                    audio,
                    language="en-IN"
                )

                print(f"You: {text}")

                return text

            except sr.WaitTimeoutError:
                print("Navi: No speech detected.")
                return ""

            except sr.UnknownValueError:
                print("Navi: Sorry, I couldn't understand.")
                return ""

            except sr.RequestError:
                print("Navi: Speech recognition service unavailable.")
                return ""

    def speak(self, text):
        """
        Convert text to speech.
        """

        print(f"Navi: {text}")

        self.engine.say(text)
        self.engine.runAndWait()
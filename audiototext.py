import speech_recognition as sr
from pydub import AudioSegment

def convert_audio_to_text(audio_file_path):
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Load the audio file
    audio = AudioSegment.from_file(audio_file_path)

    # Save the audio as a .wav file
    audio.export("temp.wav", format="wav")

    # Recognize speech using the .wav file
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        try:
            # Using Google Web Speech API for recognition
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"

# Example usage
audio_file_path = "path_to_your_audio_file.mp3"  # Change this to your audio file path
text = convert_audio_to_text(audio_file_path)
print(f"Converted Text: {text}")

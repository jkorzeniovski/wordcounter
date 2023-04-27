import speech_recognition as sr

# Set up the recognizer object
r = sr.Recognizer()

# Load the audio file
audio_file = sr.AudioFile('C:/Users\kubak\OneDrive\Pulpit/yyy6.wav')

# Open the audio file and convert to audio data
with audio_file as source:
    audio_data = r.record(source)

# Use the recognize_google() method to convert audio to text
recognized_text = r.recognize_google(audio_data, language='pl-PL')

# Count the number of occurrences of "yyy"
yyy_count = recognized_text.count('obraz')

# Print the result
print(f"Found {yyy_count} occurrences of 'obraz'.")

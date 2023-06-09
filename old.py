import speech_recognition as sr

# Set up the recognizer object
r = sr.Recognizer()

# Load the audio file
audio_file = sr.AudioFile('path/to/your/audio/file.wav')

# Open the audio file and convert to audio data
with audio_file as source:
    audio_data = r.record(source)

# Use the recognize_google() method to convert audio to text
recognized_text = r.recognize_google(audio_data, language='pl-PL')

#declare a word to fin in an audio file
word = "yyy"  # We are looking for occurences of yyy to see how much we have to edit out.

# Count the number of occurrences of "word"
word_count = recognized_text.count(word)

# Print the result
print(f'Number of "{word}" occurrences:', word_count)

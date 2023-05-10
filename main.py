import speech_recognition as sr
import yt_dlp

# Create a yt-dlp options object
ytdlp_options = {
    'format': 'bestaudio/best',  # Choose the best audio format available
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',  # Convert the audio to wav
        'preferredquality': '192',  # Set the audio quality
    }],
    'outtmpl': 'mysong'  # Specify the output file name
}

# Create a yt-dlp object with the options
ytdlp = yt_dlp.YoutubeDL(ytdlp_options)

# URL of the video to extract audio from
video_url = input('Please input valid YouTube video url: ')

# https://www.youtube.com/watch?v=MPWWe0hhJuc

# Use yt-dlp to extract audio from the video
with ytdlp:
    result = ytdlp.extract_info(video_url, download=True)

print('Audio extracted successfully!\n')

# Set up the recognizer object
r = sr.Recognizer()

# Load the audio file
audio_file = sr.AudioFile("C:/Users\kubak\PycharmProjects\pythonProject1/mysong.wav")

# Open the audio file and convert to audio data
with audio_file as source:
    audio_data = r.record(source)

# Use the recognize_google() method to convert audio to text
recognized_text = r.recognize_google(audio_data, language='pl-PL')

# Word to find
word = input('What word do you seek to find?: ')

# Count the number of occurrences of "word"
word_count = recognized_text.count(word)

# Print the result
print(f"Found {word_count} occurrences of '{word}'.")
print('\n', recognized_text)

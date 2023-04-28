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
video_url = 'https://www.youtube.com/watch?v=Bs4GfrBiYYc'

# Use yt-dlp to extract audio from the video
with ytdlp:
    result = ytdlp.extract_info(video_url, download=True)

print('Audio extracted successfully!')

# # Set up the recognizer object
r = sr.Recognizer()
#
# # Load the audio file
audio_file = sr.AudioFile('C:/Users\kubak\PycharmProjects\pythonProject1/mysong.wav')
#
# # Open the audio file and convert to audio data
with audio_file as source:
    audio_data = r.record(source)
#
# # Use the recognize_google() method to convert audio to text
recognized_text = r.recognize_google(audio_data, language='pl-PL')
#
# # Count the number of occurrences of "yyy"
yyy_count = recognized_text.count('obraz')
#
# # Print the result
print(f"Found {yyy_count} occurrences of 'obraz'.")
print(recognized_text)
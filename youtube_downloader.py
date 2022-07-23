from pytube import YouTube

# https://www.youtube.com/watch?v=g_tmQ5G-T2w

SAVE_PATH = "./downloads/"
option = int(
    input("1.video\n2.audio\nChoose which format to download(1 or 2):"))
link = input('Enter the YouTube video URL: ')

try:
    yt = YouTube(link)
except:
    print("Connection Error")


filename = "".join([c for c in yt.title if c.isalpha()
                   or c.isdigit() or c == ' ' or c == '+' or c == '-']).strip().replace('+', 'plus').replace('-', 'minus').replace(' ', '-')

if option == 1:
    video_streams = yt.streams.filter(only_video=True)
    video = video_streams[0]
    print(video)
    try:
        video.download(SAVE_PATH, filename=filename +
                       '.'+video.mime_type.split('/')[1])
    except:
        print("Error!")
elif option == 2:
    audio_streams = yt.streams.filter(only_audio=True)
    audio = audio_streams[0]
    print(audio)
    try:
        audio.download(SAVE_PATH, filename=filename + '-audio.' +
                       audio.mime_type.split('/')[1])
    except:
        print("Error!")


print('Task Completed!')

import yt_dlp
import os
import sys

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'format' : 'bestaudio/best',
    'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            # 'extract-audio': True,
            'preferredcodec': 'm4a',
            'preferredquality': '192'
        }
    ],
}

def get_videos():
    while True:
        url = input('Enter URL: ')
        if url == 'q' or url == 'quit' or url == 'exit':
            break

        trackname = input('Enter Name: ')
        # file_name = input('Enter Title: ')
        # ydl_opts['outtmpl'] = file_name + '.mp3'
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            move_file(trackname);
        except Exception as e:
            # print("Url not valid, try again or (q) to exit")
            print(e);

def move_file(trackname=None):
    cur_file_name = os.listdir()
    cur_file_name = [f for f in cur_file_name if f != "youtube_mp3.py" and f != '.DS_Store' and f != 'to_add']

    
    ext = str(os.path.splitext(cur_file_name[0])[-1])
    trackname = str(trackname);

    source = '/Users/Ujwal/Programming/music_downloads/' + cur_file_name[0]
    destination = '/Users/Ujwal/Programming/music_downloads/to_add/' + trackname + ext
    print(destination);
    os.rename(source, destination)

def delete_extra_files():
    cur_file_name = os.listdir()
    cur_file_name = [f for f in cur_file_name if f != "youtube_mp3.py" and f != '.DS_Store' and f != 'to_add']
    for file in cur_file_name:
        os.remove(file);

if len(sys.argv) > 1 and sys.argv[1] == '-d':
    delete_extra_files();
else:
    get_videos()

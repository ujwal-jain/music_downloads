# Easily Download Music From YouTube
Download Songs and Playlists from YouTube using a simple script.

Author: Ujwal Jain

# Installation

```
git checkout https://github.com/ujwal-jain/music_downloads.git
```

Use the following command to install yt_dlp for python3
```
python3 -m pip install -U yt-dlp
```
If that doesn't work checkout their github page https://github.com/yt-dlp/yt-dlp


Create a `/path/to/music_downloads/to_add` directory that will store the downloaded songs. If you want to call it something else, you will have to change it manually in the `youtube_mp3.py` folder.

# Use
```
python3 youtube_mp3.py
```
Simply run the program with `python3`. It will ask you for a URL, which is a YouTube URL to download. Then it will ask for a name, whih is the new name of the file you want (extension preserving).
To get the URL simply right-click mouse on a YouTube video and select `Copy Link Address` or `Copy Video URL`. I find it works best when using official audio videos of songs. 

Be careful entering a URL that is part of the playlist. `yt-dlp` defaults to downloading all the songs of a playlist if a playlist URL is entered, which is not supported by the main file.

However, if this does happen there's a neat flag you can use to clean up the mistakes and reset.
```
python3 youtube_mp3.py -d
```
This will remove all the files except for `youtube_mp3.py`, `to_add` directory, and `.DS_Store` (python cache) from the top directory.

## Apple Music Guide
1. Open up `Finder` App and find the `to_add` directory. 
2. Open up `Apple Music` App. 

3. Select songs from `Finder`

    1. Select specific songs you want to move to `Apple Music` using `Ctrl-Click` with the mouse 

    2. Use `Ctrl-Shift-A` to select all the songs in `to_add`
4. Drag selected songs from `Finder` to `Apple Music`

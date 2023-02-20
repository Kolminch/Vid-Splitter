from ffmpeg_split import split_by_seconds
import os

def split(filename, seconds=2):
	video_files = split_by_seconds(filename, 2, 'h264')
	return video_files

def remove(files):
    for file in files:
        os.remove(file)
 

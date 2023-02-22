from ffmpeg_split import split_by_seconds
import os
import settings

seconds = settings.SPLIT_SIZE


def change_seconds(new_seconds):
    global seconds
    seconds = new_seconds
    print(seconds)


def split(filename, seconds=seconds):
    video_files = split_by_seconds(filename, seconds, "h264")
    return video_files


def remove(files):
    for file in files:
        os.remove(file)

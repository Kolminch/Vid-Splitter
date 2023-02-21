from ffmpeg_split import split_by_seconds
import os
import settings


def split(filename, seconds=settings.SPLIT_SIZE):
    video_files = split_by_seconds(filename, seconds, "h264")
    return video_files


def remove(files):
    for file in files:
        os.remove(file)

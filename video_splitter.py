from ffmpeg_split import split_by_seconds
import os
import settings


class Video_splitter:
    """Class for video splitting and deletion."""

    def __init__(self):
        self.seconds = settings.SPLIT_SIZE

    def change_seconds(self, new_seconds):
        self.seconds = new_seconds

    def split(self, filename):
        video_files = split_by_seconds(filename, self.seconds, "h264")
        return video_files

    def remove(self, files):
        for file in files:
            os.remove(file)

from ffmpeg_split import split_by_seconds
import shutil

def split(filename, seconds=30):
	split_by_seconds('vid/input.mov', 2, 'h264')

def remove(filename):
	shutil.rmtree(filename)
from ffmpeg_split import split_by_seconds
import shutil

def split(filename, seconds=2):
	video_files = split_by_seconds('vid/input.mov', 2, 'h264')
	return video_files

def remove(filename):
	shutil.rmtree(filename)
 
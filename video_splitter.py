import ffmpeg

stream = ffmpeg.input('input.mov')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)
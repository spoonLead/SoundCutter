import sys
from moviepy.editor import *

videoClip = VideoFileClip(sys.argv[1])
audioClip = videoClip.audio
audioClip.write_audiofile("outputAudio.mp3")

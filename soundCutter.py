import sys
from moviepy.editor import *


#Params for converting
VIDEO_FILE_PATH = ""

def main():
    setParamsFromArgv()
    audioTrack = getAudioTrackFromVideo()
    writeAudioFile(audioTrack)


def setParamsFromArgv():
    global VIDEO_FILE_PATH
    VIDEO_FILE_PATH = sys.argv[1]

def getAudioTrackFromVideo():
    videoClip = VideoFileClip(VIDEO_FILE_PATH)
    return videoClip.audio

def writeAudioFile(audioClip):
    audioClip.write_audiofile("outputAudio.mp3")

main()

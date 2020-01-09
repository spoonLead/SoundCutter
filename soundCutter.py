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
    try:
        VIDEO_FILE_PATH = sys.argv[1]
    except IndexError:
        print("Incorrect params")
        sys.exit()


def getAudioTrackFromVideo():
    try:
        videoClip = VideoFileClip(VIDEO_FILE_PATH)
    except IOError:
        print("Video file not found")
        sys.exit()
    return videoClip.audio


def writeAudioFile(audioClip):
    audioClip.write_audiofile("outputAudio.mp3")

main()

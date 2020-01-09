import sys
from moviepy.editor import *


#Params for converting
VIDEO_FILE_PATH = ""
AUDIO_FILE_PATH = "Output Audio.mp3"

def main():
    setParamsFromArgv()
    audioTrack = getAudioTrackFromVideo()
    writeAudioFile(audioTrack)


def setParamsFromArgv():
    global VIDEO_FILE_PATH
    global AUDIO_FILE_PATH

    try:
        VIDEO_FILE_PATH = sys.argv[1]
        if len(sys.argv) == 3:
            AUDIO_FILE_PATH = sys.argv[2]
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
    audioClip.write_audiofile(AUDIO_FILE_PATH)

main()

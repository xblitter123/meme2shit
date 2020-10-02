from moviepy.editor import *
import sys

if sys.argv[1] == "about":
    print("meme2shit")
    print("version 1.1")
    print("2020 - 2020")
    print("by salami")
else:
    clip = VideoFileClip(sys.argv[1])
    clip = clip.resize(0.2)
    clip.write_videofile(sys.argv[3], fps=int(sys.argv[2]), audio_bitrate="8k")
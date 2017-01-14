#!/usr/bin/env python3

from pydub import AudioSegment

sound = AudioSegment.from_mp3("/home/warren/github/uncommon-2017/pps.mp3")
sound.export("/home/warren/github/uncommon-2017/pps.wav", format="wav")


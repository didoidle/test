import torch
import torchaudio
import requests
import matplotlib.pyplot as plt
import os
import wave
from os import listdir
from os.path import isfile, join
from mutagen.mp3 import MP3
from pydub import AudioSegment
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


def get_wave_duration(audio_path):
    audio = wave.open(audio_path)
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames / float(rate)
    return duration

def get_mp3_duration(audio_path):
    audio = MP3(audio_path)
    return audio.info.length

path = "C:/Users/feifu/AppData/Local/osu!/Songs/661022 DJ Genki VS Camellia feat moimoi - YELL!"

if __name__ == '__main__':
    
    os.chdir(path)
    filename = os.listdir()
    #filename = [ x for x in files if x.find(".mp3") != -1]
    for f in filename:
        #filename = "C:/Users/feifu/AppData/Local/osu!/Songs/661022 DJ Genki VS Camellia feat moimoi - YELL!/audio.wav"
        #waveform, sample_rate = torchaudio.load(filename)
        name, ext = os.path.splitext(f)
        if ext == ".mp3":
            audio_duration = get_mp3_duration(f)
            if audio_duration < 30.0:
                continue
            print(f)
            mp3_sound = AudioSegment.from_mp3(f)
            mp3_sound.export(format="wav")
            waveform, sample_rate = torchaudio.load_wav(mp3_sound)

            print("Shape of waveform: {}".format(waveform.size()))
            print("Sample rate of waveform: {}".format(sample_rate))
            
    
            plt.figure()
            plt.plot(waveform.t().numpy())
            plt.show()
            continue
# -*- coding: utf-8 -*-

import pytube
import moviepy.editor as mp
import time
from tqdm import tqdm
import sys


def backline():
    print('\r', end='')

def progresso(stream, chunk, file_handle, bytes_remaining):
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    print("{:00.0f}%".format(percent), end='')
    backline()


#exporta o video para mp3
def terminou(stream, file_handle):
    print("Downlod completo, convertendo...")
    arquivo = stream.default_filename
    video = mp.VideoFileClip("c://temp/" + arquivo)
    video.audio.write_audiofile("c://temp/" + arquivo + "_som.mp3")
    print("Concluído")

video_link = input("Qual o link do vídeo?")
converter_para_mp3 = input("Converter para mp3? (s/n) ")

print("Preparando...")

#video_link = "https://www.youtube.com/watch?v=kOlOu19JEAk"
yt = pytube.YouTube(video_link)
videos = yt.streams.first()
titulo = yt.title
yt.register_on_progress_callback(progresso)

if converter_para_mp3 == "s":
    yt.register_on_complete_callback(terminou)

print("Baixando: " + titulo)
videos.download('c://temp')



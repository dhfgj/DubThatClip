import os
import subprocess

def gp_to_mp3(name, audio_name):
    '''
    name is the file name string
    '''
    f_name = name.split('.')[0]

    c = 'avconv -i ./uploads/{}.3gp -c:a libmp3lame ./uploads/{}.mp3'.format(f_name,f_name)
    #c2 = 'mv ./uploads/{}.mp3 ./uploads/{}.mp3'.format(f_name, audio_name.split('.')[0])
    os.system(c)
    #os.system(c2)
    source = './uploads/{}.mp3'.format(f_name)
    destination = './uploads/{}.mp3'.format(audio_name.split('.')[0])
    os.rename(source, destination)


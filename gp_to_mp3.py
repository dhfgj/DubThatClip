import os
import subprocess

def gp_to_mp3(name):
    '''
    name is the file name string
    '''
    f_name = name.split('.')[0]
    c = 'avconv -i ./uploads/{}.3gp -c:a libmp3lame ./uploads/{}.mp3'.format(f_name,f_name)
    print c
    os.system(c)
    #subprocess.call(c)


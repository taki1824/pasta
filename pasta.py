#©2021 引きこもりゲーマー
import tkinter
import pygame.mixer
from time import sleep


#Initialize pygame mixer
pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 4096)

#variables definition
pasta_file = 'pasta.wav'
tukutta_file = 'tukutta.wav'

music = pygame.mixer.Sound(pasta_file)
tukutta = pygame.mixer.Sound(tukutta_file)


def make_pasta(event):#when the button pressed 
    channel_music.set_volume(0)
    channel_tukutta = tukutta.play()
    channel_tukutta.set_volume(30)
    sound_length = round(tukutta.get_length(), 4)
    sleep(sound_length)
    channel_music.set_volume(30)
    

#setting up the widow
window = tkinter.Tk()
window.iconbitmap('pasta.ico')
window.title('Oishii pasta')
window.geometry('300x300')

#pasta button
button = tkinter.Button(text='パスタ作る', width=50, height=50)
button.bind('<Button-1>', make_pasta)
button.pack()


channel_music = music.play()
channel_music.set_volume(30)

window.mainloop()
#©2021 引きこもりゲーマー
import tkinter, wave
import pygame.mixer

#Initialize pygame mixer
pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 4096)

#variables definition
pasta_file = 'pasta.wav'
tukutta_file = 'tukutta.wav'

music = pygame.mixer.Sound(pasta_file)
tukutta = pygame.mixer.Sound(tukutta_file)

def make_pasta(event):
    channel_tukutta = tukutta.play()
    channel_tukutta.set_volume(2)
    

#setting up the widow
window = tkinter.Tk()
window.title('Oishii pasta')
window.geometry('300x300')

#pasta button
button = tkinter.Button(text='パスタ作る', width=50, height=50)
button.bind('<Button-1>', make_pasta)
button.pack()




channel_music = music.play()

music_length = music.get_length()
print(music_length)

channel_music.set_volume(2)

sound_end = channel_music.get_endevent()


window.mainloop()
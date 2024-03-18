import pygame
from customtkinter import *

def play_wav(file1, file2):
    pygame.mixer.init()
    sound1 = pygame.mixer.Sound(file1)
    sound2 = pygame.mixer.Sound(file2)
    channel1 = sound1.play()
    channel2 = sound2.play()
    
    while channel1.get_busy() or channel2.get_busy():
        pygame.time.delay(100)
    
    pygame.mixer.quit()

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Beat Maker")
        self.geometry("400x400")
        pygame.mixer.init()
        
        self.kick = "kick.wav"
        self.hihat = "hihat.wav"
        self.snare = "snare.wav"
    
    def play_audios(self, sounds: list):
        kick = False
        hihat = False
        snare = False
        for sound in sounds:
            if "kick" in sound:
                kick = True
            if "hihat" in sound:
                hihat = True
            if "snare" in sound:
                snare = True

if __name__ == "__main__":
    file1 = "kick.wav"
    file2 = "snare.wav"
    play_wav(file1, file2)
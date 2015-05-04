import pygame
from pygame.locals import *

class SoundMgr:
    
    path = "media/sounds/"
    musExt = ".mp3"
    sfxExt = ".ogg"
    debug = False
    
    def __init__(self, engine):
        self.engine = engine
        

    def init(self):
        pygame.init()
        pygame.mixer.init()
        self.musicVolume = 15
   
        self.musicList = ["liverpool", "bvb", "arsenal", "liverpool", "bvb"]
        self.sfxList = ["break", "bounce"]
        
        if SoundMgr.debug:
            self.playMusic("Champions_League_theme")
            self.playSound("break")


    def playMusic(self, music):
        pygame.mixer.music.load(SoundMgr.path + music + SoundMgr.musExt)
        pygame.mixer.music.play(-1)

    def playSound(self, sfx):
        sound = pygame.mixer.Sound(SoundMgr.path + sfx + SoundMgr.sfxExt)
        sound.play()

    def stopMusic(self, music):
        pygame.mixer.music.stop()


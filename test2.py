from pygame import mixer
import time
# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
mixer.init() #turn all of pygame on.

beep = mixer.Sound("beat.wav")
beep.play()
time.sleep(0.4)
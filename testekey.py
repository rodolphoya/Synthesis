# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:01:35 2013

@author: WIN7
"""

from audiolazy import *
import pygame
from pygame.locals import *
 
nota = 0 
anterior = 0
freq = 0

rate = 44100
s,Hz=sHz(rate)
ms = 1e-3*s
player = AudioIO()

DFreq = {1 : 131.00,
        2 : 138.59,
        3 : 146.83,
        4 : 155.56,
        5 : 164.81,
        6 : 174.61,
        7 : 185.00,
        8 : 196.00,
        9 : 207.55,
        10 : 220.00,
        11 : 233.08,
        12 : 246.94,
        13 : 261.63,
        }

def main():
        global nota
        global anterior
        global freq
        
        pygame.init()
        clock = pygame.time.Clock()
        joysticks = []
        for i in range(0, pygame.joystick.get_count()):
                joysticks.append(pygame.joystick.Joystick(i))
                joysticks[-1].init()
                print "Detected joystick '",joysticks[-1].get_name(),"'"
        while 1:
                clock.tick(60)
                for event in pygame.event.get():
                        if event.type == JOYBUTTONDOWN:
                                freq = DFreq [event.button + 1]
                                signal = comb(freq_to_lag(freq * Hz), .99).linearize()(white_noise(10 * ms).append(0)).limit(2 * s)
                                filt = 0.001/(1 - 1.24148 * z**-1 + 0.056845 * z**-2 + 0.0437731 * z**-3 + 0.0337219 * z**-4 + 0.0259962 * z**-5 + 0.0200621 * z**-6 + 0.0155093 * z**-7 + 0.0120234 * z**-8 + 0.00936348 * z**-9 + 0.0073461 * z**-10 + 0.00583213 * z**-11 + 0.00471728 * z**-12 + 0.00392492 * z**-13 + 0.00340072 * z**-14 + 0.00310888 * z**-15 - 0.00275325 * z** -16)
                                player.play(filt(signal),rate = rate)                                
                                #print freq                             
if __name__ == "__main__":
        main()
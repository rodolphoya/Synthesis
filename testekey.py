# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:01:35 2013

@author: WIN7
"""
from audiolazy import *
import pygame
from pygame.locals import * 
import pygame.midi
from pygame.locals import *

nota = 0 
anterior = 0
freq = 0
rate = 44100
s,Hz=sHz(rate)
ms = 1e-3*s
player = AudioIO()

pygame.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input( input_id )

DFreq = {"60" : 131.00,
    "61" : 138.59,
    "62" : 146.83,
    "63" : 155.56,
    "64" : 164.81,
    "65" : 174.61,
    "66" : 185.00,
    "67" : 196.00,
    "68" : 207.55,
    "69" : 220.00,
    "70" : 233.08,
    "71" : 246.94,
    "72" : 261.63,
    }
    
def main():
    global nota
    global anterior
    global freq 
       
    pygame.init()
    clock = pygame.time.Clock()
    
    while 1:
        clock.tick(60)

        events = event_get()
        if i.poll():
            midi_events = i.read(10)
            pos = str(midi_events[0][0][2]) #3a casinha
            note = str(midi_events[0][0][1]) #2a casinha        
        
            if pos != "0" and note != "0":                
                freq = DFreq[note]           
                N = freq_to_lag(freq * Hz)                                
                smix = Streamix()
                smix.add(0, white_noise(N))
                smix.add(N, 0.99 * smix.copy())
                #smix.limit(2 * s)
                
                filt = 0.01/(1 - 1.24148 * z**-1 + 0.056845 * z**-2 + 
                0.0437731 * z**-3 + 0.0337219 * z**-4 + 0.0259962 * z**-5 + 
                0.0200621 * z**-6 + 0.0155093 * z**-7 + 0.0120234 * z**-8 + 
                0.00936348 * z**-9 + 0.0073461 * z**-10 + 0.00583213 * z**-
                11 + 0.00471728 * z**-12 + 0.00392492 * z**-13 + 0.00340072 
                * z**-14 + 0.00310888 * z**-15 - 0.00275325 * z** -16)
                
                player.play(filt(smix),rate = rate)

                #for idx, blk in enumerate(smix.blocks(rint(N))):
                 #   print "oi "                    
                  #  if all(abs(bi) <= 1e-15 for bi in blk):
                   #     print idx * N / s, "segundos"
                    #    break
                                           
if __name__ == "__main__":
    main()
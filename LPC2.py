# -*- coding: utf-8 -*-
"""
Created on Tue Nov 05 21:14:59 2013

@author: WIN7
"""

from __future__ import division
import wave, struct, pylab
from contextlib import closing
from audiolazy import *
from numpy.fft import fft


def gen():
  fname = "C://1 C edit.wav"
  struc = struct.Struct("h")
  with closing(wave.open(fname, "rb")) as f:
    while True:
      el = f.readframes(1)[:2]
      if not el:
        break
      yield struc.unpack(el)[0] / 2 ** 15

g = Stream(gen())
print g
tamanho = len(list(g.copy()))

pylab.plot(Stream(fft(list(g.skip(tamanho/2)))).map(abs).take(inf) )
#pylab.show()

harmonicos = [184, 14, 18, 3]

table = sin_table.harmonize(dict(enumerate(harmonicos))).normalize()
print len(table.table)
size = 512

data = table(131* Hz).take(size)
filt = lpc(data, order = 16)
gain = 1e-2

(gain / filt).plot(blk=data, rate=rate, samples=1024, unwrap=False)
pylab.show()

newfilt = gain/ filt
print newfilt


#@tostream
#def get_altera_tabela(freq):
#  tlen = len(table.table)
#  for idx, el in enumerate(table(freq)):
#    yield el
#    ridx=(idx % tlen)
#    table.table[ridx] =  .5 * table.table[ridx] + .5 * sin_table.table[ridx]
#
#pylab.plot(table.table)
#pylab.show()
#
#rate = 44100
#s, Hz = sHz(rate)
#with AudioIO(True) as player:
#  player.play(get_altera_tabela(131*Hz).limit(10 * s),rate=rate)


##def gera():
##  yield 0
##  print "aew"
##  yield 1
##  for ch in "Teste":
##    yield ch
#
## Histórico IPython com a função "gera"
##gera
##gera()
##g = gera()
##g
##next(g)
##next(g)
##next(g)
##next(g)
##next(g)
##next(g)
##next(g)
##next(g)
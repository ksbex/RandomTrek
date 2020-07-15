#!/usr/bin/python
import random

def pick_an_ep(selection=None):
  
  series = {
    'tos': [29, 26, 24],
    'tas': [16, 6],
    'tng': [26, 22, 26, 26, 26, 26, 26],
    'ds9': [20, 26, 26, 26, 26, 26, 26],
    'voy': [16, 26, 26, 26, 26, 26, 26],
    'ent': [26, 26, 24, 22],
    'dis': [15, 14],
    'pic': [10]
  }
  
  if selection in series.keys():
    season = random.randrange(1, 1 + len(series[selection]))
    ep = random.randrange(1, 1 + series[selection][season - 1])
    
  if selection is None:
    selection = random.choice(list(series))
    season = random.randrange(1, 1 + len(series[selection]))
    ep = random.randrange(1, 1 + series[selection][season - 1])
  
  return selection, season, ep
  

#specify a series, change string input to desired show
print(pick_an_ep('tng'))

#pick from all series
print(pick_an_ep())

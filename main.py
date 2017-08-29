#Import Libraries
import krakenex
import json


k = krakenex.API()
k.load_key('kraken.key')

print(k.query_private('Balance'))

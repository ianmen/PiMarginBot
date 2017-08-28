#Import Libraries
import krakenex


k = krakenex.API()
k.load_key('kraken.key')

print(k.query_private('Balance'))



#Hello World
print("Hello World")

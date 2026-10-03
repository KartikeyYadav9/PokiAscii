import time
import sys

def type(text, speed=0.1):

    for char in text:
        sys.stdout.write(f"{char}")
        sys.stdout.flush()
        time.sleep(speed)

type("Welcome to the Pokémon world!")
type("\nEnter the Pokédex number of the pokemon, whose Ascii art you wanna see!!!")

d= 0

while d==0:
    pass
    break
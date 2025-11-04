import time
def mechine_print(text,delay=0.1):
    for letter in text:
        print(letter,end="",flush=True)
        time.sleep(delay)
    print()
mechine_print("Hello, JASIM PC. Do you have time for a game?")
delay=1
mechine_print("How about a game of chess?")
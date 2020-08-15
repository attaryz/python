def play(max):
    """play the guessing game!"""
    print(f"think of a number from 1 to {max}.")
    input("when you are ready, press Enter.")

    high = max 
    low = 1
    done = False
    count = 0

    while high != low and not done:
        count += 1
        guess = int((high + low) / 2)
        inp = prompt(guess)
        if inp == 'H':
            high = guess
        elif inp == 'L':
            low = guess
        else:
            done = True
            print(f"I guessed it in {count} times")

    if high == low and not done:
        print(f"i'm confused! you ruled out all the numbers.")

    if __name__ == '__main__':
        play(1000)
    
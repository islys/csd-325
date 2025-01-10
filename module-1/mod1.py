# Ryan Monnier
# CSD325
# Assignment 1
# 10 Jan 2025

# Importing time to slow down the 'song'
import time

# Countdown function that decrements n by 1
def countdown(n):
    while n > 0:
        # When there is only 1 bottle left
        if n == 1:
            print(f'\n{n} bottle of beer on the wall, {n} bottle of beer.')
            time.sleep(0.3)
            print("Take one down and pass it around, 0 bottles of beer on the wall.")
            time.sleep(0.3)
        # When there is more than 1 bottle left
        else:
            print(f'\n{n} bottles of beer on the wall, {n} bottles of beer.')
            time.sleep(0.3)
            print(f"Take one down and pass it around, {n-1} bottles of beer on the wall")
            time.sleep(0.3)
        # Decrease by 1 to continue the countdown
        n = n-1
    
# Main function 
def main():
    # Try/except Value Error to alert the user why the function doesn't work if they type something silly
    try:
        print("Enter number of bottles: ")

        n = int(input())
        countdown(n)
        print("\nTime to buy more bottles of beer.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# Calling the function
if __name__ == '__main__':
    main()
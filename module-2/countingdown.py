
import time

def non_recursive_num(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.5)

def main():
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Input should be a positive integer.")
    else:
        print(f"Non-recursive function for n = {n}")
        non_recursive_num(n)
        print("End of non-recursive function")

main()
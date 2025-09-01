import random

def main():
    print("Hello! I want to guess your age.")
    name = input("What's your name? ")  # notice the space at the end

    while True:
        guess = random.randint(15, 30)
        ans = input(f"Is your age {guess}? (y/n): ").strip().lower()

        if ans == "y":
            print(f"NICE, I've still got it")
            break
        elif ans == "n":
            print("Off season, let me try again")
        else:
            print("Please answer with 'y' or 'n'.")

if __name__ == "__main__":
    main()

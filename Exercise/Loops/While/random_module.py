import random
"""
# random() - return float value between 0.0 to 1.0 (excluded)
print(random.random())

# randomint(a,b) - return int value between a and b (both included)
num=int(input("Enter number you want to guess in between?"))
actual=random.randint(0,num)
guess=int(input("Enter your guessed number:"))
while guess!=actual:
    if guess>actual:
        print("Too high")
        guess=int(input("Enter your guessed number:"))
    else:
        print("Too low")
        guess=int(input("Enter your guessed number:"))
print("Got it!!")  

"""
# choice(sequence) - return a random items from a sequence
nums=[10,5,7,69,5,78]
print(random.choice(nums))

# shuffle(sequence) - returns the elements shuffled in random order
print(random.shuffle(nums))
print(nums)
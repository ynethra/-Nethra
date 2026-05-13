print("Welcome to the Quiz Game!")
print()
score = 0
answer = input("1. What is the capital of India? ").lower()
if answer == "delhi" or answer == "new delhi":
    print("Correct!")
    score += 1
else:
    print(" Wrong! The correct answer is New Delhi.")
print()
answer = input("2. Which programming language is known as the 'Snake Language'? ").lower()

if answer == "python":
    print("Correct!")
    score += 1
else:
    print(" Wrong! The correct answer is Python.")
print()
answer = input("3. How many days are there in a week? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")
print()
print(" Quiz Finished!")
print("Your score is:", score, "/ 3")
if score == 3:
    print(" Excellent!")
elif score == 2:
    print("Good job!")
else:
    print(" Keep practicing!")

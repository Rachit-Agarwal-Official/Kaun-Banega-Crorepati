# Kaun Banega Crorepati

# OBJECTIVES
# Create a program capable of displaying questions to the user like KBC
# Use list datatype to store the questions and their correct answers
# Display the final amount the person is taking home after playing the game

######################## ACTUAL CODE STARTS FROM HERE ########################

# Printing Starting lines of the program
a = input("!!Press Enter To Continue!!")
print("\nWelcome to the Kaun Banega Crorepati - Rachit's Edition\n")
print('''These are some points to remember while playing the game:-
1. All the answers can be either in uppercase or lowercase or capitalized
2. Use numbers in case you have to use
3. Check the spellings because mistakes will lead you to end
4. All the questions will give you a certain amount that will take place of your previous one
5. You'll only continue if the answer is correct otherwise you'll get the prize you have as your prize money and exit

And this Program is newly made so does not have all the correct answers so if you face any problem with it, please calm down we are still working on it...
''')
b = input("If you've read the points (Press Enter to continue)")


# Questions we have in the Quiz
questions = ["How many Bits makes one Byte?",
    "Google is a Browser or a Search Engine?",
    "Printer is the example of which types of device, Output or Input?",
    "What is the full form of RAM?",
    "Who is the founder of Facebook?",
    "Which electronic component was used in first generation of computers?",
    "All mathematical and logical functions in the computer are done by?",
    "Attempts made by individuals to obtain confidential information from you by falsifying their identity are called?",
    "Who was the programmer of Ms-Dos operating system?",
    "Full form of VIRUS is?",
    "1 Kilobyte is equal to how many bytes?",
    "Who is called Father of Computer?",
    "When you purchase a product over a Mobile Phone, the transaction is called?",
    "A formal language designed to communicate instructions to a machine, particularly a computer is called?",
    "The man who built the first Mechanical Calculator was?",
    "What contains specific rules and words that express the logical steps of an algorithm?"]


# Answers of the Questions according to the index
answers = ["8 bits",
    "search engine",
    "output device",
    "random access memory",
    "mark zuckerberg",
    "vaccum tubes",
    "central processing unit",
    "phising scams",
    "bill gates",
    "virtual information resource under seize.",
    "1024 bytes",
    "charles babbage",
    "m-commerce",
    "programming language",
    "blaise pascal",
    "syntax"]


# Prizes for every question according to the index 
prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]


# Initializing the winning amount
money_won = 0


# Question Generation and Answer Checking logic as a function
def KBC(ques, prize_money):
    print("\nQuestion " + str(ques) + ":", questions[ques-1], "(Wining prize is ₹" + str(prizes[ques-1]) + ")")  # Question Generation
    ans = input("Your Answer: ").lower()  # Input of the answer
    prize = 0

    # Answer Checking
    if ans == answers[ques-1]:
        print("Congratulation!! ₹" + str(prizes[ques-1]) + " is credited as your prize money")
        prize += prize_money
    else:
        print("\nOh! That's a wrong answer")

    return prize  # Returning the prize won either 0 or the prize of question


# Loop to give the arguments to the function 16 times one by one 
# This is used to reduce the code length
for i in range(16):
    prize = KBC(i+1, prizes[i])  # Function Call

    # Logic to exit or continue
    if prize == 0:
        print("!!Better Luck Next Time!!")
        break
    else:
        money_won = prize


# Printing the conclusive lines
print("\nYou won ₹" + str(money_won))
print("Thank you for your try")
print("Have a Great Day!\n")
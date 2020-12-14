import time
import random
print("MastMath by Cl.ne")
def funct():
    try:
        print("Welcome to MastMath")
        time.sleep(1)
        print("type '1' for addition")
        time.sleep(0.5)
        print("type '2' for division")
        time.sleep(0.5)
        print("type '3' for multiplication")
        time.sleep(0.5)
        typed = int(input("enter : "))

        if typed == 2:
            print("Division")
            print("In division there will be remainders, but ignoring them and just giving the answer to the question will be considered the correct answer")
            hardness = int(input("Difficulty(first number)")) * "9"
            hardness2 = int(input("Difficulty(Second number")) * 10
            hardness = int(hardness)
            questions = int(input("how many questions: "))
            rightanswers = 0
            wronganswers = 0
            while questions > rightanswers + wronganswers:
                num1 = random.randint(0, hardness)
                num2 = random.randint(0, hardness2)
                num1, num2 = str(num1), str(num2)
                answer = int(input(num1 + " ÷ " + num2 + ' = '))
                num1, num2 = int(num1), int(num2)
                reelanswer = num1 // num2
                if answer == reelanswer:
                    print("correct!")
                    rightanswers += 1
                    print("")
                if answer != reelanswer:
                    print("wrong, correct answer is ", reelanswer)
                    wronganswers += 1
            for i in range(0, 5):
                print("")
            print("congratulations you've finished all questions")
            print("")
            print("correct answer(s) : ", rightanswers)
            print("")
            print("wrong answer(s) : ", wronganswers)
            for i in range(0, 3):
                print("")
            time.sleep(1)
            print(" ")
            print("redirecting to main menu in")
            time.sleep(0.5)
            for i in range(5, -1, -1):
                print(i)
                time.sleep(0.75)
            funct()

        if typed == 3:
            print("Multiplication")
            hardness = int(input("Difficulty(first number)")) * "9"
            hardness2 = int(input("Difficulty(Second number")) * 10
            hardness = int(hardness)
            questions = int(input("how many questions: "))
            rightanswers = 0
            wronganswers = 0
            while questions > rightanswers + wronganswers:
                num1 = random.randint(0, hardness)
                num2 = random.randint(0, hardness2)
                num1, num2 = str(num1), str(num2)
                answer = int(input(num1 + " x " + num2 + ' = '))
                num1, num2 = int(num1), int(num2)
                reelanswer = num1 * num2
                if answer == reelanswer:
                    print("correct!")
                    rightanswers += 1
                    print("")
                if answer != reelanswer:
                    print("wrong, correct answer is ", reelanswer)
                    wronganswers += 1
            for i in range(0, 5):
                print("")
            print("congratulations you've finished all questions")
            print("")
            print("correct answer(s) : ", rightanswers)
            print("")
            print("wrong answer(s) : ", wronganswers)
            for i in range(0, 3):
                print("")
            time.sleep(1)
            print(" ")
            print("redirecting to main menu in")
            time.sleep(0.5)
            for i in range(5, -1, -1):
                print(i)
                time.sleep(0.75)
            funct()


        if typed == 1:
            print("Additions")
            hardness = int(input("Difficulty (starts from 1) : ")) * "9"
            hardness = int(hardness)
            questions = int(input("how many questions: "))
            rightanswers = 0
            wronganswers = 0
            while questions > rightanswers + wronganswers:
                num1 = random.randint(0, hardness)
                num2 = random.randint(1, hardness)
                num1, num2 = str(num1), str(num2)
                answer = int(input(num1 + " + " + num2 + ' = '))
                num1, num2 = int(num1), int(num2)
                reelanswer = num1 + num2
                if answer == reelanswer:
                    print("correct!")
                    rightanswers += 1
                    print("")
                if answer != reelanswer:
                    print("wrong, correct answer is ", reelanswer)
                    wronganswers += 1
            for i in range(0, 5):
                print("")
            print("congratulations you've finished all questions")
            print("")
            print("correct answer(s) : ", rightanswers)
            print("")
            print("wrong answer(s) : ", wronganswers)
            for i in range(0, 3):
                print("")
            time.sleep(1)
            print(" ")
            print("redirecting to main menu in")
            time.sleep(0.5)
            for i in range(5, -1, -1):
                print(i)
                time.sleep(0.75)
            funct()

    except:
        print("answer correctly please.")
        funct()
funct()
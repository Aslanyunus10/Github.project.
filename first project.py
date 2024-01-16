question_1 = input("Where is the capital city of England?")

score = 0

if int(question_1) == 'London':
    score = score + 10
    print("Awesome! Your answer is true.")

else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)


question_2 = input("What is the fastest animal on the world?")

if int(question_2) == 'Cheetah':
    score = score + 10
    print("Awesome! Your answer is true.")

else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)


question_3 = input("What is the result of 9999*0")

if int(question_3) == 0:
    score = score + 10
    print("Awesome! Your answer is true.")

else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)


question_4 =  input("What is the slowest animal on the world?")

if int(question_4) == 'Turtle':
    score = score + 10
    print("Awesome! Your answer is true.")

else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)


question_5 =  input("how many week in each year?")

if int(question_5) == 52:
    score = score + 10
    print("Awesome! Your answer is true.")

else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)


if score >= 40:
    print("Congratulations!,you did it:))))")
else:
    print("Sorry,please try again...")
    

print("Total score is -->", score)

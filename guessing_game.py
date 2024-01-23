question_1 = input("Where is the capital city of England? ")

score = 0

if question_1.lower() == 'london':
    score += 20
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)

question_2 = input("What is the fastest animal in the world? ")

if question_2.lower() == 'cheetah':
    score += 10
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)

question_3 = input("What is the result of 9999 * 0? ")

if int(question_3) == 0:
    score += 20
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)

question_4 = input("What is the slowest animal in the world? ")

if question_4.lower() == 'turtle':
    score += 10
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)

question_5 = input("How many weeks in each year? ")

if int(question_5) == 52:
    score += 10
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")

print("Your score is -->", score)


question_6 = input("According to 2023 data, what is the population in the USA?\n"
                   "A) 331,000,000\n"
                   "B) 321,000,000\n"
                   "C) 341,000,000\n"
                   "D) 311,000,000\n")

if question_6.upper() == 'A':
    score += 30
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")


question_7 = input("Which is the 5th country that managed to land a vehicle on the moon recently? \nA)'Gemany'\nB)'Japan'\nC)'South Korea'\nD)'France'\n")

if question_7.upper() == 'B':
    score = score + 50
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")

question_8 = input("According to December 2023 data, which country's passport is the most powerful in the world, which can enter 160 countries, leaving Singapore behind? \nA)'Japan'\nB)'Singapore'\nC)'USA'\nD)'Spain'\n")

if question_8.upper() == 'D':
    score = score + 100
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")

question_9 = input("How many more Ballon d'Or awards does Lionel Messi, who broke his own record by winning the 8th Ballon d'Or award last year, have than his closest rival, Cristiano Ronaldo? \nA)3\nB)2\nC)4\nD)1\n")

if question_9.upper() == 'A':
    score = score + 60
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")

question_10 = input("What is the name of the person who assassinated former US President John Kennedy? ")

if question_10 == 'Lee Harvey Oswald':
    score = score + 100
    print("Awesome! Your answer is true.")
else:
    print("Unfortunately :( Your answer is wrong.")

if score >= 350:
    print("Congratulations!, you did it:))))")
else:
    print("Sorry, your knowledge is not enough, please try again...")

print("Total score is -->", score)




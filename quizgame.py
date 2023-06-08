print("Grand Welcome To Quiz Game")

playing = input("Do You want to play game? ")

if playing.lower() != "yes":
    quit()
else:
    print("ok lets play the Game")

score = 0
wrong_score = 0


q1 = input("what is the full form of oops? ")

if q1.lower() == "object oriented programming language":
    print("Correct..!")
    score += 1
else:
    print("Wrong..!")
    wrong_score += 1


q2 = input("what is the full form of API? ")
if q2.lower() == "application programming interface":
    print("Correct")
    score += 1

else:
    print("wrong answer")
    wrong_score += 1


q3 = input("how many types of loops are there in python? ")
if q3.lower() == "two":
    print("Correct")
    score += 1

else:
    print("wrong answer")
    wrong_score += 1


q4 = input("lists is mutable or immutable? ")
if q4.lower() == "mutable":
    print("Correct")
    score += 1

else:
    print("wrong answer")
    wrong_score += 1


q5 = input("tuple is mutable or immutable? ")
if q5.lower() == "immutable":
    print("Correct")
    score += 1

else:
    print("wrong answer")
    wrong_score += 1


print("Total Right Answers are " + str(score))
print("Total Wrong Answers are " + str(wrong_score))

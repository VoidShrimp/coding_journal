#learning to code in python
def main():
    i = 1
    while i < 2:
        score = int(input("What is your score? "))
        if 100 >= score >= 0:
            grade_student(score)
            i+=1
        else:
            print("Invalid answer")

def grade_student(score):
    if score > 90:
        print("You got an A")
    elif 90 > score > 80:
        print("You got a B")
    elif 80 > score > 70:
        print("You got a C")
    elif 70 > score > 60:
        print("You got a D")
    else:
        print("You got an F")
    return score

main()
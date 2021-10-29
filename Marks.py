# GROUP A ASSIGNMENT 2
"""Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency"""

def MainMenu():
    print("************MENU************")
    print("1) Average Score of the Class")
    print("2) Highest Score of the Class")
    print("3) Count of students who were absent for the class")
    print("4) Display marks with highest frequency")
    print("5) Exit")
    ch = int(input("Enter your choice"))

    if ch == 1:
        avgScore()
        print("************************")
        MainMenu()

    elif ch == 2:
        highScore()
        lowScore()
        print("************************")
        MainMenu()

    elif ch == 3:
        absentStudent()
        print("************************")
        MainMenu()

    elif ch == 4:
        medianScore()
        print("************************")
        MainMenu()

    elif ch == 5:
        exit()

    else:
        print("Enter a valid choice")
        MainMenu()


def avgScore():
    global q
    n = len(marks)
    print("Strength of the class is",n)
    count = 0
    avg = 0
    num = []
    for x in marks:
        if type(x) == type(" "):
            count = count + 1
        else:
            num.append(x)
        q = sum(num)
    avg = int(q/(n-count))
    print("Average :", avg)


def highScore():
    max = 0
    count = 0
    for x in marks:
        if type(x) == type(" "):
            count = count + 1
        elif x > max:
            max = x
    print("Highest Score is", max)


def lowScore():
    min = 99
    count = 0
    for x in marks:
        if type(x) == type(" "):
            count = count + 1
        elif min > x:
            min = x

    print("Lowest Score is", min)


def absentStudent():
    absent = 0
    for x in marks:
        if type(x) == type('AB'):
            absent = absent + 1
    print("No of absent students ", absent)


def medianScore():
    cnt = high = p = mm = 0
    counting = []
    for n in range(31):
        cnt = 0
        for x in marks:
            if type(x) == type(" "):
                p = p + 1
            elif x == n:
                cnt = cnt + 1
        counting.append(cnt)

    print("Frequency of marks")
    print(counting)
    for y in counting:
        if y > high:
            high = y

    for z in range(31):
        if counting[z]==high:
            print("Median is",z)



print("Marks scored in Fundamentals of Data Structure")
marks = ['NA', 12, 30, 'AB', 'AB', 'AB', 28, 29, 9, 18, 30, 10, 11, 12, 12, 20]
print(marks)
MainMenu()
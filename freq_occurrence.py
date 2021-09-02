# to determine the frequency of occurrence of a particular character

print("to determine the frequency of occurrence of a particular character")
str1 = input("Enter the string")
char = input("Enter the character")

counter = 0

for i in range(len(str1)):
    if char == str1[i]:
        counter += 1

print("The number of {} is {}".format(char, counter))

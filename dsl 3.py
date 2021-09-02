# String with the longest word

print("String with the longest word")
str1 = input("Enter the string")
list1 = str1.split()
m = 0  # checks each character
word = 0
print(list1)
for i in range(len(list1)):
    len(list1[i])
    if m < len(list1[i]):
        m = len(list1[i])
        word = i

print("The longest word in the list is", list1[word])

# to determine the frequency of occurrence of a particular character

print("to determine the frequency of occurrence of a particular character")
str1 = input("Enter the string")
char = input("Enter the character")

counter = 0

for i in range(len(str1)):
    if char == str1[i]:
        counter += 1

print("The number of {} is {}".format(char, counter))

# to count the occurrence of each word in the string
print("to count the occurrence of each word in the string")

str1 = input("Enter a string")
list1 = str1.split()
list2 = set(list1)
list3 = list(list2)
print(list1)
print(list3)
list4 = []
list5 = []
counter = 0
for i in range(len(list3)):
    counter = 0
    for j in range(len(list1)):
        if list3[i] == list1[j]:
            counter += 1
    list4 = list3[i], counter
    list5.append(list4)

print("\n", list5)

# to check whether the given string is a palindrome or not
print("to check whether the given string is a palindrome or not")
str2 = input("Enter the string\n")
lenstr2 = len(str2)
j = lenstr2 - 1
print(lenstr2)
flag = 0
for i in range(int(lenstr2 / 2 + 1)):
    if str2[i] == str2[j]:
        flag = 1
    else:
        break
    j -= 1

if flag == 1:
    print("\n It is a palindrome")
else:
    print("\n It is not a palindrome")

# to display the index of the first appearance of a substring
print("to display the index of the first appearance of a substring")
str1 = input("Enter the string")
sub1 = input("Enter the substring")

sublength = len(sub1)
index1 = 0
j = 0

for i in range(len(str1)):
    if sub1[j] == str1[i]:
        flag = 1
        print(sub1[j], i, j)
        j += 1

        if j == sublength:
            index = i - (sublength - 1)
            break
    else:
        flag = 0
        j = 0

print("substring index :", index1)

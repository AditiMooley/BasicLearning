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

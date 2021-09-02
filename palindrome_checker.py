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
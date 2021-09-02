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

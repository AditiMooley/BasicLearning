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
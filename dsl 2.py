# Input supply
# D 300
# D 300
# W 200
# W 100


def deposit(num):
    global balance
    balance = balance + num


def withdrawal(num):
    global balance
    if balance > num:
        balance = balance - num


list1 = []
balance = 0

while True:
    data = input("Enter the transaction details:\n")
    if 'EXIT' == data:
        break
    list1.append(data.split())
print(list1)

for var in list1:
    if var[0] == 'D':
        deposit(int(var[1]))
    elif var[0] == 'W':
        withdrawal(int(var[1]))

print("Balance is:", balance)

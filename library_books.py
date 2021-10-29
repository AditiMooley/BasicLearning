"""Write a Python program for department library which has N books, write functions for
following:
a) Delete the duplicate entries
b) Display books in ascending order based on cost of books
c) Count number of books with cost more than 500.
d) Copy books in a new list which has cost less than 500."""

library = {}
books = []
costs = []
n = int(input("Enter the number of books in the Library"))
a = 0
for a in range(n):
    book = input("Enter the name of the book")
    cost = int(input("Enter the cost of the book"))

    library.update({book: cost})  # unimportant but there a colon, not a comma
    books.append(book)
    costs.append(cost)

for m, n in zip(books, costs):  # zip presents two lists together according to the order of the elements
    print("{} is available for {}".format(books, costs))
print("***********************************")


def deleteDuplicates():
    for i in library.items():
        print("This library has :", i)
    print("***********************************")


def ascOrder():
    sorted_library = sorted(library.items(), key=lambda x: x[1])  # A lambda function is a small anonymous function.
    # A lambda function can take any number of arguments, but can only have one expression.
    print("Sorted library :")
    for i in sorted_library:
        print(i)
    print("***********************************")


def moreThan500():
    highcost500 = []

    for (i, j) in zip(books, costs):
        if j > 500:  # need to specify where j>500 should be, otherwise you'll get an error
            highcost500.append((i, j))
            
    print("The following books cost more than 500: {}".format(highcost500))
    print("There are {} books in this list".format(len(highcost500)))
    print("***********************************")


def lessThan500():
    lowcost500 = []

    for (i, j) in zip(books, costs):
        if j < 500:
            lowcost500.append((i, j))

    print("The following books cost less than 500", lowcost500)
    print("There are {} books in this list".format(len(lowcost500)))
    print("***********************************")


deleteDuplicates()
ascOrder()
moreThan500()
lessThan500()

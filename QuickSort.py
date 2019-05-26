# AUTHOR: Luis Enrique Neri Pérez
# Copyright 2019

# This is an implementation of the Quicksort Algorithm
# that sorts a txt file with numbers

def Quicksort(unorderedList):

    if len(unorderedList) == 0:
        return unorderedList

    div = unorderedList[0]
    before = []
    after = []

    for i in range(1, len(unorderedList)):
        if unorderedList[i] < div:
            before.append(unorderedList[i])
        else:
            after.append(unorderedList[i])

    before = Quicksort(before)
    after = Quicksort(after)

    before.append(div)

    for e in after:
        before.append(e)

    return before

def openFile():
    file = open('numbers.txt', 'r')
    lines = file.read()
    lines = lines.split(",")

    for i in range(0, len(lines)):
        lines[i] = int(lines[i])
    return lines


def main():
    lines = openFile()
    print("\nQUICK SORT\n")
    print("Unordered: " + str(lines))
    print("Ordered: " + str(Quicksort(lines)))

main()
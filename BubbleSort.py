# AUTHOR: Luis Enrique Neri Pérez
# Copyright 2019

# This is an implementation of the Bubblesort Algorithm
# that sorts a txt file with numbers


def BubbleSort(unorderedList):
    not_sorted=True

    while(not_sorted):
        not_sorted=False

        for i in range(0, len(unorderedList)-1):
            if(unorderedList[i]>unorderedList[i+1]):
                temp=unorderedList[i]
                unorderedList[i]=unorderedList[i+1]
                unorderedList[i+1]=temp
                not_sorted=True

    return unorderedList

def openFile():
    file = open('numbers.txt', 'r')
    lines = file.read()
    lines = lines.split(",")

    for i in range(0, len(lines)):
        lines[i] = int(lines[i])
    return lines


def main():
    lines = openFile()
    print("\nBUBBLE SORT\n")
    print("Unordered: " + str(lines))
    print("Ordered: " + str(BubbleSort(lines)))

main()
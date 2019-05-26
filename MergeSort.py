# AUTHOR: Luis Enrique Neri Pérez
# Copyright 2019

# This is an implementation of the Mergeesort Algorithm
# that sorts a txt file with numbers

def MergeSort(list):
    if len(list)==1:
        return list

    midpoint = len(list)/2

    list1 = []
    list2 = []
    counter = 0
    for element in list:
        if counter < midpoint:
            list1.append(element)
        else:
            list2.append(element)
        counter +=1

    list1 = MergeSort(list1)
    list2 = MergeSort(list2)

    Flist = []
    while(len(list1)>0 and len(list2)>0):
        if(list1[0]<=list2[0]):
            Flist.append(list1.pop(0))
        else:
            Flist.append(list2.pop(0))
    for i in range(0,len(list1)):
            Flist.append(list1.pop(0))
    for i in range(0,len(list2)):
            Flist.append(list2.pop(0))

    return Flist

def openFile():
    file = open('numbers.txt', 'r')
    lines = file.read()
    lines = lines.split(",")

    for i in range(0, len(lines)):
        lines[i] = int(lines[i])
    return lines


def main():
    lines = openFile()
    print("\nMERGE SORT\n")
    print("Unordered: " + str(lines))
    print("Ordered: " + str(MergeSort(lines)))

main()
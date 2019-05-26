# AUTHOR: Luis Enrique Neri Pérez
# Copyright 2019

# This is an implementation of the Radixsort Algorithm
# that sorts a txt file with numbers

def rSort(list):
    q0 = []
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    q6 = []
    q7 = []
    q8 = []
    q9 = []
    mod = 10
    max = 0

    for d in list:
        if len(str(d)) > max:
            max = len(str(d))

    for i in range(1, max+1):

        for e in list:
            if len(str(e)) < i:
                q0.append(e)
            else:
                dig = e % mod

                while len(str(dig))!=1:
                    dig//=10


                if dig==1:
                    q1.append(e)

                elif dig==2:
                    q2.append(e)

                elif dig==3:
                    q3.append(e)

                elif dig==4:
                    q4.append(e)

                elif dig==5:
                    q5.append(e)

                elif dig==6:
                    q6.append(e)

                elif dig==7:
                    q7.append(e)

                elif dig==8:
                    q8.append(e)

                elif dig==9:
                    q9.append(e)

                elif dig==0:
                    q0.append(e)
            list = q0 + q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9

        q1 = []
        q2 = []
        q3 = []
        q4 = []
        q5 = []
        q6 = []
        q7 = []
        q8 = []
        q9 = []
        q0 = []


        mod = 10 * mod
    return list



def RadixSort(unorderedList):

    possitive=[]
    negative=[]

    for d in unorderedList:
        if(d<0):
            negative.append(-d)
        else:
            possitive.append(d)

    possitive = rSort(possitive)
    negative = rSort(negative)

    for i in range(0, len(negative)):
        possitive.insert(0,-negative[i])

    return possitive


def openFile():
    file = open('numbers.txt', 'r')
    lines = file.read()
    lines = lines.split(",")

    for i in range(0, len(lines)):
        lines[i] = int(lines[i])
    return lines


def main():
    lines = openFile()
    print("\nRADIX SORT\n")
    print("Unordered: " + str(lines))
    print("Ordered: " + str(RadixSort(lines)))

main()
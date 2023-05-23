# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from array import array


def naive_search(arr, target):
    find = False
    for aux in range(len(arr)):
        if ~find:
            if arr[aux] == target:
                print("I finded it´s: " + str(arr[aux]))
                bol = True
                break
            elif arr[aux] == arr.__len__()-1:
                print("It´s not on the array")

def binarySearch(arr, target, low, high):
    mid = len(arr)/2
    if arr[int(mid)] == target:
        print(mid)
    elif target < arr[int(mid)]:
        return binarySearch(arr, target, low, mid-1)
    else:
        return binarySearch(arr + 1, target, mid+1, high)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    length = 10000

    sortedlist = set()
    while len(sortedlist) < length:
        sortedlist.add(random.randint(-3*length, 3*length))
    sortedlist = sorted(list(sortedlist))

    arr = array('i', [])
    for i in range(12):
        arr.append(i)

    naive_search(sortedlist, 11)
    binarySearch(sortedlist, 2, 1, 1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#write a function to reverse a string
def rev_string(n):
    n = n[::-1]
    return(n)

print(rev_string("12345string"))

#find the first non repeating character in a string
def dont_repeat(y):
    x = len(y)
    for i in range(x):
        no_repeat = True
        for o in range(x):
            if i != o and y[i] == y[o]:
                no_repeat = False
                break
        if no_repeat:
            return(y[i])
    return("all repeat!")

print(dont_repeat("ssttrrinngg"))

#merge 2 arrays into one
def merge_arrays(arr1, arr2, size1, size2, arr3):
    i = 0
    j = 0
    k = 0
    while(i < size1):
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1
    while(j < size2):
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
    arr3.sort()

if __name__ == '__main__':

    arr1 = [1, 3, 5, 7, 9, 11]
    size1 = len(arr1)

    arr2 = [0, 2, 4, 6, 8, 10]
    size2 = len(arr2)
    arr3 = [0 for i in range(size1 + size2)]
    merge_arrays(arr1, arr2, size1, size2, arr3)

    print("array 1 = ",arr1)
    print("array 2 = ",arr2)
    print("merged array = ",arr3)


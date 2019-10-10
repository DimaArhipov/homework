my_array = [446, 510, 915, 218, 160, 516, 548,261, 841, 862, 797, 655, 829, 290, 85]

for i in range(len(my_array)-1):
    for j in range(len(my_array)-i-1):
        if my_array[j] > my_array[j+1]:
            buff = my_array[j]
            my_array[j] = my_array[j+1]
            my_array[j+1] = buff
print(my_array)

array_2 = [271, 986, 177, 968, 364, 236, 48, 107, 495, 948, 382, 144, 821, 887, 575]

for i in range(len(array_2)):
    v = array_2[i]
    j = i
    while array_2[j-1] > v and j > 0:
        array_2[j] = array_2[j-1]
        j = j - 1
    array_2[j] = v
print(array_2)

array_3 = [670, 673, 88, 727, 311, 952, 471, 376, 443, 187, 431, 951, 108, 425, 471]

for i in range(len(array_3)):
    min = i
    for j in range(i+1, len(array_3)):
        if array_3[j] < array_3[min]:
            min = j
        tmp = array_3[min]
        array_3[min] = array_3[i]
        array_3[i] = tmp
print(array_3)


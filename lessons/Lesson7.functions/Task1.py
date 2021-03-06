# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  #  "0-4, 7-8, 10"
# get_ranges([4,7,10])  # "4, 7, 10"
# get_ranges([2, 3, 8, 9])  # "2-3, 8-9"

def groups(a):
    last = -2
    start = -1
    p = []
    for i in a:
        if i != last+1:
            if start != -1:
                p.append([start, last])
            start = i
        last = i
    p.append([start, last])
    for i in p:
        if i[0] == i[-1]:
            print(i[0], end=" ")
        else:
            print(*i, sep="-", end=" ")


a = list(map(int, input().split()))
groups(a)

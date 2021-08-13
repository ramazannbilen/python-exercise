"""

"""

from edabit.Test import Test

if __name__ == '__main__':

    a = [[0,1,2],[3,4,5],[6,7,8]]
    print(a[1][1])

    #a = "alphabet"
    #b = ""
    #print(b.join(sorted(a)))


    # How to sort a Python dict by value
    # (== get a representation sorted by value)
    """>> > xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

    >> > sorted(xs.items(), key=lambda x: x[1])
    [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

    # Or:

    >> > import operator
    >> > sorted(xs.items(), key=operator.itemgetter(1))
    [('d', 1), ('c', 2), ('b', 3), ('a', 4)]"""

    # a = [{"adı":"ahmet","age":15},{"adı":"mehmet","age":30}]
    # b = [i["age"] for i in a]
    # print(sum(b))

    # lst = [0,1,2,3,4]
    # lst.remove(lst[0])
    # lst.insert(len(lst),5)
    # print(lst.remove(lst[0]))
    # print(lst)

    # print(list(ab.values()))

    """lst1 = [0, 0, 0, 0, 0]
    lst2 = [i for i in enumerate(lst1)]

    indexes = []
    for i in lst2:
        indexes.append(i[0])

    new =[]
    for i in range(len(lst1)):
        new.append(lst1[i]+indexes[i])
    print(new)"""

    # tahta = [["_", "_", "_"],
    #          ["_", "_", "_"],
    #          ["_", "_", "_"]]
    #
    # print("\n" * 15)
    #
    # for i in tahta:
    #     print("\t".expandtabs(30), *i, end="\n" * 2)
    #
    # kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
    #                      [[0, 1], [1, 1], [2, 1]],
    #                      [[0, 2], [1, 2], [2, 2]],
    #                      [[0, 0], [0, 1], [0, 2]],
    #                      [[1, 0], [1, 1], [1, 2]],
    #                      [[2, 0], [2, 1], [2, 2]],
    #                      [[0, 0], [1, 1], [2, 2]],
    #                      [[0, 2], [1, 1], [2, 0]]]
    #
    # x_durumu = []
    # o_durumu = []
    #
    # sıra = 1
    # while True:
    #     if sıra % 2 == 0:
    #         işaret = "X".center(3)
    #     else:
    #         işaret = "O".center(3)
    #
    #     print()
    #     print("İŞARET: {}\n".format(işaret))
    #
    #     x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
    #     if x == "q":
    #         break
    #
    #     y = input("soldan sağa [1, 2, 3]: ".ljust(30))
    #     if y == "q":
    #         break
    #
    #     x = int(x) - 1
    #     y = int(y) - 1
    #
    #     print("\n" * 15)
    #
    #     if tahta[x][y] == "_":
    #         tahta[x][y] = işaret
    #         if işaret == "X".center(3):
    #             x_durumu += [[x, y]]
    #         elif işaret == "O".center(3):
    #             o_durumu += [[x, y]]
    #         sıra += 1
    #     else:
    #         print("\nORASI DOLU! TEKRAR DENEYİN\n")
    #
    #     for i in tahta:
    #         print("\t".expandtabs(30), *i, end="\n" * 2)
    #
    #     for i in kazanma_ölçütleri:
    #         o = [z for z in i if z in o_durumu]
    #         x = [z for z in i if z in x_durumu]
    #
    #         if len(o) == len(i):
    #             print("O KAZANDI!")
    #             quit()
    #         if len(x) == len(i):
    #             print("X KAZANDI!")
    #             quit()

    # cm = 0.0005
    # n = 3
    # for i in range(n):
    #    cm *= 2
    # print(cm)

    # a = [1, 1, 2, 2, 3, 3]
    # b = [i for i in lst if i != el]
    # # count = 0
    # # for i in a:
    # #     if i == 1:
    # #         count += 1
    # print(b+[1,1])

# a = "11:22"
# x = a.split(":")
# m = int(x[0]) * 60
# s = int(x[1])
# if int(x[1]) >= 60:
#     print("false")
# else:
#     print(m + s)

# def calculator():
# diamet = int(write.get())
# radius = diamet / 2
# area = radius * math.pi ** 2
# circumference = radius * math.pi * 2
#
# yazı.config(text="Results:")
# yazı1 = tkinter.Label(text="Radius this circle:")
# yazı1.pack()
# yazı2 = tkinter.Label(text=radius)
# yazı2.pack()
#
# yazı3 = tkinter.Label(text="Area this circle:")
# yazı3.pack()
# yazı4 = tkinter.Label(text=area)
# yazı4.pack()
#
# yazı5 = tkinter.Label(text="Circumference this circle:")
# yazı5.pack()
# yazı6 = tkinter.Label(text=circumference)
# yazı6.pack()
#
#
# # **ilk bölüm**
# window = Tk()
# window.title("Circle")
# window.geometry("400x400")
#
# yazı = tkinter.Label(window, text="plase entry diameter of the circle by cm")
# yazı.pack()
#
# write = tkinter.Entry(window)
# write.pack()
#
# buton = tkinter.Button(window, text="Enter", command=calculator)
# buton.pack()
#
# window.mainloop()

# print("{akisi} {soyad} {bkisi} {soyad}'in kardeşidir. {akisi} {bkisi}'den 10 yaş küçüktür".format(akisi="zafer",
# soyad = "bilen",
# bkisi = "ramazan"))

# meyveler = ["elma", "armut"]

# for sıra, öğe in enumerate(meyveler, 1):
#    print("{}. {}".format(sıra, öğe))

# li = list(range(10))
# type(li)
# print(li)

# print(*range(10))

# name = "Ramazan Bilen"
# namee = list(name)
# print(namee)

#     sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]
#
#     for i in sayılar:
#         print(*range(*i))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return (n * factorial(n - 1))
#
# print(factorial(3)

# mylist = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     mylist[i - 1] = mylist[i]
#
# for i in range(0, 6):
#     print(mylist[i], end=" ")

# x = "a1b1c1d"
# print(x.split("1"))

# a = [1, 2, 3, 4, 5, 6]
# print(a.pop())  # removes 6 but print the removed item.
# print(a)  # prints a except removed item.

# a1 = "kadir"
# b1 = "bilen"
# print(a1 + " " + b1)

# def pol(txt):
#     if len(txt) < 3:
#         first3 = txt
#     else:
#         first3 = txt[:3]
#
#     return first3 + first3 + first3
#
#
# print(pol("ramazan"))
# print(pol("kadir"))

# a = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]]
# print(len(a[0]))

# for i in range(3):  # i takes 0,1 and 2.
#     print(i)

# for r in a:
#     print(r, end=" ")

# tup = (4,3,2,1,0)
# lst = [0,1,2,3,4]
# if tup.index(2) == lst[-3]:
#     print("True")
# else:
#     print("False")

# a = np.array[[[1, 2], [4, 5], [7, 8]]]
# print(a[[0,0,0],[1,0,1]])

# def pol(x, y):
#     print("sl: ", x, y)
#     while x > y:
#         x -= 4
#         y += 3
#     print("el: ", x, y)
#     return x
# x = 15
# y = 8
# y = pol(x,y)
# print("afc: " ,x,y)
# pol(y,x)
# print("asc: " ,x,y)

# a = "kadir"
# print(len(a))  # returns 5

# from random import *
#
# a = randint(0,4)
# b = "zafer"
# c = b[a]
# print(c)

# a = 3 * 5 % 4
# print(a)
# a = "ramazan"
# wovels = ["a", "e", "i", "o", "u"]
# num = 0
# for i in a:
#     if i in wovels:
#         num = +1
#     else:
#         num = num
# print(num)"""

# python
# notlarım

# a=[1, 2, 3, 4, 5]
#print(2**13)

ab = {"a":1,"b":2,"c":3}
b = list(ab.keys())
print(ab["a"])


# import webbrowser as wb
#
# a = wb.get("https://eksisozluk.com/")
# a.
#
# def find_word(site, word):
#     site = input("with https give me a website: ")
#     word = input("give me a word to look for: ")

"""a =[BackgroundBrowser
BaseBrowser
Chrome
Chromium
Elinks
Error
Galeon
GenericBrowser
Grail
Konqueror
Mozilla
Netscape
Opera
UnixBrowser
WindowsDefault
get
main
open
open_new
open_new_tab
os
register
register_X_browsers
register_standard_browsers
shlex
shutil
subprocess
sys
threading]"""

# home_page = wb.open("https://eksisozluk.com/")
# print(type(home_page))

# harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
# çevrim = {i: harfler.index(i) for i in harfler}
#
# def sırala(kelime):
#     return ([çevrim.get(kelime[i]) for i in range(len(kelime))])
#
# isimler = ['ahmet', 'can', 'iskender', 'cigdem',
#            'ismet', 'ismail', 'ismit', 'çiğdem',
#            'ismıt', 'ışık', 'şule']
#
# print(*sorted(isimler, key=sırala), sep='\n')

# türkçe karakterlerle sıralama hatası almamak için kullan
# import locale
# locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
# isimler = ['ahmet', 'çiğdem', 'ışık', 'şebnem', 'zeynep', 'selin']
# sorted(isimler, key=locale.strxfrm)

# class team:
#     country = "ramo"
#
#     def __init__(self, name, color1, color2, players, coach):
#         self.name = name
#         self.color1 = color1
#         self.color2 = color2
#         self.players = players
#         self.coach = coach
#
# a1 = team("chelsea","white","blue",11,"Me")
# print(a1.country,a1.name,a1.coach,a1.color1,a1.color2,a1.players)

# x = "a"
# print(ord(x))

# for i in range(128):
#     if i % 4 == 0:
#         print("\n")
#
#     print("{:<3}{:>8}\t".format(i, repr(chr(i))), sep="", end="")

# for f in dosyalar:
#     okunan = open(f, 'rb').read(10)
#     if okunan[6:11] in [b'JFIF', b'Exif']:
#         print("{} adlı dosya bir JPEG!".format(f))
#     elif okunan[:8] == b"\211PNG\r\n\032\n":
#         print("{} adlı dosya bir PNG!".format(f))
#     elif okunan[:3] == b'GIF':
#         print("{} adlı dosya bir GIF!".format(f))
#     elif okunan[:2] in [b'II', b'MM']:
#         print("{} adlı dosya bir TIFF!".format(f))
#     elif okunan[:2] in [b'BM']:
#         print("{} adlı dosya bir BMP!".format(f))
#     else:
#         print("Türü bilinmeyen dosya: {}".format(f))

# *args ** kwargs
# lambda (lambda x: x + 1)(2) = lambda 2: 2 + 1
# = 2 + 1
# = 3
#
# while / break * true
# for
#     arrays[] - -- array_name[x]: the
#     x
#     th
#     value
#     of
#     an
#     array
# isinstance()
# eval()
# x == 0
# but
# x = "ramo"
# not ==
# int(str) and str(int)
# methods
# swap
# integers: tmp = x
# x = y
# y = tmp
#
# boolean: True
# False
# value
# name
#
# append: arrayname.append(kural): kurala
# göre
# arrayname
# adlı
# bir
# array
# oluşturur
#
# max(), min()
# of
# an
# array
# Aggregations
# sum(array_name)
# for integers only
#     enumarate()
#
#
# def first2(s):
#     return s[:2]
#     string
#     ifadenin
#     ilk
#     iki
#     harfini
#     çağırma
#     fonksiyonu
#
#
# round(number, x)  # x=after comma how many number will exist
#
# pow(m, n)
# m
# üzeri
# n
# fonksiyonu
# dict_name
# {a: b, b: c, .....}
# a = b, b = c
# you
# can
# call
# the
# elements
# of
# dict
# by
# dict_name.get(a or b or anything)
# eval()
#
# The
# try block lets you test a block of code for errors.
#
# The except block
# lets
# you
# handle
# the
# error.
#
# The finally block
# lets
# you
# execute
# code, regardless
# of
# the
# result
# of
# the
# try- and except blocks.
#
# githup
# projects
# kısmından
# trello
# gibi
# kullanabilirsin
#
# count()
# method
# counts
# strings or integers in a
# string or an
# integer.You
# can
# also
# use
# a
# substring
# like
# that: string.count(substring)
# split(x)
# method
# divide
# a
# string or integer
# by
# x.
# len()
# the
# length
# of
# an
# array_name - int
# ve
# float
# un
# len
# i
# olmaz
#
# .upper()
# .capitalize()
# .replace(old, new, count: optional)
# .strip()
# boşlukalrı
# sil
# sep ? separate
# .split()
# kelime
# kelime
# ayırır
#
# for i in range(x):
#     vs
#     break or continue
#     break: keser
#     cont: o
#     değeri
#     almayıp
#     while döndürmeye devam eder
#
# zip: iki
# array
# i
# fermuar
# gibi
# birleştirir
# 1.1, 2.2, 3.3
# gibi
#
#
# def =>
#
#
# d = {"key": value, "course": 2}
# d["key"]
# run
# value
# key
# uniqe
# value
# not
#
# .keys()
# .values()
# .items()
#
#
# def in içinde
#
#
# returnle
# değer
# döndürürsem
# o
# fonksiyonu
# bir
# parametreye
# eşitleyebilirim
# ama
# defin
# içinde
# printle
# bastırırsam
# o
# fonksiyonu
# bir
# parametreye
# eşitleyemem.
#
# capLetter = False
# True
#
# lambda x: x + 1(2)
#
# from module import function or *
#
# try:
#     ıusdgvıusdh
#     return or print
#     smyhing
#
# except errorname:
#     do
#     smt
# finally:
#     raise errorname
#
# listname.pop(x) = listenin
# x.operatörünü
# kaldırı
# vr
# kaldırdığı
# variableyi
# basar.tekrar
# listeyi
# basarsan
# onsuz
# basar.
# pop()
# şeklinde
# boş
# olursa
# son
# objeyi
# siler.
#
# numpy is a
# library
# for python
#
# arrange(start, finish,
# raise)
# linspace
# arrange in float
# hali
#
# shape and reshape
# have
# same
# items
# ravel()
# argmax and argmix
# give
# index
# of
# them
#
# vstack(axis=0) and hstack(axis=1)
#
# concatenate
#
# Slicing
#
# pandas
#
# loc and iloc
#
# ignore
# index = true
#
# regular
# expressions --> import re
#
# (learn it)
#
# ord() and chr()
# are
# inverse
#
# swapcase()
# büyükse
# küçük
# küçükse
# büyük
# yapar
#
# eval()
# convert
# string
# to
# expression in as simple
# math
#
# x[::-1]
# reverse
# string
#
# a, *b, c = [1, 2, 3, 4, 5, 6]
# a = 1
# c = 6
# b = [2, 3, 4, 5]

# # The standard string repr for dicts is hard to read:
# >> > my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
# >> > my_mapping
# {'b': 42, 'c': 12648430. 'a': 23}  # 😞
#
# # The "json" module can do a much better job:
# >> > import json
# >> > print(json.dumps(my_mapping, indent=4, sort_keys=True))
# {
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }
#
# # Note this only works with dicts containing
# # primitive types (check out the "pprint" module):
# >> > json.dumps({all: 'yup'})
# TypeError: keys
# must
# be
# a
# string

# with open(r"C:\Users\ramazan.bilen\Desktop\deneme_file.txt","w") as dosya:
#     dosya.write("hi ahmet how r u")
#
# with open(r"C:\Users\ramazan.bilen\Desktop\deneme_file.txt","r") as dosya:
#     veri = dosya.readlines()
#
# print(veri)

"""aa = "11/12/2019"
ab = aa.split("/")
ab.reverse()
ac = ""
for i in ab:
    ac += i
print(ac)"""

# abc = {123: "a", 124: "b", 125: "c"}
# def call(id):
# print(f'hi {}'.format(abc.get(id,"there")))
# call(125)

# a = 0xFF
# print(bin(int(str(a)[2:])))

# a = [[0,1,2],[3,4,5],[6,7,8]]
# print(a[1][1])

# a = "alphabet"
# b = ""
# print(b.join(sorted(a)))

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

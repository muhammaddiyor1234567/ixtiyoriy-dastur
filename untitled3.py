# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MJi2dTULt6OYafRWbwF8StrpOYEb-EPn
"""

def qoshish(a, b):
    return a + b


def ayirish(a, b):
    return a - b

def kopaytirish(a, b):
    return a * b


def bolish(a, b):
    if b == 0:
        return "0 ga bo'lish mumkin emas!"
    return a / b

print("Kalkulyator")
print("1. Qo'shish")
print("2. Ayirish")
print("3. Ko'paytirish")
print("4. Bo'lish")

tanlov = input("Tanlovni kiriting (1/2/3/4): ")

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

if tanlov == '1':
    print(f"{a} + {b} = {qoshish(a, b)}")
elif tanlov == '2':
    print(f"{a} - {b} = {ayirish(a, b)}")
elif tanlov == '3':
    print(f"{a} * {b} = {kopaytirish(a, b)}")
elif tanlov == '4':
    print(f"{a} / {b} = {bolish(a, b)}")
else:
    print("Noto'g'ri tanlov!")
a = input()

try:
    a = int(a)
    div = 1/a
    print(div)
except ZeroDivisionError:
    print("le denom doit etre diff de 0")
finally:
    print("execution oblg")

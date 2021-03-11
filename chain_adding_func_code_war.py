
# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python

class Func(int):
    def __call__(self,v):
        return Func(self+v)

def add(n):
    return Func(n)
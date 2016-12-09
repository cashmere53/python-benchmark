# -*- coding: utf-8 -*-
import typing

class Social():
    def __init__(self, n1: int, n2: int) -> None:
        self.num1 = n1
        self.num2 = n2

    def plus(self):
        return self.num1 + self.num2

def main():
    social = Social(5, 3)
    print(social.plus())
    social = Social("4", 4)
    print(social.plus())

if __name__ == '__main__':
    main()

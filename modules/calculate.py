#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from operator import add, sub, mul, truediv
from operator import pow as power


operators = {
    "+": add,
    "-": sub,
    "×": mul,
    "÷": truediv,
    "^": power
}


def calculate(s):
    if s.isdigit():
        return float(s)
    else:
        for op in operators:
            left, operator, right = s.partition(op)
            if operator in operators:
                return operators[operator](calculate(left), calculate(right))

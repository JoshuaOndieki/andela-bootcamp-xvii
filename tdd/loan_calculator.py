#!/usr/bin/env python
# encoding: utf-8


def loan_calculator(amount, rate, time):
    if amount<0:
        return "Invalid amount!"
    if rate>100:
        return "Invalid rate!"
    if time>12:
        return "Invalid Number of months!"
    return amount + (amount*(rate/100)*time)

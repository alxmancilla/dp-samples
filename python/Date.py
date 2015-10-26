#!c:/Python34/python.exe -u
# -*- coding: utf-8 -*-

class Date:
    """A class to represent a date - uses 1/1/2015 for default"""
    def __init__(self, day=1, month=1, year = 2015):
        self.day = day
        self.month = month
        self.year = year
    def __str__(self):
        return "toString: {:d}/{:d}/{:d}".format(self.day, self.month, self.year)

    def print_date(self):   
        print("print_date: {:d}/{:d}/{:d}".format(self.day, self.month, self.year))

#main routine
if __name__=='__main__':
    d1 = Date() # uses default
    d1.print_date()
    d2 = Date(year=2014) # doesn't use default year
    print(d2)
    d3 = Date(month=10, day=20)
    print(d3)

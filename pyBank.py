#this is the python challenge homework

import os
import csv
import numpy as np
#load csv file into memory
csvpath = os.path.join('Resources', 'budget_data.csv')
#list of all the data stores that will be compiled for this financil analysis
arrpnl = []
tmp_dates = []
tmp_months = []
tmp_profits = []
tmp_change = []
tmp_max = []
tmp_min = []
#open and read csv file thru csv.reader method
with open(csvpath, newline = '') as csvfile:
    linereader = csv.reader(csvfile, delimiter = ',')
    for row in linereader:
        #add dates to dates array
        tmp_dates.append(row[0])
        #add months to tmp array
        arrpnl.append(row[1])
        # print(arrpnl)

#function to split loss and profits in the months array
def pnlParser(arr):
    if (len(arr) == 0 ):
        return;
    arrpnl.sort()

    for i in range(len( arr)):
        tmp = []
        print(int(-tmp[i]), " ", int(tmp[i]), end = " ")

    if __name__ == "__main__":
        arrpnl = []
        # n = len(arrpnl)
        pnlParser(arr)


#confirm by printing output to the console
    # print(linereader)
    # line_header = next(linereader)
    # print(f"CSV Header:  {line_header}")
    # for row in linereader:
    #     print(row)
        # arr = []
        # date = row[0]
        # pnl = int(row[1])

pnlParser(arrpnl)

#iterate through the list









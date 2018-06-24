import csv
import sys
from datetime import datetime

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))
file = open('All_Sharepoint_Data.csv')
file2 = open('USCredit_monthly.csv')
reader = csv.reader(file)
reader2 = csv.reader(file2)
daterow = []
dt=next(reader2)
dt.pop(0)
for d in dt:
    daterow.append(datetime.strptime(d, '%m/%d/%Y').date())
daterow.pop(0)
file2.close()
#print daterow
example=csv.writer(open('Integrated1.csv', 'wb'), delimiter=',')
example.writerow(['TICKER','ASOFDATE','ASOFPRICE','3MONTHS','6MONTH','12MONTH'])
next(reader)
for row in reader:
    file2 = open('USCredit_monthly.csv')
    reader2 = csv.reader(file2)
    next(reader2)
    date = datetime.strptime(row[2], '%m/%d/%Y %H:%M').date()
    closest = nearest(daterow, date)
    for prices in reader2:
        if(row[0] == prices[0]):
            list = []
            list.append(row[0])
            list.append(date.strftime('%m/%d/%Y'))
            list.append(prices[daterow.index(closest)+2])
            if(len(daterow) - (daterow.index(closest)+2) >= 2):
                list.append(prices[daterow.index(closest)+5])
            if(len(daterow) - (daterow.index(closest)+2) >= 5):
                list.append(prices[daterow.index(closest)+8])
            if(len(daterow) - (daterow.index(closest)+2) >= 11):
                list.append(prices[daterow.index(closest)+14])
            example.writerow(list)
    file2.close()
    #print list

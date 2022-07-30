from multiprocessing.sharedctypes import Value
from optparse import Values
import vacations_calendar

def check(date_str):
    d_ch = date_str
    date_check=d_ch[:5]
    print(date_check)
    for keys, values in vacations_calendar.calendar.items():
        if date_check == values:
            return print(keys)
        else: exit
    print('None')
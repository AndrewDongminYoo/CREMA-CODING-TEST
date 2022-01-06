#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'preprocessDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#

def preprocess_date(date_list):
    month_list = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    day_regex = re.compile(r"\d{1,2}")
    year_regex = re.compile(r"\d{4}")
    result_list = []
    for date in date_list:
        temp_list = date.split(" ")
        day = day_regex.search(temp_list[0]).group()
        month = str(month_list.index(temp_list[1]))
        year = year_regex.search(temp_list[2]).group()
        new_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        result_list.append(new_date)
    return result_list


if __name__ == '__main__':
    dates = ["20th Oct 2052", "6th Jun 1933", "26th May 1960", "20th Sep 1958", "16th Mar 2068", "25th May 1912",
             "16th Dec 2018", "6th Jun 1933", "26th Dec 2061", "4th Nov 2030", "28th Jul 1963"]
    result = preprocess_date(dates)
    print('\n'.join(result))

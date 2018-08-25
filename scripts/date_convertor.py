##############################################################################################################
# Gregorian & Jalali ( Hijri_Shamsi , Solar ) Date Converter Functions
# Author: JDF.SCR.IR =>> Download Full Version : http://jdf.scr.ir/jdf
# License: GNU/LGPL _ Open Source & Free _ Version: 2.72 : [2017=1396]
# --------------------------------------------------------------------
# 1461 = 365*4 + 4/4   &  146097 = 365*400 + 400/4 - 400/100 + 400/400
# 12053 = 365*33 + 32/4      &       36524 = 365*100 + 100/4 - 100/100

def gregorian_to_jalali(gy,gm,gd):
    g_d_m=[0,31,59,90,120,151,181,212,243,273,304,334]

    if(gy>1600):
        jy=979
        gy-=1600
    else:
        jy=0
        gy-=621

    if(gm>2):
        gy2=gy+1
    else:
        gy2=gy

    days=(365*gy) +(int((gy2+3)/4)) -(int((gy2+99)/100)) +(int((gy2+399)/400)) -80 +gd +g_d_m[gm-1]
    jy+=33*(int(days/12053))
    days%=12053
    jy+=4*(int(days/1461))
    days%=1461

    if(days > 365):
        jy+=int((days-1)/365)
        days=(days-1)%365

    if(days < 186):
        jm=1+int(days/31)
        jd=1+(days%31)
    else:
        jm=7+int((days-186)/30)
        jd=1+((days-186)%30)
    return [jy,jm,jd]


def jalali_to_gregorian(jy,jm,jd):
    if(jy>979):
        gy=1600
        jy-=979
    else:
        gy=621

    if(jm<7):
        days=(jm-1)*31
    else:
        days=((jm-7)*30)+186

    days+=(365*jy) +((int(jy/33))*8) +(int(((jy%33)+3)/4)) +78 +jd
    gy+=400*(int(days/146097))
    days%=146097

    if(days > 36524):
        gy+=100*(int(days/36524))
        days%=36524
        if(days >= 365):
            days+=1

    gy+=4*(int(days/1461))
    days%=1461

    if(days > 365):
        gy+=int((days-1)/365)
        days=(days-1)%365

    gd=days+1
    if((gy%4==0 and gy%100!=0) or (gy%400==0)):
        kab=29
    else:
        kab=28

    sal_a=[0,31,kab,31,30,31,30,31,31,30,31,30,31]
    gm=0

    while(gm<13):
        v=sal_a[gm]
        if(gd <= v):
            break
        gd-=v
        gm+=1
    return [gy,gm,gd]
####################################################################
# Test
# 2017/12/09 -> 1396/09/18
assert (gregorian_to_jalali( 2017, 12, 9 ) == [1396,9,18]), "Date Converter is Invalid"
assert (gregorian_to_jalali( 2009, 5, 5 ) == [1388,2,15]), "Date Converter is Invalid"
import pandas as pd
data = pd.read_csv('iran total market index.csv')
print(data[1])
import pandas as pd
import numpy as np
labels = ['dates' , 'price']
data = pd.read_csv('iran total market index.csv' , header = 0, names = labels )
dates = data['dates']
def base_ten(x) : 
    value = 1000 * x[3] + 100 * x[2] + 10 * x[1] + x[0]
    return value
for i in range(len(dates)):
    year_digits = []
    month_digits = []
    day_digits = []
    seper = list(iter(dates[i]))
    counter = 0
    i = 0
    while i < len(seper) : 
        if seper[i] == '/' :
            counter == counter + 1
            continue 
        elif counter == 0 :
            year_digits.append(int(seper[i]))
        elif counter == 1 :
            month_digits.append(int(seper[i]))
        elif counter == 2 :
            month_digits.append(int(seper[i]))
    for i in range(4 - len(month_digits)):
        month_digits.append(0)
    for i in range(4 - len(day_digits)):
        day_digits.append(0)
    year = base_ten(year_digits)
    month = base_ten(month_digits)
    day = base_ten(day_digits)
    dates[i] =  jalali_to_gregorian(year , month , day)
    i = i + 1
print(dates)
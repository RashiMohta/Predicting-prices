import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate

input3=pd.read_csv("Q1_Data.csv", usecols=["Price"])
input2=pd.read_csv("Q1_Data.csv", usecols=["Date"])
input2=input2.values.tolist()
input3=input3.values.tolist()
#month=[0,30,31, 31, 28, 31, 30, 31, 30, 31, 31, 30]
month=[0, 30, 61, 92, 120, 151, 181, 212, 242, 273, 304, 334]
days=[]
#to find the number of days between that date and 31st October 2020. 
for i in range(48):
	word=str(input2[i])
	word=word.replace("]",'')
	word=word.replace("[",'')
	word=word.replace("'",'')
	string=word.split('/')
	x=int(string[0])
	if(x<10): 
		x+=12
	day=365*(int(string[2])-2020) + month[x-10] 
	if(int(string[0])<10):
		day=day-365
	#print(day)
	days.append(day)
	
#group 1 at 31/5
#group 2 at 31/8
#group 3 at 30/9
#group 4 at 31/1
#we now make 4 different functions to find the anchor points in the next year and append those points in our arrays of days and the corresponding price(input3)
#grp4_x=["1/31/2021","1/31/2022","1/31/2023","1/31/2024"]
grp4_x=[92,92+365,92+365*2,92+365*3]
grp4_y=[602.3552461, 599.4953259, 586.1306276, 568.059106]
grp4_f=interpolate.interp1d(np.array(grp4_x), np.array(grp4_y), fill_value="extrapolate" )	
days.append(92+365*4)
input3.append([grp4_f(92+365*4)])

#grp1_x=["5/31/2020" '"5/31/2021","5/31/2022","5/31/2023"]
grp1_x=[212,212+365,212+365*2,212+365*3]
grp1_y=[545.8955607, 535.4571412, 526.2513983, 524.9593148]
grp1_f=interpolate.interp1d(np.array(grp1_x), np.array(grp1_y), fill_value="extrapolate" )	
days.append(int(212+365*4))
input3.append([float(grp1_f(212+365*4))])

#grp2_x=["8/31/2020","8/31/2021","8/31/2022","8/31/2023"]
grp2_x=[304,304+365,304+365*2,304+365*3]
grp2_y=[570.4807853, 557.592587, 539.9380749, 535.1171913]
grp2_f=interpolate.interp1d(np.array(grp2_x), np.array(grp2_y), fill_value="extrapolate" )	
days.append(304+365*4)
input3.append([grp2_f(304+365*4)])

#grp3_x=["9/30/2021","9/30/2022","9/30/2023","9/30/2024"]
grp3_x=[334,334+365,334+365*2,334+365*3]
grp3_y=[562.4648076, 554.9134965, 537.456283, 534.1692775]
grp3_f=interpolate.interp1d(np.array(grp3_x), np.array(grp3_y).squeeze(), fill_value="extrapolate" )	
days.append(334+365*4)
input3.append([grp3_f(334+365*4)])

f=interpolate.interp1d(np.array(days), np.array(input3).squeeze(), fill_value="extrapolate" )	
xax=[]
yax=[]
#plotting the graph for all days upto 30th September 2025
for i in range(1794):
	xax.append(i)
	yax.append(f(i))
plt.scatter(xax,yax)
plt.plot(xax,yax)
plt.show() 


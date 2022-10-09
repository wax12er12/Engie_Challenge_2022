from cmath import pi
import pandas as pd
import matplotlib.pyplot as plt


ST = pd.read_csv("Dorm Buildings.csv")#reading the data file
SM = pd.read_csv("Weather Data.csv")

TTEC= ST['Taylor Tower - Total Energy Consumption (Cleaned) (kBTU)'].to_list()

weeklyEC = []
count = 0
sum = 0
for i in range(len(TTEC)):
    sum += TTEC[i]
    count += 1
    
    if (count == 168):
        weeklyEC.append(sum/(168))
        sum, count = 0, 0
TTocc= ST["Taylor Tower - Occupancy (DEV)"].to_list()

ATTocc=[]
for i in range(len(TTocc)):
    sum += TTocc[i]
    count += 1
    
    if (count == 168):
        ATTocc.append(sum/(168))
        sum, count = 0, 0
TTlastweek=weeklyEC[-1]/ ATTocc[-1]

SSocc= ST["Smith-Steeb Hall - Occupancy (DEV)"].to_list()
SSEC=ST["Smith-Steeb Hall - Total Energy Consumption (Cleaned) (kBTU)"].to_list()

SSweeklyEC = []
count = 0
sum = 0
for i in range(len(SSEC)):
    sum += TTEC[i]
    count += 1
    
    if (count == 168):
        SSweeklyEC.append(sum/(168))
        sum, count = 0, 0

SSocc=[]
count = 0
sum = 0
for i in range(len(SSEC)):
    sum += SSEC[i]
    count += 1
    
    if (count == 168):
        SSocc.append(sum/(168))
        sum, count = 0, 0
        
SSlastweek= SSweeklyEC[-1]/SSocc[-1]

TTdifference=((TTlastweek- SSlastweek)/(TTlastweek))*100
print(TTdifference)
SSdifference=((SSlastweek- TTlastweek)/(SSlastweek))*100
print(SSdifference)
# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data,new_record))

print(census.shape)
print(data.shape)

age=census[0:,0]
max_age= age.max()
min_age= age.min()
age_mean= age.mean()
age_std= age.std()

print(max_age,min_age,age_mean,age_std)

race_0 = list(filter(lambda x: x==0,census[0:,2]))
race_1 = list(filter(lambda x: x==1,census[0:,2]))
race_2 = list(filter(lambda x: x==2,census[0:,2]))
race_3 = list(filter(lambda x: x==3,census[0:,2]))
race_4 = list(filter(lambda x: x==4,census[0:,2]))

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

mini = min([len_0,len_1,len_2,len_3,len_4])
if(mini==len_0):
    minority_race=0
if(mini==len_1):
    minority_race=1
if(mini==len_2):
    minority_race=2
if(mini==len_3):
    minority_race=3
if(mini==len_4):
    minority_race=4

print(minority_race)

senior_citizens= list(filter(lambda x: x>60,census[0:,0]))
working_hours_sum = 0
for i in range(0,len(census)):
    if(census[i,0] in senior_citizens):
        working_hours_sum+=  census[i,6]
senior_citizens_len= len(senior_citizens)   
avg_working_hours= working_hours_sum/senior_citizens_len
print(avg_working_hours)
if(avg_working_hours>=25):
    print("Government policy is not followed")
else:
    print("Government policy is followed")

high=list(filter(lambda x: x>10,census[0:,1]))
low=list(filter(lambda x: x<=10,census[0:,1]))
temp=[]
for i in range(0,len(census)):
    if(census[i,1] in high):
        temp.append(census[i,7])
avg_pay_high= np.mean(temp)
temp=[]
for i in range(0,len(census)):
    if(census[i,1] in low):
        temp.append(census[i,7])
avg_pay_low = np.mean(temp)
if(avg_pay_low>avg_pay_high):
    print("No, there is no truth in better education leads to better pay ")
else:
    print("yes, there is truth in better education leads to better pay ") 







import csv


with open("data.csv",newline="") as f:
    reader= csv.reader(f)
    file_data= list(reader)
#print(file_data)
data= file_data[0]
#print(data)

numbers = 0
numberofnumbers = len(data)
for sum in data:
    numbers = numbers+ float(sum[1])

mean= numbers / numberofnumbers
#print("mean is: "+ str(mean))

import math 

diffrence= []
for dif in data:
    a = int(dif) - mean
    a= a**2
    diffrence.append(a)

#print("difference of each number by the mean and squared is: " + str(diffrence))

sum=0
for i in diffrence:
    sum= sum+i
#print(sum)

result= sum/ (len(data)-1)
#print(result)

standard_deviation= math.sqrt(result)
print("standard deviation is:" + str(standard_deviation))












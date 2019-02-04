import matplotlib.pylab as plt
import numpy as np


## Get analyzing data
f = open('input', 'r')
input_data = f.read()

input_data = input_data.splitlines()

for i in range(0, len(input_data)):
	input_data[i] = float(input_data[i])

sum_of_xy = 0
sum_of_x = 0
sum_of_y = 0
sum_of_x2 = 0

for i in range(0, len(input_data)):
	sum_of_xy = sum_of_xy + i * input_data[i]
	sum_of_x = sum_of_x + i
	sum_of_y = sum_of_y + input_data[i]
	sum_of_x2 = sum_of_x2 + i**2

a = (len(input_data) * sum_of_xy - sum_of_x * sum_of_y) / (len(input_data) * sum_of_x2 - sum_of_x**2)
b = (sum_of_y - a * sum_of_x) / len(input_data)

def prediction(x):
	return a * x + b

f.close()

#get full data
f = open('expected', 'r')
full_data = f.read()
full_data = full_data.splitlines()
for i in range(0, len(full_data)):
	full_data[i] = float(full_data[i])

#Plotting the data
plt.plot(np.arange(len(input_data)), input_data, 'ro')
plt.plot(len(input_data) + 1, full_data, 'ro', color='k')
plt.plot(np.arange(len(input_data) + 2), prediction(np.arange(len(input_data) + 2)))
plt.xlabel('Number of month')
plt.ylabel('stock index')
plt.title('Facebook\'s stock data on year 2018 and prediction for January of 2019')
plt.grid(True)
plt.show()

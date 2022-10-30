import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
#matplotlib.use('Agg')

threads = ["sequential", "1", "2", "4", "8", "16", "32", "64"]
index = 1
data = {}

#  read sequential ------------
fp = open("seq/run_kmeans.out")
line = fp.readline()
while line:
    if("total = " in line):
        time_line = line.split("total = ")[1]
        time = time_line[:7]
        print(time)
        data["sequential"] = float(time)
        break
fp.close() 


#  read & plot WITH affinity ------------
fp = open("with_aff_8ppn/run_kmeans.out")
line = fp.readline()

while line:
    if("total = " in line):
        time_line = line.split("total = ")[1]
        time = time_line[:7]
        print(time)
        data[threads[index]] = float(time)
        index+=1
    line = fp.readline()
fp.close() 

values = list(data.values())
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
bar_with_aff = plt.bar(np.arange(len(threads)), values, color ='green',
        width =0.2)

#  read & plot WITHOUT affinity ------------
index = 1

fp = open("without_aff/run_kmeans.out")
line = fp.readline()

while line:
    if("total = " in line):
        time_line = line.split("total = ")[1]
        time = time_line[:7]
        print(time)
        data[threads[index]] = float(time)
        index+=1
    line = fp.readline()

fp.close() 

values_no_aff = list(data.values())
bar_without_aff = plt.bar(np.arange(len(threads))+0.2, values_no_aff, color ='blue',
        width =0.2)

plt.legend( (bar_with_aff, bar_without_aff), ('affinity', 'no affinity') )

plt.xticks(np.arange(len(threads)) + 0.1, threads)
plt.xlabel("Number of Threads")
plt.ylabel("Time (in sec)")
plt.title("K-means")
plt.show()



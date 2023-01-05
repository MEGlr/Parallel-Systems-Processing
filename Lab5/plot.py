import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
#matplotlib.use('Agg')

block_size = ["32", "64", "128", "256", "512", "1024"]
versions = ["Naive version", "Transpose version", "Shared version"]
def plot_time_speedup():
    fp = open("Sz-256_Coo-2_Cl-16_with_val.csv")
    data_time = {}
    data_speedup = {}
    fp.readline()  #ignore headers
    line = fp.readline()   
    seq_time = float(line.split(",")[2])  #TODO

    for version in versions:
        index = 0
        while index < len(block_size):
            size = block_size[index]
            line = fp.readline()  
            if("Sequential" not in line):
                time = line.split(",")[2]  #TODO
                data_speedup[size] = seq_time/float(time)
                data_time[size] = float(time)
                # print(time)
                # print(index)
                index+=1

        values_time = list(data_time.values())
        values_speedup = list(data_speedup.values())
        print("values", values_time)
        fig = plt.figure(figsize = (10, 5))
        plt.title("K-means - " + version + " (time plot)")
        bar_time = plt.bar(np.arange(len(block_size)+1), [seq_time] + values_time, color ='green',
            width =0.2)
        plt.xlabel("block size")
        plt.ylabel("time (in sec)")
        plt.xticks(np.arange(len(block_size)+1) , ["sequential"]+block_size)
        plt.savefig(version+"_time", bbox_inches="tight")

        fig = plt.figure(figsize = (10, 5))
        plt.title("K-means - " + version + " (speedup plot)")
        bar_time = plt.bar(np.arange(len(block_size)+1), [seq_time] + values_speedup, color ='green',
            width = 0.2)
        plt.xlabel("block size")
        plt.ylabel("speedup")
        plt.xticks(np.arange(len(block_size)+1) , ["sequential"]+block_size)
        plt.savefig(version+"_speedup", bbox_inches="tight")

    fp.close() 
        
plot_time_speedup()
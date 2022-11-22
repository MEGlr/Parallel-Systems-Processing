import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
#matplotlib.use('Agg')

threads = ["1", "2", "4", "8", "16", "32", "64"]
fp = open("./run_kmeans_locks.out")
line = fp.readline()

def plot_time_speedup():
    locks = ["nosync","pthread-mutex", "pthread-spinlock", "tas", "ttas", "array-based" ]
    for lock in locks:
        index = 0
        data_time = {}
        data_speedup = {}
        line = fp.readline()
        print(lock)
        while index < 7:
            if("total = " in line):
                time_line = line.split("total = ")[1]
                time = time_line[:7]
                #data_speedup[threads[index]] = seq_time/float(time)
                data_time[threads[index]] = float(time)
                print(time)
                print(index)
                index+=1
            line = fp.readline()
        values_time = list(data_time.values())
        print(values_time)
        fig = plt.figure(figsize = (10, 5))
        plt.title(str(lock))
        bar1_speedup = plt.bar(np.arange(len(threads)), values_time, color ='green',
            width =0.2)
        plt.savefig(str(lock)+"_time", bbox_inches="tight")
    fp.close() 
        
        #values_speedup = list(data_speedup.values())
        
        
        #plt.show()
        

plot_time_speedup()
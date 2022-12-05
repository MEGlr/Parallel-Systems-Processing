import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
#matplotlib.use('Agg')

threads = ["1", "2", "4", "8", "16", "32", "64", "128"]
workload = ["100_0_0", "80_10_10", "20_40_40", "0_50_50"]
list_size = ["1024", "8192"]
implementation = ["serial","Coarse-grain locking","Fine-grain locking","Optimistic synchronization","Lazy synchronization","Non-blocking synchronization"]
throughput = {}
#read serial
fp = open("./run_conc_ll_serial.out")
line = fp.readline()

for size_ in list_size:
    throughput[size_] = {}
    for wl in workload:
        while "Nthreads" not in line:
            line = fp.readline()
        throu = line.split("Throughput(Kops/sec): ")[1]
        throughput[size_][wl] = {}
        throughput[size_][wl]["serial"] =  float(throu)
        line = fp.readline()
print(throughput)

throughputF = {}    
for size_ in list_size:
    throughputF[size_]= {}
    for wl in workload:
        throughputF[size_][wl] = {}
        throughputF[size_][wl]["serial"] = {}
        for thread in threads:    
            throughputF[size_][wl]["serial"][thread] = throughput[size_][wl]["serial"] 
for impl in implementation[1:]:
    for thread in threads:
        for size_ in list_size:
            for wl in workload:
                throughputF[size_][wl][impl] ={}

fp = open("./run_conc_ll.out")
line = fp.readline()
for impl in implementation[1:]:
    for thread in threads:
        for size_ in list_size:
            for wl in workload:
                while "Nthreads" not in line:
                    line = fp.readline()
                throu = line.split("Throughput(Kops/sec): ")[1]
                throughputF[size_][wl][impl][thread] =  float(throu)
                line = fp.readline()
print(throughputF["1024"]["0_50_50"])  

def plot_one(input_, name, title):
    fig = plt.figure(figsize = (10, 5))
    colors= ["#588c7e", "#96ceb4" ,"#b5e7a0","#86af49", "#e3eaa7",  "green","mediumaquamarine", "teal"]
    legend_ = []
    for index, lock in enumerate(implementation):
        values_time = list(input_[lock].values())
        legend_.append(plt.bar(np.arange(len(threads)) -0.2+index*0.1 , values_time, color =colors[index],
        width =0.1))
    plt.xticks(np.arange(len(threads)) , threads)
    plt.xlabel("Number of Threads")
    plt.ylabel("throughput (Kops/sec)")
    plt.title(f"{title} : throughput per implementation")
    plt.legend((legend_[0], legend_[1], legend_[2], legend_[3], legend_[4], legend_[5]), ("serial","Coarse-grain locking","Fine-grain locking","Optimistic synchronization","Lazy synchronization","Non-blocking synchronization"))
    plt.savefig(f"plot_throughput{name}", bbox_inches="tight")

for size_ in list_size:
            for wl in workload:
                    input_ = throughputF[size_][wl]
                    plot_one(input_, f"_{size_}_{wl}", f"size: {size_}, workload:{wl}")
# def plot_time_speedup():
#     throughputF = {}
#     for lock in implementation:
#         index = 0
#         throughputF[lock] = {}
#         data_speedup = {}
#         line = fp.readline()
#         print(lock)
#         while index < 7:
#             if("total = " in line):
#                 time_line = line.split("total = ")[1]
#                 time = time_line[:7]
#                 #data_speedup[threads[index]] = seq_time/float(time)
#                 throughputF[lock][threads[index]] = float(time)
#                 print(time)
#                 print(index)
#                 index+=1
#             line = fp.readline()
#         values_time = list(throughputF[lock].values())
#         print(values_time)
#     fig = plt.figure(figsize = (10, 5))
#     colors= ["#588c7e", "#96ceb4" ,"#b5e7a0","#86af49", "#e3eaa7",  "green","mediumaquamarine", "teal"]
#     legend_ = []
#     for index, lock in enumerate(implementation):
#         values_time = list(throughputF[lock].values())
#         legend_.append(plt.bar(np.arange(len(threads)) -0.3+index*0.1 , values_time, color =colors[index],
#         width =0.1))
#     values_time = [0.8952, 1.8086, 3.0666, 4.4614, 6.8206, 6.8162, 6.006]
#     legend_.append(plt.bar(np.arange(len(threads)) -0.3+index*0.1+0.1 , values_time, color =colors[index+1],
#         width =0.1))
#     plt.xticks(np.arange(len(threads)) , threads)
#     plt.xlabel("Number of Threads")
#     plt.ylabel("time (in sec)")
#     plt.title("execution time per lock type")
#     plt.legend((legend_[0], legend_[1], legend_[2], legend_[3], legend_[4], legend_[5], legend_[6], legend_[7]), ("nosync","pthread-mutex", "pthread-spinlock", "tas", "ttas", "array-based", "clh-queue", "critical"))
#     plt.savefig("plot_time", bbox_inches="tight")
#     fp.close() 
        
#         #values_speedup = list(data_speedup.values())
        
        
#         #plt.show()
        

# plot_time_speedup()
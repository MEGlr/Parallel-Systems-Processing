import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

threads = ["sequential", "1", "2", "4", "8", "16", "32", "64"]
fp = open("sequential/run_kmeans.out")
line = fp.readline()
while line:
    if("total = " in line):
        time_line = line.split("total = ")[1]
        time = time_line[:7]
        seq_time = float(time)
    line = fp.readline()
fp.close() 

def plot_time_speedup(title_, input_loc1, input_loc2, output, legend1, legend2 ):
    
        #  read & plot 1 ------------
        index = 1
        data_time = {}
        data_speedup = {}
        fp = open(input_loc1)
        line = fp.readline()
        data_speedup["sequential"] = 1
        data_time["sequential"] = seq_time

        while line:
            if("total = " in line):
                time_line = line.split("total = ")[1]
                time = time_line[:7]
                data_speedup[threads[index]] = seq_time/float(time)
                data_time[threads[index]] = float(time)
                index+=1
            line = fp.readline()

        fp.close() 
        fig = plt.figure(figsize = (10, 5))
        values_speedup = list(data_speedup.values())
        values_time = list(data_time.values())
        print(values_time)
        bar1_speedup = plt.bar(np.arange(len(threads)), values_speedup, color ='green',
                width =0.2)
        
        
        #  read & plot 2 ------------
        index = 1
        if input_loc2 != "":
                fp = open(input_loc2)
                line = fp.readline()
                while line:
                    if("total = " in line):
                        time_line = line.split("total = ")[1]
                        time = time_line[:7]
                        print(time)
                        data_speedup[threads[index]] = seq_time/float(time)
                        data_time[threads[index]] = float(time)
                        index+=1
                    line = fp.readline()

                fp.close() 

                values_speedup2 = list(data_speedup.values())
                values_time2 = list(data_time.values())
                bar2_speedup = plt.bar(np.arange(len(threads))+0.2, values_speedup2, color ='blue',
                        width =0.2)
                

        if input_loc2 == "":
            plt.legend(bar1_speedup, legend1)
            plt.xticks(np.arange(len(threads)) , threads)
        else:
            plt.legend( (bar1_speedup, bar2_speedup), (legend1, legend2) )
            plt.xticks(np.arange(len(threads)) + 0.1, threads)
       
        
        plt.xlabel("Number of Threads")
        plt.ylabel("speedup")
        plt.title(title_)
        plt.show()
        plt.savefig(output+"_speedup.png", bbox_inches="tight")
        print(values_time)
        
        fig = plt.figure(figsize = (10, 5))
        bar1_time = plt.bar(np.arange(len(threads)), values_time, color ='green',
                        width =0.2)
                        
        if input_loc2 == "":
            plt.legend(bar1_time, legend1)
            plt.xticks(np.arange(len(threads)), threads)
        else:
            bar2_time = plt.bar(np.arange(len(threads))+0.2, values_time2, color ='blue',
                        width =0.2)
            plt.legend( (bar1_time, bar2_time), (legend1, legend2) )
            plt.xticks(np.arange(len(threads)) + 0.1, threads)
        
        plt.xlabel("Number of Threads")
        plt.ylabel("time (in sec)")
        plt.title(title_)
        plt.show()
        plt.savefig(output+"_time.png", bbox_inches="tight")


plot_time_speedup("k-means (naive parallel)","kmeans_shared_affinity/run_kmeans.out", "kmeans_shared/run_kmeans.out" ,"plots/k_means_naive.png", "affinity", "no affinity" )

plot_time_speedup("k-means - reduction  (i)","kmeans_reduction_i_without_parallelism/run_kmeans_reduction.out", "" ,"plots/k_means_reduction_i.png", "", "" )

plot_time_speedup("k-means - reduction  (ii) \n Coords = 1, Clusters = 4","kmeans_reduction_ii_init_parallel_inside_while_1_4/run_kmeans_reduction.out", "" ,"plots/k_means_reduction_ii_1_4.png", "", "" )

plot_time_speedup("k-means - reduction  (ii) \n Coords = 1, Clusters = 4 - calloc","kmeans_reduction_ii_parallel_calloc_1_4/run_kmeans_reduction.out", "" ,"plots/k_means_reduction_ii_calloc_1_4.png", "", "" )

plot_time_speedup("k-means - reduction  (ii) \n Coords = 16, Clusters = 16","kmeans_reduction_ii_init_parallel_inside_while_16_16/run_kmeans_reduction.out", "" ,"plots/k_means_reduction_ii_16_16.png", "", "" )

plot_time_speedup("k-means - reduction  (ii) \n Coords = 16, Clusters = 16 - calloc","kmeans_reduction_ii_parallel_calloc_16_16/run_kmeans_reduction.out", "" ,"plots/k_means_reduction_ii_calloc_16_16.png", "", "" )

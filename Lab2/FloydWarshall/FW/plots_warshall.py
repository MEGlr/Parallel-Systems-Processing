import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

threads = ["sequential", "1", "2", "4", "8", "16", "32", "64"]
#fp = open("sequential/run_fw.out")
# line = fp.readline()
# while line:
#     if("total = " in line):
#         time_line = line.split("total = ")[1]
#         time = time_line[:7]
#         seq_time = float(time)
#     line = fp.readline()
# fp.close() 
seq_time = float(13)
def plot_time_speedup(title_, input_loc1,output):
    
        #  read & plot 1 ------------
        index = 1
        fp = open(input_loc1+"/run_fw.out")
        line = fp.readline()
        table_block = {}
        for table_size in [1024, 2048, 4096]: 
                for block_size in [16, 32, 64, 256]:
                    table_block["table size = "+str(table_size)+", block size = "+str(block_size)] = {"sequential":seq_time}
        for thread_ in ["1", "2", "4", "8", "16", "32", "64"]:
             for block_size in [16, 32, 64, 256]:
                for table_size in [1024, 2048, 4096]:
                    if("FW_TILED" in line):
                        time = float(line.split(",")[-1])
                        index+=1
                        print(thread_)
                        print("table size = "+str(table_size)+", block size = "+str(block_size)) 
                        table_block["table size = "+str(table_size)+", block size = "+str(block_size)][thread_] = time
                        print(table_block["table size = "+str(table_size)+", block size = "+str(block_size)][thread_])
                    line = fp.readline()     
        fp.close() 

        for table_size in [1024, 2048, 4096]: 
                for block_size in [16, 32, 64, 256]:
                    plt.figure()
                    data_time = table_block["table size = "+str(table_size)+", block size = "+str(block_size)]
                    print(data_time)
                    values_time = list(data_time.values())
                    plt.bar(np.arange(len(threads)), values_time, color ='green', width =0.2)
                    plt.xticks(np.arange(len(threads)) , threads)
                    plt.xlabel("Number of Threads")
                    plt.ylabel("time(sec)")
                    plt.title(title_+"\ntable size = "+str(table_size)+", block size = "+str(block_size))
                    plt.show()
                    plt.savefig(output+title_+"_"+str(table_size)+"_"+str(block_size)+"_time", bbox_inches="tight")
       
plot_time_speedup("Floyd-Warshall (recursive)",".", "plots/")

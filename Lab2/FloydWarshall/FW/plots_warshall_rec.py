import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

threads = ["sequential", "1", "2", "4", "8", "16", "32", "64"]

seq_time = {"1024":1.3720, "2048":11.3550,"4096":96.1754}
def plot_time_speedup(title_, input_loc1,output):
        table_block = {}
        fp = open("run_fw_rec_seq.out")
        for table_size in [1024, 2048, 4096]: 
                table_block["table size = "+str(table_size)] = {}
        #line = fp.readline() 
        for block_size in [16, 32, 64, 124, 256]:
                for table_size in [1024, 2048, 4096]:    
         #           seq_time = float(line.split(",")[-1])
                    #if(table_size == 1024): 
                    print("time", seq_time, table_size)
                    table_block["table size = "+str(table_size)][str(block_size)] = {"sequential":seq_time[str(table_size)]}
          #          line = fp.readline()
        fp.close()
        fp = open(input_loc1+"/run_fw_rec.out")
        line = fp.readline()
        for thread_ in ["1", "2", "4", "8", "16", "32", "64"]:
             for block_size in [16, 32, 64, 124, 256]:
                for table_size in [1024, 2048, 4096]:
                        time = float(line.split(",")[-1])
                        table_block["table size = "+str(table_size)][str(block_size)][thread_] = time
                        line = fp.readline()     
        fp.close() 
        print(table_block)
        for table_size in [1024, 2048, 4096]: 
                plt.figure(figsize=(15,4))
                legend_ = []
                #["#034f84", "#b7d7e8", 
                colors= ["#588c7e", "#96ceb4" ,"#b5e7a0","#86af49", "#e3eaa7"]
                for i, block_size in enumerate([16, 32, 64, 124, 256]):    
                    data_time = table_block["table size = "+str(table_size)][str(block_size)] 
                    values_time = list(data_time.values())
                    print(block_size, values_time)
                    legend_.append(plt.bar(np.arange(len(threads))-0.2+i*0.1, values_time, color =colors[i], width =0.1))
                
                plt.legend((legend_[0], legend_[1], legend_[2], legend_[3], legend_[4]), ("16", "32", "64", "124", "256"))
                plt.xticks(np.arange(len(threads)) , threads)
                plt.xlabel("Number of Threads")
                plt.ylabel("time(sec)")
                plt.title(title_+"\ntable size = "+str(table_size))
                plt.show()
                plt.savefig(output+title_+"_"+str(table_size)+"_time", bbox_inches="tight")
       
plot_time_speedup("Floyd-Warshall (recursive)",".", "plots/")

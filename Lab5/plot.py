import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib
#matplotlib.use('Agg')
color = ["#588c7e", "#96ceb4" ,"#b5e7a0"]
block_size = ["32", "64", "128", "256", "512", "1024"]
versions = ["Naive version", "Transpose version", "Shared version"]
def plot_time_speedup(input_file, max_):
    fp = open(str(input_file))
    data_time = {}
    data_speedup = {}
    fp.readline()  #ignore headers
    line = fp.readline()   
    seq_time = float(line.split(",")[2])  #TODO
    coo_ = input_file.split("Coo-")[1]
    coo_ = coo_.split("_Cl")[0]
    fig, ax = plt.subplots(2, 1,figsize=(10, 8))
    for i, version in enumerate(versions[:max_]):
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
        offset = (i-int(max_/2)/2+int(max_/3)/2-int((max_-1)/2))*0.2
        ax[0].set_title("K-means - "  + f"coordinates = {coo_} (time plot)")
        bar_time = ax[0].bar(np.arange(len(block_size)+1)+offset, [seq_time] + values_time, color =color[i],
            width =0.2, label = version)


        
        ax[1].set_title("K-means - "  +f"coordinates = {coo_} (speedup plot)")
        bar_time = ax[1].bar(np.arange(len(block_size)+1)+offset, [1] + values_speedup, color =color[i],
            width = 0.2, label = version)
    
    ax[0].set_xlabel("block size")
    ax[0].set_ylabel("time (in sec)")
    ax[0].set_xticks(np.arange(len(block_size)+1) , ["sequential"]+block_size)
    

    ax[1].set_xlabel("block size")
    ax[1].set_ylabel("speedup")
    ax[1].set_xticks(np.arange(len(block_size)+1) , ["sequential"]+block_size)
    ax[0].legend()
    ax[1].legend()
    plt.tight_layout()
    plt.savefig("up_to_"+version+"_speedup"+f"_coo_{coo_}", bbox_inches="tight")
    plt.savefig("up_to_"+version+"_time"+f"_coo_{coo_}", bbox_inches="tight")

    fp.close() 
        
plot_time_speedup("Sz-256_Coo-2_Cl-16_with_val.csv", 1)
plot_time_speedup("Sz-256_Coo-2_Cl-16_with_val.csv", 2)
plot_time_speedup("Sz-256_Coo-2_Cl-16_with_val.csv", 3)

# plot_time_speedup("Sz-256_Coo-16_Cl-16.csv", 1)
# plot_time_speedup("Sz-256_Coo-16_Cl-16.csv", 2)
plot_time_speedup("Sz-256_Coo-16_Cl-16.csv", 3)


# temp = input_file.split("Sz-")[1]
# size_ = temp.split("Coo-")[0]

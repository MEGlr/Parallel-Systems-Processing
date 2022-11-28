# import matplotlib.pyplot as plt
# import sys
# import numpy as np
# import matplotlib
# #matplotlib.use('Agg')

# threads = ["1", "2", "4", "8", "16", "32", "64"]
# fp = open("./run_kmeans_locks.out")
# line = fp.readline()

# def plot_time_speedup():
#     locks = ["nosync","pthread-mutex", "pthread-spinlock", "tas", "ttas", "array-based", "clh-queue"]
#     data_time = {}
#     for lock in locks:
#         index = 0
#         data_time[lock] = {}
#         data_speedup = {}
#         line = fp.readline()
#         print(lock)
#         while index < 7:
#             if("total = " in line):
#                 time_line = line.split("total = ")[1]
#                 time = time_line[:7]
#                 #data_speedup[threads[index]] = seq_time/float(time)
#                 data_time[lock][threads[index]] = float(time)
#                 print(time)
#                 print(index)
#                 index+=1
#             line = fp.readline()
#         values_time = list(data_time[lock].values())
#         print(values_time)
#     fig = plt.figure(figsize = (10, 5))
#     colors= ["#588c7e", "#96ceb4" ,"#b5e7a0","#86af49", "#e3eaa7", "#588c7e", "#96ceb4" ,"#b5e7a0","#86af49"]
#     legend_ = []
#     for index, lock in enumerate(locks):
#         values_time = list(data_time[lock].values())
#         legend_.append(plt.bar(np.arange(len(threads)) -0.3+index*0.1 , values_time, color =colors[index],
#         width =0.1))
#     plt.xticks(np.arange(len(threads)) , threads)
    
#     plt.legend((legend_[0], legend_[1], legend_[2], legend_[3], legend_[4], legend_[5], legend_[6]), ("nosync","pthread-mutex", "pthread-spinlock", "tas", "ttas", "array-based", "clh-queue"))
#     plt.savefig("plot_time", bbox_inches="tight")
#     fp.close() 
        
#         #values_speedup = list(data_speedup.values())
        
        
#         #plt.show()
        

# plot_time_speedup()
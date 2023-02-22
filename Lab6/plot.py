import matplotlib.pyplot as plt
import numpy as np

## Jacobi Method
j2048 = {}
j2048['serial'] = 7.491788
j2048['parallel'] = [8.415402,4.324453,2.437425, 1.469033, 1.143714, 0.719666, 0.447212]
j2048['parallel_computation'] = [8.415301,4.217135, 2.112347, 1.058304, 0.798992, 0.307639 , 0.056788]


j4096 = {}
j4096['serial'] = 30.131113
j4096['parallel'] = [33.652385,
16.989755,
9.263372,
5.373293,
4.786425,
4.797003,
4.429228]

j4096['parallel_computation'] = [
33.652213,
16.841915,
8.431927,
4.302982,
3.690894,
3.582705,
3.276222

]

 

j6144 = {}
j6144['serial'] = 67.274402
j6144['parallel'] = [
75.650377, 
38.113721, 
20.600989, 
11.829779, 
10.650341, 
10.779092, 
10.701636
]
j6144['parallel_computation'] = [
75.650192, 
 37.903769, 
 18.970566, 
 9.698367 , 
 8.327327 , 
 8.266357 , 
 8.178860 
]


## Gauss Method
g2048 = {}
g2048['serial'] = 0.849018
g2048['parallel'] = [

9.509269,
9.703483,
5.132257,
2.814442,
1.931338,
1.104422,
0.707672

]

g2048['parallel_computation'] = [

9.508933,
4.752676,
2.378559,
1.189893,
0.825789,
0.355204,
0.154573
]
     

g4096 = {}
g4096['serial'] = 48.324781
g4096['parallel'] = [
38.000771,
38.280988,
19.938373,
10.699515,
7.931534 ,
5.637519 ,
4.479457 
]

g4096['parallel_computation'] = [
38.000296,       
19.002580,       
9.506541 ,       
4.792839 ,       
3.677409 ,       
2.279150 ,       
1.718522  
]

g6144 = {}
g6144['serial'] = 108.634645
g6144['parallel'] = [
85.573253,
85.926708,
44.524132,
23.766648,
17.622186,
12.801880,
10.749983
]
g6144['parallel_computation'] = [
 85.572803,         
 42.786803,         
 21.382064,         
 10.784257,         
 8.298901 ,         
 5.384795 ,         
 4.241378    
]


## Red-Black Method

 
r2048 = {}
r2048['serial'] = 13.380248
r2048['parallel'] = [
    18.601360 ,
9.522882 ,
5.031305 ,
2.772705 ,
1.981205 ,
1.105580, 
0.555231


]
r2048['parallel_computation'] = [
18.600564 ,
9.313108 ,
4.660311 ,
2.332955 ,
1.647357 ,
0.700053, 
0.130342 
]


r4096 = {}
r4096['serial'] =  53.699685
r4096['parallel'] = [
74.516325 ,
37.606842 ,
19.540683 ,
10.525260 ,
8.589728 ,
8.472278 ,
7.591635 

]
r4096['parallel_computation'] = [
74.515390 ,
37.344394 ,
18.642323 ,
9.395898 ,
7.426475 ,
7.116254 ,
6.213211 
]

r6144 = {}
r6144['serial'] = 120.120547
r6144['parallel'] = [

167.988526 ,
84.345990 ,
43.648183 ,
23.380349 ,
19.135194 ,
19.280779 ,
18.933333 
]
r6144['parallel_computation'] = [
167.987564 ,
83.993859 ,
41.937003 ,
21.129698 ,
16.735530 ,
16.593384 ,
16.243792 
]



def speedup_plot(size, j_list, g_list, r_list):
    jspeedup = []
    for i in range(7):
            jspeedup.append(j_list['serial']/j_list['parallel'][i])
    gspeedup = []
    for i in range(7):
            gspeedup.append(g_list['serial']/g_list['parallel'][i])
    rspeedup = []
    for i in range(7):
            rspeedup.append(r_list['serial']/r_list['parallel'][i])
    print(jspeedup)
    print(gspeedup)
    print(rspeedup)
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.set_xlabel("number of cores")
    ax.xaxis.set_ticks(np.arange(0, 7, 1))
    ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64'], rotation=45)
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylabel("speedup")
    plt.plot(jspeedup, label="Jacobi", color="green", marker='x')
    plt.plot(gspeedup, label="Gauss", color="blue", marker='*')
    plt.plot(rspeedup, label="RedBlack", color="red", marker='o')
    plt.title(f"Speedup Plot ({size}×{size} table)")
    plt.legend()
    plt.savefig(f"speedup_{size}.png", bbox_inches="tight")


speedup_plot(2048,j2048, g2048, r2048)
speedup_plot(4096,j4096, g4096, r4096)
speedup_plot(6144,j6144, g6144, r6144)


labels = ['Jacobi', 'Gauss', 'Red-Black']

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize = (15, 6))


a1 = [269.131002, 0.361636, 0.225310]
rects1 = ax.bar(x, a1, width/4, label="64 threads", color = "green")



a1 = [40.340626, 0.038081, 0.031633]
rects1 = ax.bar(x, a1, width/4, label="computation time", color = "grey")


#######################################################################
# Add some text for labels, title and custom x-axis tick labels, etc.
k = 1024
ax.set_ylabel(f'Time Plot (in secs) ({k}×{k} table)')
ax.set_title('Total & Computation Time')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.savefig("Total Time 1024.png", bbox_inches="tight")


labels = ['Gauss', 'Red-Black']

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize = (8, 6))


a1 = [0.361636, 0.225310]
rects1 = ax.bar(x, a1, width, label="64 threads", color = "green")



a1 = [ 0.038081, 0.031633]
rects1 = ax.bar(x, a1, width, label="computation time", color = "grey")


#######################################################################
# Add some text for labels, title and custom x-axis tick labels, etc.
k = 1024
ax.set_ylabel(f'Time Plot (in secs) ({k}×{k} table)')
ax.set_title('Total & Computation Time')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
fig.tight_layout()
plt.savefig("Total Time 1024_rest.png", bbox_inches="tight")



for k in 2048,4096,6144:
    
    if k == 2048:
        labels = ['Jacobi', 'Gauss', 'Red-Black']

        a1 = [j2048['parallel'][3], g2048['parallel'][3], r2048['parallel'][3]]
        a2 = [j2048['parallel'][4], g2048['parallel'][4], r2048['parallel'][4]]
        a3 = [j2048['parallel'][5], g2048['parallel'][5], r2048['parallel'][5]]
        a4 = [j2048['parallel'][6], g2048['parallel'][6], r2048['parallel'][6]]

        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars

        fig, ax = plt.subplots(figsize = (15, 6))
        
        rects1 = ax.bar(x - width, a1, width/4, label="8", color = "green")
        rects2 = ax.bar(x- width/2, a2, width/4, label="16", color = "orange")
        rects3 = ax.bar(x , a3, width/4, label="32", color = "black")
        rects4 = ax.bar(x+ width/2, a4, width/4, label="64", color = "blue")

        a1 = [j2048['parallel_computation'][3], g2048['parallel_computation'][3], r2048['parallel_computation'][3]]
        a2 = [j2048['parallel_computation'][4], g2048['parallel_computation'][4], r2048['parallel_computation'][4]]
        a3 = [j2048['parallel_computation'][5], g2048['parallel_computation'][5], r2048['parallel_computation'][5]]
        a4 = [j2048['parallel_computation'][6], g2048['parallel_computation'][6], r2048['parallel_computation'][6]]

        rects1 = ax.bar(x - width, a1, width/4, label="computation time", color = "grey")
        rects2 = ax.bar(x - width/2, a2, width/4, color = "grey")
        rects3 = ax.bar(x, a3, width/4, color = "grey")
        rects4 = ax.bar(x + width/2, a4, width/4,  color = "grey")
        

        #######################################################################
        # Add some text for labels, title and custom x-axis tick labels, etc.

        ax.set_ylabel(f'Time Plot (in secs) ({k}×{k} table)')
        ax.set_title('Total & Computation Time')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        plt.savefig("Total Time 2048.png", bbox_inches="tight")


    if k == 4096:

        labels = ['Jacobi', 'Gauss', 'Red-Black']

        a1 = [j4096['parallel'][3], g4096['parallel'][3], r4096['parallel'][3]]
        a2 = [j4096['parallel'][4], g4096['parallel'][4], r4096['parallel'][4]]
        a3 = [j4096['parallel'][5], g4096['parallel'][5], r4096['parallel'][5]]
        a4 = [j4096['parallel'][6], g4096['parallel'][6], r4096['parallel'][6]]

        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars
        fig, ax = plt.subplots(figsize = (15, 6))

        rects1 = ax.bar(x - width, a1, width/4, label="8", color = "green")
        rects2 = ax.bar(x- width/2, a2, width/4, label="16", color = "orange")
        rects3 = ax.bar(x , a3, width/4, label="32", color = "black")
        rects4 = ax.bar(x+ width/2, a4, width/4, label="64", color = "blue")


        a1 = [j4096['parallel_computation'][3], g4096['parallel_computation'][3], r4096['parallel_computation'][3]]
        a2 = [j4096['parallel_computation'][4], g4096['parallel_computation'][4], r4096['parallel_computation'][4]]
        a3 = [j4096['parallel_computation'][5], g4096['parallel_computation'][5], r4096['parallel_computation'][5]]
        a4 = [j4096['parallel_computation'][6], g4096['parallel_computation'][6], r4096['parallel_computation'][6]]

        rects1 = ax.bar(x - width, a1[0], width/4, label = "computation_time", color = "grey")
        rects2 = ax.bar(x - width/2, a2[0], width/4, color = "grey")
        rects3 = ax.bar(x, a3[0], width/4, color = "grey")
        rects4 = ax.bar(x + width/2, a4[0], width/4, color = "grey")


        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(f'Time Plot (in secs) ({k}×{k} table)')
        ax.set_title('Total & Computation Time')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        fig.tight_layout()
        ax.legend()
        plt.savefig("Total Time 4096.png", bbox_inches="tight")

    if k == 6144:
        labels = ['Jacobi', 'Gauss', 'Red-Black']

        a1 = [j6144['parallel'][3], g6144['parallel'][3], r6144['parallel'][3]]
        a2 = [j6144['parallel'][4], g6144['parallel'][4], r6144['parallel'][4]]
        a3 = [j6144['parallel'][5], g6144['parallel'][5], r6144['parallel'][5]]
        a4 = [j6144['parallel'][6], g6144['parallel'][6], r6144['parallel'][6]]

        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars
        fig, ax = plt.subplots(figsize = (15, 6))
        rects1 = ax.bar(x - width, a1, width/4, label="8", color = "green")
        rects2 = ax.bar(x- width/2, a2, width/4, label="16", color = "orange")
        rects3 = ax.bar(x , a3, width/4, label="32", color = "black")
        rects4 = ax.bar(x+ width/2, a4, width/4, label="64", color = "blue")

        # Add some text for labels, title and custom x-axis tick labels, etc.

        a1 = [j6144['parallel_computation'][3], g6144['parallel_computation'][3], r6144['parallel_computation'][3]]
        a2 = [j6144['parallel_computation'][4], g6144['parallel_computation'][4], r6144['parallel_computation'][4]]
        a3 = [j6144['parallel_computation'][5], g6144['parallel_computation'][5], r6144['parallel_computation'][5]]
        a4 = [j6144['parallel_computation'][6], g6144['parallel_computation'][6], r6144['parallel_computation'][6]]

        rects1 = ax.bar(x - width, a1[0], width/4, label = "computation_time", color = "grey")
        rects2 = ax.bar(x - width/2, a2[0], width/4,color = "grey")
        rects3 = ax.bar(x, a3[0], width/4, color = "grey")
        rects4 = ax.bar(x + width/2, a4[0], width/4,  color = "grey")


        ax.legend()
        ax.set_ylabel(f'Time Plot (in secs) ({k}×{k} table)')
        ax.set_title('Total & Computation Time')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        fig.tight_layout()
        plt.savefig("Total Time 6144.png", bbox_inches="tight")
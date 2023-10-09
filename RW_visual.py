import  matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(dpi=128,figsize=(10, 5))
    point_number=list(range(rw.num_points))
    plt.scatter(rw.xvalue, rw.yvalue,c=point_number,cmap=plt.cm.Blues,edgecolors='none', s=1)
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.xvalue[-1],rw.yvalue[-1],c='red',edgecolors='none',s=100)
    plt.savefig("plot_random_data.png",bbox_inches='tight')
    keep_running = input("Make another walk?  (y/n):")
    if keep_running == 'n':
            break


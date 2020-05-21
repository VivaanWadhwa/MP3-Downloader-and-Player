#%%
import matplotlib.pyplot as plt
import math
x,y=[],[]
for a in range(0,10000,100):
    x.append(a)
    y.append(a)
    
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 2, 
         marker='o', markerfacecolor='blue', markersize=1)

``
import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,6])
y = np.array([5,234])
"""
plt.plot(x,y)
# As the terminal doesnt support interactive display thus we save the graph instead of show()
#plt.show()
plt.savefig('my_plot.png')

plt.close() 

"""
#####################################################
"""The Three Objects You MUST Know
1️⃣ Figure

The entire canvas / page

Think: PDF page, slide, whiteboard

fig

2️⃣ Axes

The actual plot area

Where lines, bars, points are drawn

ax


Yes, confusing name — Axes ≠ axis (bad Matplotlib naming, not your fault).

3️⃣ Axis (x-axis, y-axis)

Ticks, labels, scales

Controlled through ax

Visual Analogy (Lock this in)
Figure (page)
 ├── Axes (plot area 1)
 └── Axes (plot area 2)




fig, ax = plt.subplots()
ax.plot(x,y)
plt.savefig("fig,ax")
plt.close()


"""
##################################
"""
plt.scatter(x,y)
plt.xlabel("x axis")
plt.ylabel("y_axis")
plt.savefig("scatterplot")
"""
###################################
"""
categories = ['A','B','C']
qty=np.array([12,10,4])

fig , ax = plt.subplots()
ax.bar(categories,qty)
plt.xlabel("x-axis")
plt.ylabel("y-label")
plt.savefig("Bar Graph")
"""
####################################
"""
data = np.random.randn(1000)
plt.hist(data , bins = 20)
plt.title("Histogram")
plt.savefig("histogram")
"""
"""Converted from matplot.ipynb."""

# <h1>Matplotlib</h1>

# for visualization

# <h4>Importing packages</h4><br>
# from matplotlib import pyplot as plt<br>
# or<br>
# import matplotlib.pyplot as plt

# show() -> used to represent graphical visualization<br>
# to view the visualization  => plt.show()

# Examples =>bar graph, histogram, pie, scatter, line

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,11)
y=x+5
plt.title("Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x,y)
plt.show()

plt.plot(x,y,'*')
plt.show()

plt.plot(x,y,'v r')
plt.show()

plt.plot(x,(3*x)+y,'v r')
plt.show()

x=np.arange(1,11)
y=3*x+5
plt.title("Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x,y,color="orange",marker='v',markersize='12',label='graph')
plt.plot(x,x+2,marker="x",label='gra')
plt.legend()
plt.show()

x=["2000","2001","2002","2003","2004"]
y=[100,159,300,256,567]
z=[10,26,58,110,126]
plt.plot(x,y,color='orange',marker='o',label='popln')
plt.plot(x,z,color='green',marker='v',label='death')
plt.legend()
plt.show()

# <h1>Prg 2</h1>

x=np.arange(0,3*np.pi,.1)
y=np.sin(x)
plt.title("sine graph")
plt.xlabel("x")
plt.ylabel("sinx")
plt.plot(x,y)
plt.show()

plt.title("cosine graph")
plt.xlabel("x")
plt.ylabel("cosx")
plt.plot(x,np.cos(x))
plt.show()

plt.title("tangent graph")
plt.xlabel("x")
plt.ylabel("tanx")
plt.plot(x,np.tan(x))
plt.show()

x=np.arange(0,3*np.pi,.1)
y=np.sin(x)
z=np.cos(x)
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('sine wave')
plt.subplot(1,2,2)
plt.plot(x,z)
plt.title('cosine wave')
plt.show()

# BARCHART

x=[7,8,10]
y=[12,16,6]
x2=[6,9,11]
y2=[6,15,7]
plt.bar(x,y,color='black',align='center')
plt.bar(x2,y2,color="red",align='center')
plt.show()

# PIECHART

x=[20,40,40]
plt.pie(x,colors=['orange','beige','brown'],labels=["x","y","z"],explode=[0.15,0,0])
plt.title("Pie Chart")
plt.legend()
plt.show()

# HISTOGRAM

x=[1,1,2,3,3,3,4,4,5,5,5,5,5]

plt.hist(np.random.randn(100),bins=50)
plt.show()

# Write a code to plot a line chart to depict the run rate of  a T20 match<br>
# Over|runs<br>
# 5   |45<br>
# 10  |79<br>
# 15  |145<br>
# 20  |234<br>
# Also change the thickness of the line<br>

x=[5,10,15,20]
y=[45,79,145,234]
z=[]
for i,j in zip(x,y):
    z.append(j/i)
plt.plot(x,z,color='blue',lw=4,label='runrate',)
plt.xlabel('over')
plt.ylabel('runrate')
plt.title("cricket")
plt.show()

# SCATTER

x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,100,86,103,87,94,78,77,85,86]
x2=[12,3,5,7,8,33,45,67]
y2=[112,83,95,78,88,93,95,100]
plt.scatter(x,y,color='lime',marker="v")
plt.scatter(x2,y2,color='red',marker="x")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('scatter - plot')
plt.show()

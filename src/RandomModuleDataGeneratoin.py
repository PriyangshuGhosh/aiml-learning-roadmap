import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(42)
"""
X=np.random.randn(100 ,2)
y = np.random.randint(0,2,100)

fig , ax= plt.subplots()
ax1 = ax.twinx()

ax.scatter(X[:, 0],X[:, 1],c=y)
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Scatter plot of Random Data")
plt.savefig("Scatter plot ")

"""
##############################################
# generating random data with probability distribution
##############################################
"""
This is not right as it plots in 2 dimensions only 


Y=np.random.choice([0,1,2],size = 1000, p=[0.1,0.2,0.7])
print(np.sum(Y==0))
print(np.sum(Y==1))
print(np.sum(Y==2))

X=np.random.randn(1000,3)
fig,ax = plt.subplots()
ax.scatter(X[:,0],X[:,1],X[:,2],c=Y)
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Random choice generator")
plt.savefig("Random generator scatter plot")
"""

##############################################
# Correct 3d plotting with probability distribution
##############################################

from mpl_toolkits.mplot3d import Axes3D
Y=np.random.choice([1,2,3],size=1000 , p = [0.5,0.4,0.1])
X=np.random.randn(1000,3)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0],X[:,1],X[:,2],c=Y)

ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel("X3")
ax.set_title("3D plotting using mpl_toolkits.mplot3d -> Axes3D")
plt.savefig("3D Plotting")
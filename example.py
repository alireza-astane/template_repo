# imports 
import numpy as np 
import matplotlib.pyplot as plt

#define a function
def sin(x):
    return np.sin(x)




# create plot
x = np.linspace(0,10,1000)
y = sin(x)

#save plot and the numpy file
plt.plot(x,y)
plt.title("sin function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print(x)
np.save("y.npy",y)
np.save("x.npy",x)



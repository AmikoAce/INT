#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

# Matplotlib is one of the librries commonly used for data visualization in Python.
# It is reccomended to visit the official Matplotlib web page: http://matplotlib.org/
# 
#     
# ## Importing

# Import the `matplotlib.pyplot` module under the name `plt` (the tidy way):

# In[1]:


import matplotlib.pyplot as plt


# Write this line in Jupyter notebook:

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# This will produce all the plots genereted in the code, inside the notebook. 
# This is *not* required in Spyder, etc.

# # Example 1
# 
# 

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
#Used only in Jupyter Notebook to get inline plots:
get_ipython().run_line_magic('matplotlib', 'inline')
x = np.array([1, 2, 3, 4, 5])
y = np.array([50, 20, 30, 90, 100])
plt.plot (x,y)
plt.show()
print(x)


# ## Line Style
# 
# 

# In[4]:


x=np.array([1,2,3,4,5])
y=np.array([50,20,30,90,100])
plt.plot(x, y, color="red", ls='--', marker='o')
plt.plot(x+1, y-5, color="red", ls='--', marker='o')
plt.xlabel('Bins')
plt.ylabel('Quantities')
plt.title('My Plot')
plt.show()


# ## Sin and Cos

# In[5]:


x = np.linspace(-np.pi, np.pi)
y, z = np.cos(x), np.sin(x)

plt.plot(x, y, color = 'green')
plt.plot(x, z, color = 'blue')
plt.show()


# ### Sin and Cos with Line Styles

# In[6]:


x = np.linspace(-np.pi, np.pi)
y, z = np.cos(x), np.sin(x)
plt.plot(x, y, color = 'green', ls='-', 
         marker='o',markersize=8, 
         markeredgecolor="green", markeredgewidth=3,
         markerfacecolor="red")
plt.plot(x, z, color = 'b', ls='-',lw=3,marker='s',
         markerfacecolor="y")

plt.show()


# ## Multiple Axes

# Code is a little more complicated, but the advantage is that we now have full control of where the plot axes are placed, and we can easily add more than one axis to the figure:

# In[7]:


x=np.arange(100)
y=x**2
# Creates blank canvas
fig = plt.figure()
print("type of fig:" , type(fig))

outer = fig.add_axes([0.1, 0.1, 0.9, 0.9]) # main axes
inner = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # "inner" axes

# Larger Figure Axes 1
outer.plot(x, y, 'b')
print("type(outer)=", type(outer))
outer.set_xlabel('X_label_Large')
outer.set_ylabel('Y_label_Large')
outer.set_title('Main Axes Title')

# Insert Figure Axes 2
inner.plot(y, x, 'r')
inner.set_xlabel('X_label_Small')
inner.set_ylabel('Y_label_Small')
inner.set_title('Small Axes Title');


# ____
# ## Legends and Labels

# ### Legends

# In[8]:


fig = plt.figure()
x=np.linspace(0.1,10.0,num=50)
ax = fig.add_axes([0,0,1,1])
import math
ax.plot(x, np.log10(x), label="log10")
ax.plot(x, x**0.5, label="Square Root")
ax.legend

"""
fig2.plot(x, np.log10(x), label="log10") # NO PLOT FOR FIGURE
fig2.plot(x, x**0.5, label="Square Root")
fig2.legend
"""
plt.plot(x, np.log10(x))
plt.plot(x, x**0.5, label="Square Root")
#Without axes - only 1 legend...
plt.legend() 


# In[9]:


fig = plt.figure()
x=np.linspace(0.1,10.0,num=50)
ax = fig.add_axes([0,0,1,1])
import math
ax.plot(x, np.log10(x), label="log10")
ax.plot(x, x**0.5, label="Square Root")
#ax.text(0.55, 2, r"$y=sqrt(x)$", fontsize=20, color="orange")
#ax.text(5, 0.1, r"$y=log(x)$", fontsize=20, color="blue");
ax.text(0.55, 2, "y=sqrt(x)", fontsize=20, color="orange")
ax.text(5, 0.1, "y=log(x)", fontsize=20, color="blue")


# ## Figure size & Saving Figures

# In[41]:


"""
fig, axes = plt.subplots(figsize=(5,3))
x=np.linspace(1.0,10.0,num=100)
y=2*x+np.sin(x)+5
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');
"""

fig = plt.figure()
plt.plot(figsize=(15,3))
ax = fig.add_axes([0,0,10,10])
x=np.linspace(0.0,10.0,num=100)
y=2*x+np.sin(x)+5
ax.plot(x, x+5, 'g')
#ax.plot(x, y**2, 'r')
#plt.show()
"""
plt.set_xlabel('x')
plt.set_ylabel('y')
plt.set_title('title');
"""


# In[16]:


fig, axes = plt.subplots(figsize=(8,1.5))
x=np.linspace(1.0,10.0,num=100)
y=2*x+np.sin(x)+5
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');


# ## Saving figures

# In[17]:


fig.savefig("filename1.png")


# In[18]:


fig.savefig("filename2.pdf", dpi=150)


# # Some Nice (and Useful!) Plots

# In[22]:


import random

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


# ## Histogram

# In[25]:


import random
vals = np.random.randn(100)
plt.hist(vals, bins=10)


# In[26]:


plt.hist(vals, bins=50)


# ## 3D Plots

# In[155]:


from mpl_toolkits.mplot3d.axes3d import Axes3D


# ## Meshgrid

# In[148]:


# Make data.
XX = np.arange(-5, 5, 0.25)
YY = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(XX, YY)
R = np.sqrt(X**2 + Y**2)
Z=np.sin(R)
Z2=np.sqrt(R)
X


# In[137]:


Y


# In[139]:


plt.plot(X,Y, marker='.', color='k', linestyle='none')


# In[159]:


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
XX = np.arange(-5, 5, 0.25)
YY = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(XX, YY)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


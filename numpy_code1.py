#!/usr/bin/env python
# coding: utf-8

# #                                   NumPy 
# 
# NumPy (or Numpy) is a Linear Algebra Library for Python. Good for manipulating large arrays and matrices of numeric data.

# 
# ## Numpy Arrays
# 
# N-dimension tables of elements
# 
# ## Creating NumPy Arrays
# 
# ### From a Python List
# 
# We can create an array by directly converting a list or list of lists:

# In[4]:


import numpy as np
a = np.array([0,1,2])
a


# In[5]:


mat=np.array([[0, 1, 2], [3, 4, 5]])
mat


# ## Built-in Methods
# 
# There are lots of built-in ways to generate Arrays

# ### arange
# 
# Return evenly spaced values within a given interval.

# In[6]:


np.arange(0,10)


# In[7]:


np.arange(0,11,2)


# ## Attributes & Methods
# 
# Shape is an attribute that arrays have (not a method):
# 

# ### zeros and ones
# 
# Generate arrays of zeros or ones

# In[8]:


np.zeros(3, dtype=int)


# In[9]:


np.ones((2,3), dtype = float)


# In[10]:


np.ones(3)


# In[11]:


np.ones((3,3))


# In[12]:


arr1 = np.arange(10)
arr2 = np.arange(2,7)
arr3 = np.arange(2,7,2)
[print(x) for x in [arr1, arr2, arr3]]


# ### linspace
# Return evenly spaced numbers over a specified interval.

# In[13]:


np.linspace(1,5,9)


# ## Random 
# 
# Numpy also has lots of ways to create random number arrays:
# 
# ### rand
# Create an array of the given shape and populate it with
# random samples from a uniform distribution
# over ``[0, 1)``.

# In[14]:


np.random.rand(5)


# In[15]:


np.random.rand(5,1)


# ### randn
# 
# Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform:

# In[16]:


np.random.randn(2)


# In[17]:


np.random.randn(5,1)


# ### randint
# Return random integers from `low` (inclusive) to `high` (exclusive).

# In[18]:


np.random.randint(1,100)


# In[20]:


np.random.randint(1,100,10)


# In[23]:


# Vector
arr1.shape


# ## Array Attributes and Methods
# 
# Let's discuss some useful attributes and methods or an array:

# ## Shape
# Returns a tuple containing the size(s) of the array.

# In[24]:


mat = np.array([[0, 1, 2], [3, 4, 5]]) 
mat.shape


# ## Len & Transpose
# Return array's length and transpose, respectively.

# In[25]:


len(mat) 


# In[26]:


mat.T


# ## Reshape
# Returns an array containing the same data with a new shape.

# In[27]:


a=np.arange(10.0)
a


# In[28]:


a=a.reshape(5,2)
a


# In[29]:


a.shape


# In[30]:


a.reshape(2,5)


# ### dtype & type
# 
# You can also grab the data type of the object in the array:

# In[31]:


a = np.array(range(10), dtype=float) 
a


# In[32]:


a.dtype


# In[33]:


type(a)


# In[34]:


a=np.array([1,'a',-2.2])
a


# In[35]:


a[0]


# In[36]:


type(a)


# In[37]:


a.dtype


# ## Indexing & Slicing
# Basically similar to Lists.

# In[38]:


a = np.diag(np.arange(3))
a


# In[39]:


a[2,1]


# In[40]:


a[1:]


# In[41]:


a[2,1]=10
a[:,1]


# In[42]:


a[2,1:]


# In[43]:


a=np.arange(0,100).reshape(10,10)[:6,:6]
a


# In[44]:


a[2::2,0::2]


# ## Reductions: Sum
# 

# In[45]:


x = np.array([[1, 1], [2, 2]])
x


# In[46]:


x.sum()


# In[47]:


x.sum(axis=0)


# In[48]:


x.sum(axis=1)


# In[49]:


a=np.array([[4, 3, 5], [1, 2, 1]])
b=np.sort(a,axis=1)
b


# In[50]:


a.sort(axis=0)
a


# In[ ]:





# ## Array Arithmetic
# 

# In[51]:


x = np.array([1, 5, 2])
y = np.array([7, 4, 1])
x+y

x.sum()
# In[52]:


x*y


# In[53]:


np.dot(x,y)


# In[54]:


[x-y, x/y, x%y]


# ## Broadcasting
# 

# In[55]:


a=np.array([1,2,3])
a*2


# In[56]:


a=3
a


# In[57]:


a = np.array([[ 0.0, 0.0, 0.0],
              [10.0,10.0,10.0],
              [20.0,20.0,20.0],
              [30.0,30.0,30.0]])
b=np.array([0.0,1.0,2.0])
a+b


# In[58]:


b.T is b


# In[59]:


a=np.array([1,2,3,4])
#a+b


# ## Comparison and Boolean operators
# 

# In[60]:


a = np.array([1,4,3,5,2,3])
b = np.array([1,2,4,5,2,1])
a==b


# In[61]:


comp=a==b
comp


# In[62]:


[comp.any() , comp.all() , comp.nonzero()]


# ## Logical indexing
# 

# In[63]:


a = np.random.randint(0, 20, 15)
a


# In[64]:


a%3==0


# In[65]:


a[a%3==0]


# In[66]:


a[a%3==0]=99
a


# In[122]:


a[[0,1,7,2]]


# ## Array Stacking
# 

# In[124]:


a = np.array([1,2,3])
b = np.array([2,3,4])
print(a)


# In[130]:


print(np.hstack([a,b]))


# In[142]:


c=np.array([[1],[2],[3]])
d=np.array([[2],[3],[4]])
print(c)


# In[138]:


c=np.array([[1],[2],[3]])
d=np.array([[2],[3],[4]])
print(np.hstack([c,d]))


# In[140]:


print(np.vstack((a,b)))


# In[141]:


print(np.vstack((c,d)))


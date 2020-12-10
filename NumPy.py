#!/usr/bin/env python
# coding: utf-8

# # NumPy - Numerical Python
# NumPy is a python library used for working with arrays.<br>
# It also has functions linear algebra and working with matrices.<br>
# NumPy offers the `ndarray` object which is maintained as a continuous block of memory (as opposed to the dynamically allocated Python `list`s) and supports a variety of functions for working with `ndarray`s (N-dimensional).<br>
# As such, NumPy arrays work much faster than Python lists. The parts of NumPy which require fast computations are written in C or C++, it is not built over Python data structures and operators.<br>
# NumPy documentation can be found here: https://numpy.org/doc/stable/index.html

# In[ ]:


get_ipython().system('pip install numpy')
get_ipython().system('pip install matplotlib')
import numpy as np 
import matplotlib.pyplot as plt


# The basic NumPy array can be constructed from a Python `list`.

# In[ ]:


li = [1, 2, 3, 4, 5]
print("list:",li)
print("list type:",type(li))
print("list repr:", repr(li))
arr1 = np.array(li)
print("array:",arr1)
print("array type:",type(arr1))
print("array repr:",repr(arr1))


# *Notes:*
# 1. The NumPy array is printed as a space-delimited vector.
# 2. The Numpy array class is ndarry, np.array is not a constructor but rather a function that returns a `ndarray` object.
# 

# In[ ]:


arr0 = np.array(17)
print(arr0)
print(type(arr0))


# In[ ]:


arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)


# In[ ]:


arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)


# In[ ]:


print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)


# In[ ]:


arr = np.array(arr3, ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)


# *The `ndmin` argument expands the created array up to the given number of dimensions if needed*

# ### Array Indexing and Slicing

# In[ ]:


print("arr1\t\t",arr1)
print("arr1[0]\t\t",arr1[0])
print("arr1[1]\t\t",arr1[1])
print("arr1[-1]\t",arr1[-1])
print("arr1[1:3]\t",arr1[1:3])


# In[ ]:


print("arr2\n",arr2)
print("arr2[0]:",arr2[0])
print("arr2[1,0]:",arr2[1,0])
print("arr2[-1,1]:",arr2[-1,1])
print("arr2[1:3]:",arr2[1:3])
##print("arr2[3]:",arr2[3])


# In[ ]:


print("arr3\n",arr3)
print("arr3[0]\n",arr3[0])
print("arr3[1,0]:",arr3[1,0])
print("arr3[-1,1,0]:",arr3[-1,1,0])
print("arr3[1,0:1,-1:]:\n",arr3[1,0:2,-1:])
print("arr3[-1][1][0]:",arr3[-1][1][0])


# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'arr3[-1,1,0]')


# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'arr3[-1][1][0]')


# In[ ]:


get_ipython().run_cell_magic('timeit', '-n1000', 'n = np.arange(1000)\nn**2')


# In[ ]:


get_ipython().run_cell_magic('timeit', '-n1000', 'p = range(1000)\n[i**2 for i in p]')


# In[ ]:


iterarray = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in iterarray:
    print(x)
    for y in x:
        print(y)
        for z in y:
            print(z)


# In[ ]:


for x in np.nditer(iterarray):
    print(x)


# In[ ]:


for i, x in np.ndenumerate(iterarray):
    print(i, x)


# In[ ]:


n_array = np.array(((1,2,3),(4,5,6)))
print(n_array)
n_array[0,1] = 100
print(n_array)


# In[ ]:


##n_array[0] = "hello" #error


# In[ ]:


n_array[1] = np.array([7,8,9])
print(n_array)
##n_array[1] = np.array([7,8,9,10]) #error


# *`ndarray`s are mutable, however you cannot change the type or shape*

# ### Limitations
# A `ndarray` holds a single data type and all arrays in the same dimension must have the same length.

# In[ ]:


np.array([1,2.2,3.3])


# In[ ]:


np.array([1,2,"a"]) 


# In[ ]:


np.array([1,2,True]) 


# In[ ]:


np.array([1,2,print]) 


# In[ ]:


np.array([[1,2,3],[1,[2]]]) #error (deprecated)


# **Older versions of Numpy will implicitly transform this "matrix" into a flat array of `list` objects. Newer versions will require an explicit declaration of `dtype`=`object` for this**

# ### Data Types
# NumPy extends the basic python types into C-like types that can be stored in arrays. Numpy will attempt to assign a type based on array content. Alternatively, a `dtype` argument can be set when creating the array.

# In[ ]:


int_array = np.array([1, 2, 3, 4])
print(int_array)
print(int_array.dtype)
str_array = np.array([1, 2, 3, 4], dtype="S")
print(str_array)
print(str_array.dtype)


# In[ ]:


num_array = np.array([1, 2, 3, 4], dtype='i4')
print(num_array)
print(num_array.dtype)
num_array = np.array([32, 64, 128, 256], dtype='i1')
print(num_array)
print(num_array.dtype)


# In[ ]:


num_array = np.array(["1", "2", "3", "4"], dtype='i1')
print(num_array)
print(num_array.dtype)
##num_array = np.array(["a", "b", "c", "d"], dtype='i1') #error


# ### Array Shape

# In[ ]:


print("array 0: ",arr0)
print('shape of array 0 :', arr0.shape,'\n')
print("array 1: ",arr1)
print('shape of array 1 :', arr1.shape,'\n')
print("array 2: ",arr2)
print('shape of array 2 :', arr2.shape,'\n')
print("array 3: ",arr3)
print('shape of array 3 :', arr3.shape,'\n')
print("array: ",arr)
print('shape of array :', arr.shape)


# In[ ]:


flat = np.arange(1,13)
matrix = flat.reshape(4, 3)
print(flat)
print(matrix)


# In[ ]:


matrix3d = flat.reshape(2, 3, 2)
print(matrix3d)


# In[ ]:


matrix4d = flat.reshape(2, 2, 1,-1) # we can have 1 dimension be unknown (-1) and NumPy will fill in the blank if possible.
print(matrix4d)


# In[ ]:


u_matrix = flat.reshape(-1,6)
print(u_matrix)


# *Note: bad dimensions for reshape will result in an exception*

# In[ ]:


print("matrix: ",matrix.base)
print("flat: ",flat.base)


# ##### Some NumPy functions return a 'copy' of an `ndarray`, while others return a 'view'. If a view is returned, then it's `base` attribute will show the original `ndarray`. <br> If an array is a base itself, the `base` attribute will be `None`.

# In[ ]:


matrix3d[1,1,0] = 17
print(matrix3d)
print(matrix)
print(u_matrix)
print(flat)


# In[ ]:


print(u_matrix.reshape(12))
print(u_matrix.reshape(-1))
print(u_matrix)


# ### Filtering Arrays
# We can filter arrays by using a boolean mask, returning only the values where the indices match the `True` indices of the filter.

# In[ ]:


fil = [True,True,False,False]*3
flat_fil = flat[fil]
print(flat_fil)
print(flat_fil.base)


# In[ ]:


filter_arr = []

for element in flat:
    if element > 6:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
flat_filter = flat[filter_arr]
print(filter_arr)
print(flat_filter)


# In[ ]:


even_filter = flat % 2 == 0
flat_even = flat[even_filter]
print(even_filter)
print(flat_even)


# *Note: using this method, a Boolean `ndarray` is created for the filter*

# In[ ]:


odd_filter = matrix3d % 2 == 0
matrix3d_odd = matrix3d[odd_filter]
print(odd_filter)
print(matrix3d_odd)


# In[ ]:


print(matrix3d)
t=np.where(matrix3d < 7)
print(t)
matrix3d[t]


# ### Operations on Arrays

# In[ ]:


a = np.arange(10)
l = [i for i in range(5)]*2
b = a[l]
print(a)
print(l)
print(b)
print(a==b)


# In[ ]:


rand = np.random.rand(6,6)*2*np.pi
randint = np.random.randint(1,20,size=(5,5))
print(rand)
print(randint)


# In[ ]:


randint[0]|randint[1]


# In[ ]:


rand.sum()


# In[ ]:


rand.max()


# In[ ]:


rand.min()


# In[ ]:


randint.mean()


# In[ ]:


print(randint.mean(0)) # columns
print(randint.mean(1)) # rows


# In[ ]:


randint.std()


# In[ ]:


np.median(randint)


# In[ ]:


np.unique(randint)


# In[ ]:


rand_sort = np.sort(rand.reshape(-1))
sinus = np.sin(rand_sort)
print( rand_sort)
print( sinus)


# In[ ]:


plt.plot(rand_sort,sinus)


# ## Example - Random Walks

# In[ ]:


walks, time = 10,10
r_walk=np.random.choice([-1,1],(walks,time)) #simulate steps in random walk
print(r_walk)


# In[ ]:


pos = np.cumsum(r_walk, axis=1)
print(pos) #cumulative position in random walk


# In[ ]:


dist = np.abs(pos)
print(dist)


# In[ ]:


mean = np.mean(dist, axis=0)
print(mean)


# In[ ]:


rand_walks, travel_time = 5000,500
sample_walks=np.random.choice([-1,1],(rand_walks,travel_time))
positions = np.cumsum(sample_walks, axis=1)
distance = np.abs(positions**2)
mean_distance = np.mean(np.sqrt(distance), axis=0)


# In[ ]:


t = np.arange(travel_time)
plt.plot(t, mean_distance, 'g.')


# In[ ]:


pf = np.polyfit(t,mean_distance,3)
print(pf)


# In[ ]:


p = np.poly1d(pf)
print(p)
print("p(10): ",p(10))
print(type(p))


# *The `poly1d` object makes use of the dunder method `__call__` which makes an object callable like a function.*

# In[ ]:


plt.plot(t, mean_distance, 'g.',t, p(t),'b-')


# In[ ]:


print(np.sqrt(2/np.pi))
t_sim = np.arange(2*travel_time)
plt.plot(t_sim, p(t_sim),'b-')


# In[ ]:


t = np.arange(travel_time)
plt.plot(t, mean_distance, 'g.',t, np.sqrt(t), 'b-')


# In[ ]:


pf2 = np.polyfit(np.sqrt(t),mean_distance,3)
print(pf2)
p2 = np.poly1d(pf2)
print(p2)
t_sim = np.arange(2*travel_time)
plt.plot(t_sim, p2(np.sqrt(t_sim)),'b-')


# In[ ]:


pf3 = np.polyfit(np.sqrt(t),mean_distance,1)
print(pf3)
p3 = np.poly1d(pf3)
print(p3)
plt.plot(t_sim, p3(np.sqrt(t_sim)),'b-')


# In[ ]:


plt.plot(t, mean_distance, 'g.',t, p3(np.sqrt(t)),'b-')


# In[ ]:


print(np.sqrt(2/np.pi))
plt.plot(t, mean_distance, 'g+',t, p3(np.sqrt(t)), 'b-', t, np.sqrt(2*t/np.pi),'y-')


# ## Example - Sea  Ice File

# In[ ]:


import csv
date = {'north':[],'south':[]}
extent = {'north':[],'south':[]}
with open('sea-ice-fixed.csv') as file:
    reader = csv.DictReader(file)
    for d in reader:
        extent[d["hemisphere"]].append(d['Extent'])
        date[d["hemisphere"]].append(d['Date'])
print(date['north'][0])
print(extent['north'][0])


# In[ ]:


n_extent = np.array(extent['north'], dtype = 'f')
s_extent = np.array(extent['south'], dtype = 'f')
n_extent


# In[ ]:


n_date = np.array(date['north'], dtype = 'datetime64')
s_date = np.array(date['south'], dtype = 'datetime64')
n_date


# In[ ]:


n_date = np.array(date['north'], dtype = 'datetime64[D]')
s_date = np.array(date['south'], dtype = 'datetime64[D]')
n_date


# In[ ]:


n_date[5]-n_date[0]


# In[ ]:


n_date < np.datetime64('1978-10-27')


# In[ ]:


plt.plot(n_date,n_extent)


# In[ ]:


plt.plot(s_date,s_extent)


# In[ ]:


fig=plt.figure(figsize=(12, 6))
plt.plot(n_date,n_extent,label='Northern Hemisphere')
plt.plot(s_date,s_extent,label='Southern  Hemisphere')
plt.legend(bbox_to_anchor=(0., -.362, 1., .102), loc=3, ncol=2, 
           mode="expand", borderaxespad=0.)


# In[ ]:


years = np.unique(n_date.astype('datetime64[Y]'))
print(years)


# In[ ]:


dates = []
extents = {"n":[], "s":[]}
for y in years:
    nind = np.where(n_date.astype('datetime64[Y]') == y)
    sind = np.where(s_date.astype('datetime64[Y]') == y)
    dates.append(n_date[nind ])
    extents["s"].append(s_extent[sind].mean())
    extents["n"].append(n_extent[nind].mean())
print(dates[0])
print(extents["n"][0])
print(extents["s"])


# In[ ]:


fig=plt.figure(figsize=(12, 6))
plt.plot(years[1:],extents["n"][1:],label='Northern Hemisphere') # the first year has only partial data so we ignore it
plt.plot(years[1:],extents["s"][1:],label='Southern  Hemisphere')
plt.legend(bbox_to_anchor=(0., -.362, 1., .102), loc=3, ncol=2, 
           mode="expand", borderaxespad=0.)


# In[ ]:


date_shuffle = n_date.copy()
extent_shuffle = n_extent.copy()
perm = np.random.permutation(date_shuffle.size)
print(perm)
date_shuffle = date_shuffle[perm]
extent_shuffle = extent_shuffle[perm]
print(date_shuffle)
print(extent_shuffle)


# In[ ]:


plt.plot(date_shuffle,extent_shuffle)


# In[ ]:


dateorder = date_shuffle.argsort()
dateorder


# In[ ]:


ordered_date = date_shuffle[dateorder]
ordered_extent = extent_shuffle[dateorder]
print(ordered_date)
print(ordered_extent)


# In[ ]:


plt.plot(ordered_date,ordered_extent)


# ### Structured Arrays
# NumPy arrays can be arrays whose datatype is a composition of simple datatypes orgranizes as a sequence of named fields. This is similar to having each item in the array be a well-defined dictionary object. These arrays must still conform to the limitations of simple arrays with regards to data type and same-sized dimensions. 

# In[ ]:


import csv
ice_data = []
dates= []
extents = []
hemispheres = []
with open('sea-ice-fixed.csv') as file:
    reader = csv.DictReader(file)
    for d in reader:
        ice_data.append((d['Date'],d['hemisphere'],d['Extent']))
print(ice_data[0])


# In[ ]:


ice_array = np.array(ice_data,dtype=[('date','datetime64[D]'),('hemisphere','U5'),('extent','f')])
print(ice_array[0])
print(ice_array[['date','extent']][0:10])
print(ice_array.dtype)


# In[ ]:


averages =  {"n":[], "s":[]}
for y in years[1:]:
    year = (ice_array['date'].astype('datetime64[Y]') == y)
    averages["n"].append(ice_array[ year & (ice_array['hemisphere']=="north")]['extent'].mean())
    averages["s"].append(ice_array[ year & (ice_array['hemisphere']=="south")]['extent'].mean())
print(averages["n"])
print(averages["s"])


# In[ ]:


fig=plt.figure(figsize=(12, 6))
plt.plot(years[1:-1],averages["n"][1:],label='Northern Hemisphere') # the first year has only partial data so we ignore it
plt.plot(years[1:-1],averages["s"][1:],label='Southern  Hemisphere')
plt.legend(bbox_to_anchor=(0., -.362, 1., .102), loc=3, ncol=2, 
           mode="expand", borderaxespad=0.)


# In[ ]:





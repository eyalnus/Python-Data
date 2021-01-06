#!/usr/bin/env python
# coding: utf-8

# # Visualization with Matplotlib
# Matplotlib is a plotting library modeled after Matlab's plotting capabilities. Matplot works with basic Python objects as well as Numpy arrays, and is integrated into Pandas for quick DataFrame plotting.<br>
# Plot types include line plots, scatter plots, image plots, contour plots, histograms and others. Matplotlib also allows for a wide variety of styling options. While Matplotlib was originally designed only for 2-dimensional plots, an add-on toolkit, `mpl_toolkits`, is available for some basic 3-d plotting.

# In[ ]:


get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')
get_ipython().system('pip install numpy')
get_ipython().system('pip install pandas')
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
plt.style.use('classic')


# ### Pyplot
# The `Pyplot` module gives us an easy interface for Matplotlib plotting, including convenience methods and render handling. You can think of `Pyplot` as a canvas which gives you access to plotting operations supported by `Matplotlib`. All plotting will be done on the canvas and calling `Pyplot`'s `show()` function will render the canvas.

# In[ ]:


x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()


# *Note that both plots were created on the same axes*

# In[ ]:


x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(2*x), '-')
plt.plot(x, np.cos(2*x), '--')


# *Jupyter's environment does not require a call to the `show()` function. This is done implicitly.*

# In[ ]:


x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), 'r-')
plt.plot(x, np.cos(x), 'k--')
plt.savefig('sinus.png')


# *We can call the `savefig()` to save the plot to an image file.*

# In[ ]:


from IPython.display import Image
Image('sinus.png')


# ## Separate plots
# In order to display plot separately, we must create a figure on the canvas with multiple plot axes. This can be done using 2 methods as follows. The first is a **stateful** interface, where we set the state of `Pyplot` to reference the axes we will be plotting on before each plot. The second is an **object oriented** interface, where we call plotting functions for each axes object.

# In[ ]:


plt.figure()  # create a plot figure

# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))

# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x));

plt.show()


# In[ ]:


# First create a grid of plots
# ax will be an array of two Axes objects, fig will be the figure object
fig, ax = plt.subplots(2)

# Call plot() method on the appropriate object
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()


# ## Plot Color and Styles

# In[ ]:


plt.style.use('seaborn-whitegrid')


# In[ ]:


x = np.linspace(0, 10, 1000)
fig = plt.figure()
ax = plt.axes()
ax.plot(x, np.sin(x))
plt.show()


# In[ ]:


plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
plt.show()


# If no color is specified, Matplotlib will automatically cycle through a set of default colors for multiple lines.
# 
# Similarly, the line style can be adjusted using the ``linestyle`` keyword:

# In[ ]:


plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':');  # dotted
plt.show()


# ##### Shorthand Styling
# All line styles but only basic colors are supported in this method (rgbcmykw)

# In[ ]:


plt.plot(x, x + 0, '-g')  # solid green
plt.plot(x, x + 1, '--c') # dashed cyan
plt.plot(x, x + 2, '-.k') # dashdot black
plt.plot(x, x + 3, ':r');  # dotted red
plt.show()


# In[ ]:


plt.plot(x, np.sin(4*x))

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)
plt.show()


# In[ ]:


plt.plot(x, np.sin(4*x))

plt.xlim(10, 0) # reverse axes
plt.ylim(1.2, -1.2); # reverse axes


# *You can also reverse the axes order.*

# In[ ]:


plt.plot(x, np.sin(x))
plt.axis('equal')
plt.show()


# ##### You can set the axes for each subplot

# In[ ]:



fig, ax = plt.subplots(2)
fig.subplots_adjust(hspace=0.4)
ax[0].plot(x, np.sin(x))
ax[1].plot(2*x, 2*np.cos(2*x))
ax[0].set(xlim=(0, 10), ylim=(-1.5, 1.5),
       xlabel='x', ylabel='sin(x)',
       title='Sinus Plot');
ax[1].set(xlim=(0, 20), ylim=(-3, 3),
       xlabel='x', ylabel='cos(x)',
       title='Cosinus Plot');
plt.show()


# ### Labeling

# In[ ]:


plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");


# In[ ]:


plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')
plt.legend()
plt.show()


# ## Scatter Plots
# For the basic functionalities of `Matplotlib` we experimented with line plots. This is just one of many plot types offered by `Matplotlib`. We will now discuss the scatter plot, which is most useful when dealing with sampled data.

# In[ ]:


x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='navy')


# *Using a dot-style instead of a line style in the `plot` method gives us a simple scatter plot.*

# In[ ]:


rng = np.random.RandomState(0)
for marker in ['1','o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd','p']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8);


# In[ ]:


plt.plot(x, y, '-*k');


# In[ ]:


plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=1,
         markerfacecolor='red',
         markeredgecolor='orange',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2);


# #### A more powerful scatter plot tool - `plt.scatter` 
# The primary difference of ``plt.scatter`` from ``plt.plot`` is that it can be used to create scatter plots where the properties of each individual point (size, face color, edge color, etc.) can be individually controlled or mapped to data.<br>
# *Note: this functionality comes at the cost of efficiency - scatter plots with many data points using this method may be computationally intensive and reduce performance.*

# In[ ]:


plt.scatter(x, y, marker='o');


# In[ ]:


rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar();  # show color scale


# ### Example - Diamonds

# In[ ]:


df = pd.read_csv('diamonds.csv')
print(df.head())


# In[ ]:


diamonds = df.loc[((df.y-df.x).abs()<0.1) & (df.x>1) ]
plt.scatter(diamonds.x, diamonds.carat, s=diamonds.price/20, alpha=0.3,
            cmap='jet')


# In[ ]:


diamonds = df.loc[((df.y-df.x).abs()<0.1) & (df.x>1) & (df.cut=="Fair")]
plt.scatter(diamonds.x, diamonds.carat, s=diamonds.price/20, alpha=0.3,
            cmap='jet')


# In[ ]:


sorted_color=sorted(df.color.unique())
sorted_color


# In[ ]:


color_cat = pd.Categorical(diamonds.color,
  ordered=True,
  categories=sorted_color
)
color_cat.codes


# In[ ]:


plt.scatter(diamonds.x, diamonds.carat, c=color_cat.codes,s=diamonds.price/20, alpha=0.3,
            cmap='jet')
plt.colorbar()
plt.show()


# In[ ]:


print(df.clarity.unique())
sorted_clarity = ['I1','SI2', 'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'IF']


# In[ ]:


clarity_cat = pd.Categorical(diamonds.clarity,
  ordered=True,
  categories=sorted_clarity
)
clarity_cat.codes


# In[ ]:


plt.scatter(diamonds.x, diamonds.carat, c=clarity_cat.codes,s=diamonds.price/20, alpha=0.3,
            cmap='jet')
plt.colorbar()
plt.show()


# ### Example - Population

# In[ ]:


cities = pd.read_csv('california_cities.csv')
cities.head()


# In[ ]:



# Extract the data we're interested in
lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_land_km2'].values

# Scatter the points, using size and color but no label
plt.scatter(lon, lat, label=None,
            c=np.log10(population), cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
plt.axis("equal")
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')


plt.title('California Cities: Area and Population');


# In[ ]:


plt.scatter(lon, lat, label=None,
            c=np.log10(population), cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
plt.axis("equal")
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7) #limit color scale to create better variation
plt.title('California Cities: Area and Population');
# Here we create a legend:
# we'll plot empty lists with the desired size and label
for ar in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=ar,
                label=str(ar) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')


# *The legend will always reference some object that is on the plot, so if we'd like to display a particular shape we need to plot it. In this case, the objects we want (gray circles) are not on the plot, so we fake them by plotting empty lists.
# Notice too that the legend only lists plot elements that have a label specified. By plotting empty lists, we create labeled plot objects which are picked up by the legend, and now our legend tells us some useful information.*

# ### Contour Plots
# Sometimes it is useful to display three-dimensional data in two dimensions using contours or color-coded regions.
# There are three Matplotlib functions that can be helpful for this task: ``plt.contour`` for contour plots, ``plt.contourf`` for filled contour plots, and ``plt.imshow`` for showing images.

# In[ ]:


def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


# #### `contour`
# Takes three arguments: a grid of x values, a grid of y values, and a grid of z values. The x and y values represent positions on the plot, and the z values will be represented by the contour levels. 

# In[ ]:


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y) #create a 2-d matrix from each array 
Z = f(X, Y)

print(X, X.shape)
print(Z,Z.shape)


# In[ ]:


plt.contour(X, Y, Z, colors='black');


# *When a single color is used, dashed lines represent negative values.*

# In[ ]:


plt.contour(X, Y, Z, 20, cmap='RdGy');
plt.colorbar();


# #### `contourf`
# Fills the white spaces for better visualization.

# In[ ]:


plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar();


# In[ ]:


from mpl_toolkits.mplot3d import Axes3D  
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z,
                       linewidth=0, antialiased=False)
plt.show()


# In[ ]:


from mpl_toolkits.mplot3d import Axes3D  
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(45, 45)
surf = ax.plot_surface(X, Y, Z,
                       linewidth=0, antialiased=False)
plt.show()


# In[ ]:


ax = plt.axes(projection='3d')
ax.scatter(X, Y, Z, c=Z, cmap='viridis', linewidth=0.5)
ax.view_init(20, 30)
plt.show()


# In[ ]:


ax = plt.axes(projection='3d')
ax.scatter(X, Y, Z, c=Z, cmap='viridis', linewidth=0.5)
ax.view_init(90, 270)
plt.show()


# In[ ]:


plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
           cmap='RdGy',aspect=1)
plt.colorbar()
plt.show()


# #### Example - wildfires

# In[ ]:


fires1 = pd.read_csv('fire_archive_M6_101673.csv')
fires2 = pd.read_csv('fire_nrt_M6_101673.csv')
fires = pd.concat([fires1,fires2])
fires.latitude = fires.latitude.round(0)
fires.longitude = fires.longitude.round(0)
fires.head()


# In[ ]:


m=fires.groupby(['latitude','longitude']).mean()
m.head()


# In[ ]:


bright=m.pivot_table(index='latitude',columns='longitude',values='brightness').T.values
X_unique = np.sort(fires.latitude.unique())
Y_unique = np.sort(fires.longitude.unique())
X, Y = np.meshgrid(X_unique, Y_unique)


# In[ ]:



# Generate a contour plot
plt.contourf(X, Y, bright,levels=20, cmap=plt.cm.afmhot)
plt.colorbar()
plt.show()


# In[ ]:


plt.imshow(bright, extent=[X_unique.min(),X_unique.max(),Y_unique.min(),Y_unique.max()], origin='lower',
           cmap=plt.cm.afmhot,aspect=1)
plt.colorbar()
plt.show()


# ### Histogtams

# In[ ]:


hist_data=diamonds.x
plt.hist(hist_data)
plt.show()


# In[ ]:


plt.hist(hist_data, bins=30, alpha=0.5,
         histtype='stepfilled', color='steelblue',
         edgecolor='navy')
plt.show()


# In[ ]:



kwargs = dict(histtype='stepfilled', alpha=0.3,  bins=40) #density normalizes data

plt.hist(hist_data, **kwargs)
plt.hist(diamonds.carat, **kwargs)
plt.hist(diamonds.z, **kwargs)
plt.show()


# ### Subplots

# In[ ]:


fig = plt.figure() # create figure 
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
                   xticklabels=[], ylim=(-1.2, 1.2)) #add axes object: left, bottom, width, height
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
                   ylim=(-1.2, 1.2))

x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x))
plt.show()


# In[ ]:


for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')
plt.show()


# In[ ]:


fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)),
           fontsize=18, ha='center')
plt.show()


# In[ ]:


fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
for ind,axis in np.ndenumerate(ax):
    print(ind)
    axis.plot(x,np.sin((ind[0]+1)*x)+ind[1]*np.cos(x))
plt.show()


# In[ ]:


grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3) #convience method for creating grid coordinates recognized by subplot
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])
plt.show()


# In[ ]:



# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.4, wspace=0.4)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# scatter points on the main axes
main_ax.plot(diamonds.x, diamonds.carat, 'ok', markersize=3, alpha=0.2)

# histogram on the attached axes
x_hist.hist(diamonds.x, 40, histtype='stepfilled',
            orientation='vertical', color='gray')
x_hist.invert_yaxis()
x_hist.set_xlabel("Width (x) in mm")

y_hist.hist(diamonds.carat, 40, histtype='stepfilled',
            orientation='horizontal', color='gray')
y_hist.invert_xaxis()
y_hist.set_xlabel("carat")
plt.show()


# #### Customizing Matplotlib: Configurations and Stylesheets

# In[ ]:


x = np.random.randn(1000)
plt.hist(x)
plt.show()


# In[ ]:


# use a gray background
ax = plt.axes(facecolor='#E6E6E6')

# draw solid white grid lines
plt.grid(color='w', linestyle='solid', visible=True, lw=1)

# hide axis spines
for spine in ax.spines.values():
    spine.set_visible(False)

ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# lighten ticks and labels
ax.tick_params(colors='k', direction='out',length=4, width=2)
for tick in ax.get_xticklabels():
    tick.set_color('gray')
for tick in ax.get_yticklabels():
    tick.set_color('gray')
    
# control face and edge color of histogram
ax.hist(x, edgecolor='r', color='#EEAA66');
plt.show()


# In[ ]:


y = np.random.randn(2000)+2
plt.hist(y,bins=50)
plt.show()


# In[ ]:


colors = mpl.cycler('color',
                ['EEAA66b1', '3388BBb1', '9988DDb1',
                 'EECC55b1', '88BB44b1', 'FFBBBBb1'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
       axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')

plt.rc('xtick', direction='out', color='k')
plt.rc('ytick', direction='out', color='k')
plt.rc('xtick.major', size=2,width=4,top=False)
plt.rc('ytick.major', size=8,width=2,right=False)

plt.rc('patch', edgecolor='r')
plt.rc('lines', linewidth=1)


# In[ ]:


plt.hist(y,bins=50)
plt.hist(x)
plt.show()


# In[ ]:


for i in range(4):
    plt.plot(np.random.rand(10))


# In[ ]:


def hist_and_lines():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(['a', 'b', 'c'], loc='lower left')


# In[ ]:


my_params = plt.rcParams.copy()
plt.rcParams.update(plt.rcParamsDefault)


# In[ ]:


hist_and_lines()


# In[ ]:


plt.rcParams.update(my_params)


# In[ ]:


hist_and_lines()


# In[ ]:


with plt.style.context('fivethirtyeight'):
    hist_and_lines()


# In[ ]:


hist_and_lines()


# In[ ]:


with plt.style.context('ggplot'):
    hist_and_lines()


# In[ ]:


with plt.style.context('dark_background'):
    hist_and_lines()


# ### Geographic Data with Basemap
# One common type of visualization in data science is that of geographic data. Matplotlib's main tool for this type of visualization is the Basemap toolkit, which is one of several Matplotlib toolkits which lives under the mpl_toolkits namespace. Admittedly, Basemap feels a bit clunky to use, and often even simple visualizations take much longer to render than you might hope.

# In[ ]:


get_ipython().system('conda install -y basemap')
import os
os.environ["PROJ_LIB"]='/srv/conda/envs/notebook/lib/python3.7/site-packages/mpl_toolkits/basemap'
from mpl_toolkits.basemap import Basemap
plt.rcParams.update(plt.rcParamsDefault)


# In[ ]:


fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            width=8E6, height=8E6, 
            lat_0=45, lon_0=-100,)
m.etopo(scale=0.5, alpha=0.5)

# Map (long, lat) to (x, y) for plotting
x, y = m(-122.3, 47.6)
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, ' Seattle', fontsize=12);


# In[ ]:


sorted_cities=cities.sort_values('area_total_km2',ascending=False).dropna()
to_plot = pd.concat([sorted_cities.head(10),sorted_cities.tail(10)])[['city','latd','longd']]
to_plot


# In[ ]:


# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='c', 
            lat_0=37.5, lon_0=-119,
            width=1E6, height=1.2E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

# 2. scatter city data, with color reflecting population
# and size reflecting area
m.scatter(lon, lat, latlon=True,
          c=np.log10(population), s=area,
          cmap='Reds', alpha=0.5)

# 3. create colorbar and legend
plt.colorbar(label=r'$\log_{10}({\rm population})$')
plt.clim(3, 7)

# Map (long, lat) to (x, y) for plotting
for i,r in to_plot.iterrows():
    x, y = m(r['longd'],r['latd'])
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, " "+r['city'], fontsize=8);
# make legend with dummy points
for a in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.5, s=a,
                label=str(a) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, loc='lower left');


# ### Visualization with Seaborn
# Matplotlib's API is relatively low level. Doing sophisticated statistical visualization is possible, but often requires a lot of boilerplate code. Seaborn provides a convenience API on top of Matplotlib, and is well integrated with Pandas `Dataframe`s.

# In[ ]:


rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)


# In[ ]:


plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');


# In[ ]:


sns.set() # set rcparams for matplotlib
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');


# In[ ]:


data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col],  alpha=0.5)


# In[ ]:


for col in 'xy':
    sns.kdeplot(data[col], shade=True) #kernel density estimation


# In[ ]:


sns.histplot(data['x'],kde=True)
sns.histplot(data['y'],kde=True)


# In[ ]:


with sns.axes_style('white'):
    sns.jointplot(x="x", y="y",data=data, kind='hex');


# #### Pair plots
# When you generalize joint plots to datasets of larger dimensions, you end up with pair plots. This is very useful for exploring correlations between multidimensional data, when you'd like to plot all pairs of values against each other.
# 
# We'll demo this with the well-known Iris dataset, which lists measurements of petals and sepals of three iris species:

# In[ ]:


iris = sns.load_dataset("iris")
iris.head()


# In[ ]:


sns.pairplot(iris, hue='species')


# In[ ]:


titanic = pd.read_csv('titanic.csv', index_col='PassengerId')
titanic.drop(['Name','Ticket'],axis=1,inplace=True)
titanic.head(10)


# In[ ]:


grid = sns.FacetGrid(titanic, row="Sex", col="Pclass", margin_titles=True)
grid.map(plt.hist, "Age", bins=np.linspace(0, 80, 15));


# In[ ]:


tips = sns.load_dataset('tips')
tips.head()


# In[ ]:


with sns.axes_style(style='ticks'):
    g = sns.catplot(x="day", y="total_bill", hue="sex", data=tips, kind="box") #categorical plot
    g.set_axis_labels("Day", "Total Bill");


# ### Example: Exploring Marathon Finishing Times
# https://raw.githubusercontent.com/jakevdp/marathon-data/master/marathon-data.csv

# In[ ]:


data = pd.read_csv('marathon-data.csv')
data.head()


# By default, Pandas loaded the time columns as Python strings (type ``object``); we can see this by looking at the ``dtypes`` attribute of the DataFrame:

# In[ ]:


data.dtypes


# In[ ]:


import datetime

def convert_time(s):
    h, m, s = map(int, s.split(':'))
    return datetime.timedelta(hours=h, minutes=m, seconds=s)

data = pd.read_csv('marathon-data.csv',
                   converters={'split':convert_time, 'final':convert_time})
data.head()


# In[ ]:


data.dtypes


# For the purpose of our Seaborn plotting utilities, let's next add columns that give the times in seconds:

# In[ ]:


data['split_sec'] = data['split'].astype(int) / 1E9
data['final_sec'] = data['final'].astype(int) / 1E9
data.head()


# To get an idea of what the data looks like, we can plot a jointplot over the data:

# In[ ]:


with sns.axes_style('white'):
    g = sns.jointplot(x="split_sec", y="final_sec", data=data, kind='scatter')
    g.ax_joint.plot(np.linspace(4000, 16000),
                    np.linspace(8000, 32000), ':k')


# *The dotted line shows where someone's time would lie if they ran the marathon at a perfectly steady pace. The fact that the distribution lies above this indicates (as you might expect) that most people slow down over the course of the marathon. If you have run competitively, you'll know that those who do the opposite—run faster during the second half of the race—are said to have "negative-split" the race.*
# 
# *Let's create another column in the data, the split fraction, which measures the degree to which each runner negative-splits or positive-splits the race:*

# In[ ]:


data['split_frac'] = 1 - 2 * data['split_sec'] / data['final_sec']
data.head()


# In[ ]:


sns.displot(data['split_frac'], kde=False,bins=40);
plt.axvline(0, color="k", linestyle="--");


# In[ ]:


sum(data.split_frac < 0)


# *Out of nearly 40,000 participants, there were only 250 people who negative-split their marathon.*
# 
# *Let's see whether there is any correlation between this split fraction and other variables. We'll do this using a pairgrid, which draws plots of all these correlations:*

# In[ ]:


g = sns.PairGrid(data, vars=['age', 'split_sec', 'final_sec', 'split_frac'],
                 hue='gender', palette='RdBu_r')
g.map(plt.scatter, alpha=0.8)
g.add_legend()


# It looks like the split fraction does not correlate particularly with age, but does correlate with the final time: faster runners tend to have closer to even splits on their marathon time.

# The difference between men and women here is interesting. Let's look at the histogram of split fractions for these two groups:

# In[ ]:


data.groupby('gender').count()['age']


# In[ ]:


sns.kdeplot(data.split_frac[data.gender=='M'], label='men', shade=True)
sns.kdeplot(data.split_frac[data.gender=='W'], label='women', shade=True)
plt.xlabel('split_frac')
plt.legend()


# The interesting thing here is that there are many more men than women who are running close to an even split.
# 

# In[ ]:


sns.violinplot(x="gender", y="split_frac", data=data,
               palette=["lightblue", "lightpink"]);


# This is yet another way to compare the distributions between men and women.
# 
# Let's look a little deeper, and compare these violin plots as a function of age. We'll start by creating a new column in the array that specifies the decade of age that each person is in:

# In[ ]:


data['age_dec'] = data.age.map(lambda age: 10 * (age // 10))
data.head()


# In[ ]:



with sns.axes_style(style=None):
    sns.violinplot(x="age_dec", y="split_frac", hue="gender", data=data,
                   split=True, inner="quartile",
                   palette=["lightblue", "lightpink"]);


# Looking at this, we can see where the distributions of men and women differ: the split distributions of men in their 20s to 50s show a pronounced over-density toward lower splits when compared to women of the same age (or of any age, for that matter).
# 
# Also surprisingly, the 80-year-old women seem to outperform everyone in terms of their split time. This is probably due to the fact that we're estimating the distribution from small numbers, as there are only a handful of runners in that range:

# In[ ]:


(data.age > 80).sum()


# In[ ]:





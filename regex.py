#!/usr/bin/env python
# coding: utf-8

# # Regular Expressions
# Regular expressions, dubbed RegEx, is a sequence of characters that form a search pattern. Commonly used when extracting data from text or working with string data. RegEx can be used to check if a string matches or contains a specified pattern.<br>
# Python's built in RegEx package is called `re`.

# In[ ]:


import re


# In[ ]:


txt = "Scientific Programming in Python"
x = re.search("P",txt)
print(x)


# In[ ]:


print(x.start(), x.end())


# In[ ]:


y = re.search("Z",txt)
print(y)


# In[ ]:


z=re.findall("P",txt)
print(z)


# In[ ]:


z=re.findall("Z",txt)
print(z)


# In[ ]:


s = re.sub("i","e",txt,2)
print(s)


# In[ ]:


print(txt)
m = re.finditer(re.compile("i"),txt)
for i in m:
    print(i)


# In[ ]:


html = """<li id="menu-item-899746" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-899746"><a href="https://techcrunch.com/mobile/">Mobile</a></li>
<li id="menu-item-899747" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-899747"><a href="https://techcrunch.com/gadgets/">Gadgets</a></li>
<li id="menu-item-899748" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-899748"><a href="https://techcrunch.com/enterprise/">Enterprise</a></li>
<li id="menu-item-899749" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-899749"><a href="https://techcrunch.com/social/">Social</a></li>
<li id="menu-item-899750" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-899750"><a href="https://techcrunch.com/europe/">Europe</a></li>
<li id="menu-item-901944" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-901944"><a href="/asia">Asia</a></li>
<li id="menu-item-1266871" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1266871"><a href="https://techcrunch.com/crunch-network/">Crunch Network</a></li>
<li id="menu-item-1210304" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1210304"><a href="https://techcrunch.com/unicorn-leaderboard/">Unicorn Leaderboard</a></li>
<li id="menu-item-1242803" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1242803"><a href="https://techcrunch.com/gifts/">Gift Guides</a></li>"""


# In[ ]:


html


# In[ ]:


anchors = re.finditer("<a.*>",html)
for a in anchors:
    print(a.group())


# #### RegEx is greedy and will keep searching for a match until it reaches the end of a line. We need so be very clear on exactly which pattern we wish to match.

# In[ ]:


anchors = re.finditer("<a.*?>",html)
for a in anchors:
    print(a.group())


# ###### here we search for a `<a` followed by any number of characters up until the first `>`

# In[ ]:


html


# In[ ]:


menu = re.finditer('menu(-[^\s"]*)[\s"]',html) #\s = whitespaces (\t, \r, \n, space characters)
for m in menu:
    print(m.group(1))


# In[ ]:


menu = re.finditer('menu(-[^\s"]*)-(?P<num>\d+)',html)
for m in menu:
    print(m.group("num"))


# In[ ]:


menu = re.finditer(r'((menu(-[^\s"]*)-(?P<num>\d+)).*\2)',html)
results = []
for m in menu:
    results.append(m)
    print(m.groups())


# In[ ]:


print(results[0].groups())
print(results[0].group()) # default is 0 - the entire pattern match
print(results[0].group(0)) # group 0 is the entire pattern match
print(results[0].group(1)) # the first user defined group in parentheses


# In[ ]:


import csv


# In[ ]:


with open("sea-ice.csv") as file:
    reader = csv.DictReader(file)
    for i,entry in enumerate(reader):
        print(dict(entry))
        if (i>9):
            break


# In[ ]:


data=[]
with open("sea-ice.csv") as file:
    reader = csv.DictReader(file)
    for entry in reader:
        tmp={}
        for key in entry.keys():
            tmp[key.strip()]=entry[key].strip()
        tmp['Extent']=float(tmp['Extent'])
        data.append(tmp)
for d in data[0:9]:
    print(d)
for d in data[-10:]:
    print(d)


# In[ ]:


print(data[-1])


# #### We would like to create a new data set which containst the date, extent, dataset name and hemisphere for each row
# We will start by turning "Source Data" into a python list. Lists are valid JSON objects, so we will use the `json.loads()` function

# In[ ]:


import json


# In[ ]:


s = data[0]["Source Data"].replace("'",'"')
print(type(s),s)
j = json.loads(s)
print(type(j), j)


# In[ ]:


def parseList(s):
    return json.loads(s.replace("'",'"'))


# In[ ]:


len(data)


# In[ ]:


newData = []
for i,d in enumerate(data):
    sources = parseList(d["Source Data"])
    for src in sources:
        tmp = dict(d)
        del tmp["Source Data"]
        tmp["src"] = src
        newData.append(tmp)


# In[ ]:


len(newData)


# In[ ]:


for d in newData[0:9]:
    print(d)
for d in newData[-10:]:
    print(d)


# #### We will create a RegEx to extract the dataset name and date from each src

# In[ ]:


pDataset = "(nsidc\d*)"
pDate = "(\d{8})[-_]"


# ## The datetime object

# In[ ]:


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A")) #print day of week
print(x.strftime("%B")) #print month


# *The datetime constructor accepts parameters in the following order: year, month, day, hour, minute, second, microsecond*

# In[ ]:


birthday = datetime.datetime(1983,9,9,17)
print(birthday)


# *We can also create a datetime object from a string by defining the format the string represents*

# In[ ]:


dt = datetime.datetime.strptime("20000412","%Y%m%d")
print(dt)


# **We can now complete our new data set**

# In[ ]:


print(re.search(pDate,newData[0]['src']).groups(1)[0])
print(re.search(pDataset,newData[0]['src']).groups(1)[0])


# In[ ]:


for d in newData:
    src = d['src']
    date = re.search(pDate,src).groups(1)[0]
    dataset = re.search(pDataset,src).groups(1)[0]
    d['Date'] = str(datetime.datetime.strptime(date,"%Y%m%d"))
    d['Dataset'] = dataset
    del d['src']


# In[ ]:


for d in newData[0:9]:
    print(d)
for d in newData[-10:]:
    print(d)


# In[ ]:


fieldnames = [key for key in newData[0].keys()]
print(fieldnames)


# *We want to re-order the list so the columns will be: Date,Dataset,hemisphere,Extent*

# In[ ]:


order = [2,3,1,0]
fieldnames = [fieldnames[i] for i in order]
print(fieldnames)


# In[ ]:


with open('sea-ice-fixed.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in newData:
        writer.writerow(entry)


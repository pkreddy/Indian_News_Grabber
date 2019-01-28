#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from lxml import html
from bs4 import BeautifulSoup
import datetime


# In[2]:


url = "https://inshorts.com/sitemap-en.xml"
page = requests.get(url)
tree = html.fromstring(page.content)


# In[3]:


count = len(tree.xpath("//url"))
raw_urls = []


# In[4]:


str(tree.xpath("//url[2]/loc/text()")).replace("['","").replace("']","")


# In[5]:


for i in range(1,count+1):
    raw_urls.append(str(tree.xpath("//url["+str(i)+"]/loc/text()")).replace("['","").replace("']",""))


# In[6]:


k = []
v = []
for i in range(1,count+1):
    #l = str(tree.xpath("//url["+i+"]/loc/text()")).replace("['","").replace("']","").count("-")
    #str(tree.xpath("//url[2]/loc/text()")).replace("['","").replace("']","").split("-")[:l]
    k.append(int(str(tree.xpath("//url["+str(i)+"]/loc/text()")).replace("['","").replace("']","").split("-")[-1]))
    v.append(str(tree.xpath("//url["+str(i)+"]/loc/text()")).replace("['","").replace("']",""))


# In[7]:


dict_url = {k[i]:v[i] for i in range(count)}


# In[8]:


#dict_url_pandas = pd.DataFrame.from_dict(dict_url, orient='index')
dict_url_pandas = pd.DataFrame(list(dict_url.items()), columns=['news_id','news_url'])


# In[9]:


dict_url_pandas.head()


# In[10]:


temp = pd.read_csv('inshorts_url.csv')
news_url_set = set(temp['news_url'])


# In[11]:


temp.head()


# In[12]:


dict_url_pandas_set = set(dict_url_pandas['news_url'])


# In[13]:


pd.DataFrame(list((dict_url_pandas_set | news_url_set)), columns=['news_url']).to_csv('inshorts_url.csv', index=False)


# In[14]:


if len(dict_url_pandas_set - news_url_set) > 0:
    pd.DataFrame(list((dict_url_pandas_set - news_url_set)), columns=['news_url']).to_csv('inshorts_new_url.csv', index=False)


# In[15]:


temp.news_url[2001]


# In[16]:


temp = pd.read_csv('inshorts_url.csv')
temp.size


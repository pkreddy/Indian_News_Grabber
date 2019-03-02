#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from lxml import html
from bs4 import BeautifulSoup
import datetime


# In[2]:


proxy = {
            "http":"http://45.64.11.1:8080",
            "http":"http://125.62.213.161:83",
            "http":"http://103.218.101.113:8080",
            "http":"http://103.253.211.182:8080",
            "http":"http://103.46.233.21:83",
            "http":"http://103.46.233.27:82",
            "http":"http://175.101.80.145:8080",
            "http":"http://175.101.80.140:8080",
            "http":"http://123.108.200.118:83",
            "http":"http://103.26.56.30:8080",
            "http":"http://103.226.3.233:8080",
            "http":"http://103.41.99.130:8080",
            "http":"http://103.224.48.17:8080",
            "http":"http://103.209.64.19:6666",
            "http":"http://103.14.235.26:8080",
        }


# In[3]:


url = "https://inshorts.com/sitemap-en.xml"
page = requests.get(url,proxies=proxy)
tree = html.fromstring(page.content)


# In[4]:


count = len(tree.xpath("//url"))
raw_urls = []


# In[5]:


str(tree.xpath("//url[2]/loc/text()")).replace("['","").replace("']","")


# In[6]:


for i in range(1,count+1):
    raw_urls.append(str(tree.xpath("//url["+str(i)+"]/loc/text()")).replace("['","").replace("']",""))


# In[7]:


k = []
v = []
for i in range(1,count+1):
    #l = str(tree.xpath("//url["+i+"]/loc/text()")).replace("['","").replace("']","").count("-")
    #str(tree.xpath("//url[2]/loc/text()")).replace("['","").replace("']","").split("-")[:l]
    k.append(int(str(tree.xpath("//url["+str(i)+"]/loc/text()")).replace("['","").replace("']","").split("-")[-1]))
    v.append(str(tree.xpath("//url["+str(i)+"]/loc/text()")).replace("['","").replace("']",""))


# In[8]:


dict_url = {k[i]:v[i] for i in range(count)}


# In[9]:


#dict_url_pandas = pd.DataFrame.from_dict(dict_url, orient='index')
dict_url_pandas = pd.DataFrame(list(dict_url.items()), columns=['news_id','news_url'])


# In[10]:


dict_url_pandas.head()


# In[11]:


temp = pd.read_csv('inshorts_url.csv')
news_url_set = set(temp['news_url'])


# In[12]:


temp.head()


# In[13]:


dict_url_pandas_set = set(dict_url_pandas['news_url'])


# In[14]:


pd.DataFrame(list((dict_url_pandas_set | news_url_set)), columns=['news_url']).to_csv('inshorts_url.csv', index=False)


# In[15]:


if len(dict_url_pandas_set - news_url_set) > 0:
    pd.DataFrame(list((dict_url_pandas_set - news_url_set)), columns=['news_url']).to_csv('inshorts_new_url.csv', index=False)


# In[16]:


temp.news_url[2001]


# In[17]:


temp = pd.read_csv('inshorts_url.csv')
temp.size



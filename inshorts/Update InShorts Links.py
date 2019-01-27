#!/usr/bin/env python
# coding: utf-8

# In[62]:


import requests
import pandas as pd
from lxml import html
from bs4 import BeautifulSoup
import datetime


# In[63]:


url = "https://inshorts.com/sitemap-en.xml"
page = requests.get(url)
tree = html.fromstring(page.content)


# In[64]:


count = len(tree.xpath("//url"))
raw_urls = []


# In[65]:


str(tree.xpath("//url[2]/loc/text()")).replace("['","").replace("']","")


# In[66]:


for i in range(1,count+1):
    raw_urls.append(str(tree.xpath("//url["+str(i)+"]/loc/text()")).replace("['","").replace("']",""))


# In[67]:


k = []
v = []
for i in range(1,count+1):
    #l = str(tree.xpath("//url["+i+"]/loc/text()")).replace("['","").replace("']","").count("-")
    #str(tree.xpath("//url[2]/loc/text()")).replace("['","").replace("']","").split("-")[:l]
    k.append(int(str(tree.xpath("//url["+str(i)+"]/loc/text()")).replace("['","").replace("']","").split("-")[-1]))
    v.append(str(tree.xpath("//url["+str(i)+"]/loc/text()")).replace("['","").replace("']",""))


# In[68]:


dict_url = {k[i]:v[i] for i in range(count)}


# In[69]:


#dict_url_pandas = pd.DataFrame.from_dict(dict_url, orient='index')
dict_url_pandas = pd.DataFrame(list(dict_url.items()), columns=['news_id','news_url'])


# In[70]:


dict_url_pandas.head()


# In[71]:


temp = pd.read_csv('inshorts_url.csv')
news_url_set = set(temp['news_url'])


# In[72]:


temp.head()


# In[73]:


dict_url_pandas_set = set(dict_url_pandas['news_url'])


# In[56]:


pd.DataFrame(list((dict_url_pandas_set | news_url_set)), columns=['news_url']).to_csv('inshorts_url.csv', index=False)


# In[57]:


pd.DataFrame(list((dict_url_pandas_set - news_url_set)), columns=['news_url']).to_csv('inshorts_new_url.csv', index=False)


# In[60]:


temp.news_url[2001]


# In[61]:


temp = pd.read_csv('inshorts_url.csv')
temp.size


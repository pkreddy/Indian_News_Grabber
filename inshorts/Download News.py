#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import pandas as pd
from lxml import html
from bs4 import BeautifulSoup
import datetime
import os


# In[2]:


def clean_xpath(xpath):
    xpath = str(xpath).replace('["','').replace('"]','')
    xpath = str(xpath).replace("['","").replace("']","")
    return xpath


# In[3]:


def proxy_list():
    url = 'https://www.proxynova.com/proxy-server-list/country-in/'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    proxy_list = tree.xpath('//abbr')
    proxy = []
    for i in proxy_list:
        p = i.get('title')
        if len(p)<16:
            proxy.append(p)
    return proxy    


# In[4]:


def get_news(news_url, proxy):
    page = requests.get(news_url, proxies=proxy)
    tree = html.fromstring(page.content)
    headline = clean_xpath(tree.xpath("/html/body/div[4]/div/div[3]/div/div/div[2]/a/span/text()"))
    author = clean_xpath(tree.xpath("/html/body/div[4]/div/div[3]/div/div/div[2]/div/span[1]/text()"))
    time = clean_xpath(tree.xpath("/html/body/div[4]/div/div[3]/div/div/div[2]/div/span[2]/text()"))
    date = clean_xpath(tree.xpath("/html/body/div[4]/div/div[3]/div/div/div[2]/div/span[3]/text()"))
    date = "-".join(date.split(",")[0].split())
    body = clean_xpath(tree.xpath("/html/body/div[4]/div/div[3]/div/div/div[3]/div[1]/text()"))
    news_from_source = clean_xpath(tree.xpath("/html/body/div[4]/div/div[3]/div/div/div[4]/div/a/text()"))
    news = (news_url,headline,body,author,time,date,news_from_source)
    return news


# In[15]:


temp = pd.read_csv('inshorts_new_url.csv')
temp.head()


# In[6]:


temp.news_url.iloc[2]


# In[7]:


l = []
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


# In[9]:


for i in range(len(temp)):
    l.append(get_news(temp.news_url.iloc[i],proxy))


# In[16]:


news_total = pd.DataFrame.from_records(l, columns=['url','headline','body','author','time','date','source'])
news_total.to_csv('news_inshorts.csv', index = False, mode = a)


# In[17]:


news_total = pd.read_csv('news_inshorts.csv')
#news_total = news_total.drop(news_total.columns[[0]], axis=1)


# In[18]:


news_total.head()


# In[4]:


myfile = "F:\GitHub\Indian_News_Grabber\inshorts\inshorts_new_url.csv"
if os.path.isfile(myfile):
    os.remove(myfile)


# In[ ]:





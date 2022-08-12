#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


response = requests.get("https://www.thepilot.com/news/pets/")
data = BeautifulSoup(response.text)


# In[3]:


data.find(class_= 'panel-body')


# In[5]:


for pet in data.find_all(class_= 'panel-body'):
    #img = pet.select_one("img[data-srcset]").attrs['data-srcset'].split(',')[0]
    img = pet.img['data-srcset'].split(",")[0].rstrip('1234567890w')
    if img == False:
        pass
    else:
        print(pet.text.strip())
        print(img)
    print("----")


# In[6]:


for pet in data.find_all(class_= 'panel-body'):
    info = pet.text.strip()
    img = pet.img
    if img == None:
        print(info)
    else:
        print(info)
        print(img.attrs['data-srcset'].split(",")[0].rstrip("12345567890W"))
    print("----")


# In[7]:


for pet in data.find_all(class_= 'panel-body'):
    info = pet.text.strip()
    img = pet.img
    if img == None:
        print(info)
    else:
        print(info)
        print(img.attrs['data-srcset'].split(",")[0].rstrip("12345567890w"))
    print("----")


# In[30]:


pets_southern_pines = []


for pet in data.find_all(class_= 'panel-body'):
    pet_indiv = {}
    info = pet.text.strip()
    img = pet.img
    if img == None:
        print(info)
    else:
        pet_indiv['info'] = pet.text.strip()
        pet_indiv['image_url'] = img.attrs['data-srcset'].split(",")[0].rstrip("12345567890w")
        pet_indiv['url'] = 'https://www.thepilot.com' + pet.a['href']
        pets_southern_pines.append(pet_indiv)


# In[27]:


import pandas as pd


# In[31]:


pets_southern_pines = pd.DataFrame(pets_southern_pines)


# In[32]:


pets_southern_pines


# In[33]:


pets_southern_pines.to_csv('pets-of-southern-pines.csv', index= False)


# In[ ]:





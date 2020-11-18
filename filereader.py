#!/usr/bin/env python
# coding: utf-8

# In[40]:


import os
files = os.listdir()
print(files)
pointfile = open("pointlist.txt", "w")
for i in files:
    if i.lower().endswith(".txt"):
        file = open(i, "r")
for text in file:
    if "Points" in text or "POINTS" in text or "points" in text:
        print(text)
        pointfile.write(text)
file.close()
pointfile.close()


# In[ ]:





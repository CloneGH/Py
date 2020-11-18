#!/usr/bin/env python
# coding: utf-8

# In[40]:


txtfile = input("type in the file name you want to copy parts of: ")
newfile = input("type in a new file name: ")
txtwrite = open(newfile, "w")
file = open(txtfile, "r")
for text in file:
    if "word" in text:
        print(text)
        txtwrite.write(text)
file.close()
txtwrite.close()


# In[ ]:





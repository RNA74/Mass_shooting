#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np
import os
working_directory = os.getcwd()
print (working_directory)


# In[47]:


path = working_directory + '/Mother_Jones_MassShootings.csv'
df = pd.read_csv(path)
df.head()


# In[48]:


#Droping columns
new_df=df.drop(columns=['case','summary','sources','mental_health_details','where_obtained','weapon_details','mental_health_sources'])
new_df.head()


# In[49]:


#Replacing values
Shooting_df=new_df.replace(to_replace=['white', 'black', 'other','yes','workplace','religious'], value=['White', 'Black', 'Other','Yes','Workplace','Religious'])
Shooting_df.head()


# In[50]:


#Replacing values
Mass_Shootind_df= Shooting_df.replace(to_replace=['TK','(TK - "fewer than 10"'], value=[4,0])
Mass_Shootind_df.head(20)


# In[51]:


#Renaming columns
Mass_Shootind_df.rename(columns = {'location.1':'Place'},inplace=True)
Mass_Shootind_df.head(145)


# In[55]:


#Spliting data into two columns
Mass_Shootind_df = df ['location'].str.split(',', n=1,expand=True).rename(columns={0:'City', 1:'State'})
                                                               
Mass_Shootind_df.head()


# In[56]:


#Spliting data into two columns
Mass_Shootind_df= df ['weapon_type'].str.split(',',n=1,expand=True).rename(columns={0:'weapon_1', 1:'weapon_2'})
Mass_Shootind_df.head(145)


# In[57]:


Mass_Shootind_df.to_excel('/Users/rnababikar/Downloads/MassShooting_Last.xlsx', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





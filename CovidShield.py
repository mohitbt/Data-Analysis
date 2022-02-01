#!/usr/bin/env python
# coding: utf-8

# In[145]:


get_ipython().system('pip install plotly')


# In[148]:


import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[133]:


covid_df=pd.read_csv("C:/Users/MOHIT/OneDrive/Desktop/india/covid_19_india.csv")


# In[8]:


covid_df.head(10)


# In[9]:


covid_df.info()


# In[10]:


covid_df.describe()


# In[11]:


vaccine_df=pd.read_csv("C:/Users/MOHIT/OneDrive/Desktop/india/covid_vaccine_statewise.csv")


# In[17]:


covid_df.drop(["Sno","Time","ConfirmedIndianNational","ConfirmedForeignNational"],inplace=True,axis=1)
   


# In[18]:


covid_df.head()


# In[19]:


covid_df['Date']=pd.to_datetime(covid_df['Date'],format="%Y-%m-%d")


# In[20]:


covid_df.head()


# In[21]:


#Active cases
covid_df['Active_Cases']=covid_df['Confirmed']-(covid_df['Cured']+covid_df['Deaths'])


# In[23]:


statewise=pd.pivot_table(covid_df,values=["Confirmed","Deaths","Cured"],index="State/UnionTerritory",aggfunc=max)


# In[25]:


statewise["Rcovery Rate"]=statewise["Cured"]*100/statewise["Confirmed"]


# In[27]:


statewise["Rcovery Rate"]=statewise["Deaths"]*100/statewise["Confirmed"]


# In[28]:


statewise=statewise.sort_values(by="Confirmed",ascending=False)


# In[29]:


statewise.style.background_gradient(cmap="cubehelix")


# In[35]:


# Top 10 Active cases states



top_10_active_cases=covid_df.groupby(by='State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by=['Active_Cases'],ascending=False).reset_index()


# In[36]:


fig=plt.figure(figsize=(16,9))


# In[37]:


plt.title("Top 10 states with most active Cases In India",size=25)


# In[41]:


ax=sns.barplot(data=top_10_active_cases.iloc[:10],y="Active_Cases",x="State/UnionTerritory",linewidth=2,edgecolor='red')


# In[45]:


top_10_active_cases=covid_df.groupby(by='State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by=['Active_Cases'],ascending=False).reset_index()
fig=plt.figure(figsize=(16,9))
plt.title("Top 10 states with most active Cases In India",size=25)
ax=sns.barplot(data=top_10_active_cases.iloc[:10],y="Active_Cases",x="State/UnionTerritory",linewidth=2,edgecolor='red')
plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show()


# In[49]:


# Top states with highst deaths
top_10_deaths=covid_df.groupby(by='State/UnionTerritory').max()[['Deaths','Date']].sort_values(by=['Deaths'],ascending=False).reset_index()
fig=plt.figure(figsize=(18,5))
plt.title("Top 10 states with most Deaths",size=25)
ax=sns.barplot(data=top_10_deaths.iloc[:12],y="Deaths",x="State/UnionTerritory",linewidth=2,edgecolor='black')
plt.xlabel("States")
plt.ylabel("Total Death Cases")
plt.show()


# In[112]:


#Growth trend
#fig=plt.figure(figsize=(12,6))
#l=covid_df['State/UnionTerritory'].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu','Uttar Pardesh']) 
#ax=sns.lineplot(data=covid_df[l])

#ax.set_title("Top 5 Affected States in  india",size=16)


# In[113]:


vaccine_df.head()


# In[114]:


vaccine_df.rename(columns={'Updated':'vaccine_Date'},inplace=True)


# In[115]:


vaccine_df.head(10)


# In[116]:


vaccine_df.info()


# In[118]:


vaccine_df.isnull().sum()


# In[121]:


vaccination=vaccine_df.drop(columns=['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years(Individuals Vaccinated)','60+ Years(Individuals Vaccinated)'],axis=1)


# In[122]:


vaccination.head()


# In[149]:


# Male vs Female vaccination
male=vaccination["Male(Individuals Vaccinated)"].sum()
female=vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=["Male","Female"],values=[male,female],title="Male and Female Vaccination")


# In[150]:


#Remove rows where state=India
vaccine=vaccine_df[vaccine_df.State!='India']
vaccine


# In[169]:


vaccine.rename(columns={"Total Individuals vaccinated":"Total"},inplace=True)
vaccine.head()


# In[170]:


#Most vaccinated State

max_vac=vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac=max_vac.sort_values('Total',ascending=False)[:5]
max_vac


# In[173]:


fig=plt.figure(figsize=(10,5))
plt.title("Top 5 Vaccinated States in India",size=20)
x=sns.barplot(data=max_vac.iloc[:10],y=max_vac.Total,x=max_vac.index,linewidth=2,edgecolor='black')

plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()


# In[ ]:





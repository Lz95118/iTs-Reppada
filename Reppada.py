#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# load the data into pandas dataframes
demographic_data  = pd.read_excel("Table 1.xlsx")
genitive_plurals   = pd.read_excel("Table 2.xlsx")

demographic_data.head()


# In[3]:


# extract the 'nid' column from 'speaker' column of table_1
demographic_data['Nid'] = demographic_data['Speaker'].str.split('\\').str[-1]

# drop the 'Speaker' column since it's no longer needed
demographic_data.drop(columns=['Speaker'],inplace=True)


# In[4]:


# Check for missing values in demographic_data
missing_values = demographic_data.isnull().sum()
print(missing_values)

# Check for missing values in genitive_plurals
missing_values = genitive_plurals.isnull().sum()
print(missing_values)


# In[5]:


# Check the tables
print(demographic_data)
print(genitive_plurals)


# In[6]:


# merge the two tables on the 'Mid' column
merged_table = pd.merge(demographic_data, genitive_plurals, on='Nid')


# In[7]:


merged_table


# In[8]:


# Compute summary statistics for age
age_summary = merged_table['Age'].describe()
print(age_summary)

# Compute summary statistics for the number of times each form was used
form_counts = merged_table.iloc[:, -10:-1].sum()
form_summary = form_counts.describe()
print(form_summary)

# Plot a histogram of age
plt.hist(merged_table['Age'])
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot a histogram of Religion
plt.hist(merged_table['Religion'])
plt.title('Religion Distribution')
plt.xlabel('Religion')
plt.ylabel('Frequency')
plt.show()


# Plot a bar chart of gender
gender_counts = merged_table['Gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[9]:


# Calculate the correlation matrix
corr_matrix = merged_table.iloc[:, -10:-1].corr()

# Plot a heatmap of the correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[10]:


# Group by gender and calculate the sum of counts for each form
gender_counts = merged_table.groupby('Gender')[['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7']].sum()

# Plot a bar chart of the counts by gender
gender_counts.plot(kind='bar')
plt.title('Counts by Gender')
plt.xlabel('Form')
plt.ylabel('Count')
plt.show()


# In[11]:


# Group by Religion and calculate the sum of counts for each form
Religion_counts = merged_table.groupby('Religion')[['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7']].sum()

# Plot a bar chart of the counts by Religion
Religion_counts.plot(kind='bar')
plt.title('Counts by Religion')
plt.xlabel('Form')
plt.ylabel('Count')
plt.show()


# In[12]:


# Group by Length of interview and calculate the sum of counts for each form
Length_counts = merged_table.groupby('Length of interview ( 1 =less 30 min, 2 = 30 min to 1 hour,3=1 hour to 2 hours, 4=over two hours)')[['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7']].sum()

# Plot a bar chart of the counts by Length of interview
Length_counts.plot(kind='bar')
plt.title('Counts by Length of interview')
plt.xlabel('Form')
plt.ylabel('Count')
plt.show()


# In[13]:


# Group by Length of interview and calculate the sum of counts for each form
Village_counts = merged_table.groupby('Village')[['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7']].sum()

# Plot a bar chart of the counts by Length of interview
Village_counts.plot(kind='bar')
plt.title('Village')
plt.xlabel('Form')
plt.ylabel('Count')
plt.show()


# In[ ]:





# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 20:56:19 2022

@author: unpat
"""

import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')


#pd.set_option('max_rows', 99999)
#pd.set_option('max_colwidth', 400)
#pd.describe_option('max_colwidth')


data_dir_path = os.path.dirname(__file__)
#data_dir_path = os.path.dirname(os.path.abspath("__file__"))
data_url = os.path.join(data_dir_path, 'glassdoor_jobs.csv')
df = pd.read_csv(data_url)
#df = pd.read_csv('glassdoor_jobs.csv')


# salary parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
# print(len(df))

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))  # removing $ sign

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2


# company name text only

df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1) 


# state field

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


# age of company

df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2022 - x)


# parsing of job description (Python, etc.)

# Python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

# r studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

# spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

# aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

# excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('salary_data_cleaned.csv', index = False)































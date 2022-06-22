# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:11:27 2022

@author: unpat
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/unpat/_Projects/ds_salary_proj/geckodriver"

#df = gs.get_jobs('Data Scientist', 'Chicago', 2, False, path, 5)


df = gs.get_jobs('data scientist', 3, False, path, 5)


#path = "chromedriver"
#df = gs.get_jobs('data scientist',3, False, path, 4)
df.to_csv('Uncleaned_DS_jobs.csv', index=False)



# coding: utf-8

# In[1]:

from enum import Enum
from collections import namedtuple
import collections


# In[2]:

SKD = namedtuple('Schedule', 'HC, V, W, L, EA, CK')


# # Chapter XI Others III Life Schedule / 第11章 その他 第3節 生活スケジュール

# ## 1. Type of schedule

# ### 1) Heating and Coolind
# The type of schedule for heating and cooling consists of "Weekday" and "Holiday".

# In[3]:

class SKD_HC(Enum):
    W = 'Weekday'
    H = 'Holiday'


# ### 2) Ventilation
# The type of schedule for ventilation consists of "Weekday", "Holiday in house" and "Holiday in absence".

# In[4]:

class SKD_V(Enum):
    W  = 'Weekday'
    HH = 'Holiday in House'
    HA = 'Holiday in Absence'


# ### 3) Hot Water Supply
# The type of schedule for hot water supply consists of "Weekday with large use", "Weekday with middle use", "Weekday with small use", "Holiday in house with large use", "Holiday in house with small use" and "Holiday in absence".

# In[5]:

class SKD_W(Enum):
    W_L  = 'Weekday with Large use'
    W_M  = 'Weekday with Middle use'
    W_S  = 'Weekday with Small use'
    HH_L = 'Holiday in House with Large use'
    HH_S = 'Holiday in House with Small use'
    HA   = 'Holiday in Absence'


# ### 4) Lighting
# The type of schedule for lighting consists of "Weekday", "Holiday in house" and "Holiday in absence".

# In[6]:

class SKD_L(Enum):
    W  = 'Weekday'
    HH = 'Holiday in House'
    HA = 'Holiday in Absence'


# ### 5) Use of Electric Appliances
# The type of schedule for use of electric appliances consists of "Weekday", "Holiday in house" and "Holiday in absence".

# In[7]:

class SKD_EA(Enum):
    W  = 'Weekday'
    HH = 'Holiday in House'
    HA = 'Holiday in Absence'


# ### 6) Cooking
# The type of schedule for cooking consists of "Weekday", "Holiday in house" and "Holiday in absence".

# In[8]:

class SKD_CK(Enum):
    W  = 'Weekday'
    HH = 'Holiday in House'
    HA = 'Holiday in Absence'


# ## 2. Annual Schedule
# Annual schedule is defined in the csv file named "住宅02-11-03_その他_生活スケジュール_生活スケジュール（データ）_131216.csv".  
# Febrary has 28 days and the year has 365 days, not leap year.

# In[9]:

SKDDATA = {
    '1/1'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '1/2'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/3'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/4'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/5'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/6'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/7'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '1/8'  : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '1/9'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/10' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/11' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/12' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/13' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/14' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '1/15' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '1/16' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/17' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/18' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/19' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/20' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/21' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '1/22' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '1/23' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/24' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/25' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/26' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/27' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/28' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '1/29' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '1/30' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '1/31' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/1'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/2'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/3'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/4'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '2/5'  : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '2/6'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/7'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/8'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/9'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/10' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/11' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '2/12' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '2/13' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/14' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/15' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/16' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/17' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/18' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '2/19' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '2/20' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/21' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/22' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/23' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/24' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/25' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '2/26' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '2/27' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '2/28' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/1'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/2'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/3'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/4'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '3/5'  : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '3/6'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/7'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/8'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/9'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/10' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/11' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '3/12' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '3/13' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/14' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/15' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/16' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/17' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/18' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '3/19' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '3/20' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/21' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '3/22' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/23' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/24' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/25' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '3/26' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '3/27' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/28' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/29' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/30' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '3/31' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/1'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '4/2'  : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '4/3'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/4'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/5'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/6'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/7'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/8'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '4/9'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '4/10' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/11' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/12' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/13' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/14' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/15' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '4/16' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '4/17' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/18' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/19' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/20' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/21' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/22' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '4/23' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '4/24' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/25' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/26' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/27' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/28' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '4/29' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '4/30' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '5/1'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/2'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/3'  : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '5/4'  : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '5/5'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '5/6'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '5/7'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '5/8'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/9'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/10' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/11' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/12' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/13' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '5/14' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '5/15' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/16' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/17' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/18' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/19' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/20' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '5/21' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '5/22' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/23' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/24' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/25' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/26' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/27' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '5/28' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '5/29' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/30' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '5/31' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/1'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/2'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/3'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '6/4'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '6/5'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/6'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/7'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/8'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/9'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/10' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '6/11' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '6/12' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/13' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/14' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/15' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/16' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/17' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '6/18' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '6/19' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/20' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/21' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/22' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/23' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/24' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '6/25' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '6/26' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/27' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/28' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/29' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '6/30' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/1'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '7/2'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '7/3'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/4'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/5'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/6'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/7'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/8'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '7/9'  : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '7/10' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/11' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/12' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/13' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/14' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/15' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '7/16' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '7/17' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/18' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/19' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/20' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '7/21' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/22' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '7/23' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '7/24' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/25' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/26' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/27' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/28' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '7/29' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '7/30' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '7/31' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/1'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/2'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/3'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/4'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/5'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '8/6'  : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '8/7'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/8'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/9'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/10' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/11' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/12' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '8/13' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '8/14' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/15' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/16' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/17' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/18' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/19' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '8/20' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '8/21' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/22' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/23' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/24' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/25' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/26' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '8/27' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '8/28' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/29' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/30' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '8/31' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/1'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/2'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '9/3'  : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '9/4'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/5'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/6'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/7'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/8'  : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/9'  : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '9/10' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '9/11' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/12' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/13' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/14' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/15' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '9/16' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '9/17' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '9/18' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/19' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/20' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/21' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/22' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/23' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '9/24' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '9/25' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/26' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/27' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/28' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/29' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '9/30' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '10/1' : SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '10/2' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/3' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/4' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/5' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/6' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/7' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '10/8' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '10/9' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/10': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '10/11': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/12': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/13': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/14': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '10/15': SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '10/16': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/17': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/18': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/19': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/20': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/21': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '10/22': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '10/23': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/24': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/25': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/26': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/27': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/28': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '10/29': SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '10/30': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '10/31': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/1' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/2' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/3' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '11/4' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '11/5' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '11/6' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/7' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/8' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/9' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/10': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/11': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '11/12': SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '11/13': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/14': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/15': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/16': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/17': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/18': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '11/19': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '11/20': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/21': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/22': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/23': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '11/24': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/25': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '11/26': SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '11/27': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/28': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/29': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '11/30': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/1' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/2' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '12/3' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '12/4' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/5' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/6' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/7' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/8' : SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/9' : SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '12/10': SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '12/11': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/12': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/13': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/14': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/15': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/16': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '12/17': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_L,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '12/18': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/19': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/20': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/21': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/22': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/23': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH ),
    '12/24': SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '12/25': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/26': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/27': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_L, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/28': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_S, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/29': SKD(SKD_HC.W, SKD_V.W,  SKD_W.W_M, SKD_L.W,  SKD_EA.W,  SKD_CK.W  ),
    '12/30': SKD(SKD_HC.H, SKD_V.HA, SKD_W.HA,  SKD_L.HA, SKD_EA.HA, SKD_CK.HA ),
    '12/31': SKD(SKD_HC.H, SKD_V.HH, SKD_W.HH_S,SKD_L.HH, SKD_EA.HH, SKD_CK.HH )
    }


# ## 3. Functions

# ### 1) Get annual days

# In[10]:

def get_Annual_Days():
    return ['1/1'  ,'1/2'  ,'1/3'  ,'1/4'  ,'1/5'  ,'1/6'  ,'1/7'  ,'1/8'  ,'1/9'  ,'1/10' ,'1/11' ,'1/12' ,'1/13' ,'1/14' ,'1/15' ,'1/16' ,'1/17' ,'1/18' ,'1/19' ,'1/20' ,'1/21' ,'1/22' ,'1/23' ,'1/24' ,'1/25' ,'1/26' ,'1/27' ,'1/28' ,'1/29' ,'1/30' ,'1/31' ,'2/1'  ,'2/2'  ,'2/3'  ,'2/4'  ,'2/5'  ,'2/6'  ,'2/7'  ,'2/8'  ,'2/9'  ,'2/10' ,'2/11' ,'2/12' ,'2/13' ,'2/14' ,'2/15' ,'2/16' ,'2/17' ,'2/18' ,'2/19' ,'2/20' ,'2/21' ,'2/22' ,'2/23' ,'2/24' ,'2/25' ,'2/26' ,'2/27' ,'2/28' ,'3/1'  ,'3/2'  ,'3/3'  ,'3/4'  ,'3/5'  ,'3/6'  ,'3/7'  ,'3/8'  ,'3/9'  ,'3/10' ,'3/11' ,'3/12' ,'3/13' ,'3/14' ,'3/15' ,'3/16' ,'3/17' ,'3/18' ,'3/19' ,'3/20' ,'3/21' ,'3/22' ,'3/23' ,'3/24' ,'3/25' ,'3/26' ,'3/27' ,'3/28' ,'3/29' ,'3/30' ,'3/31' ,'4/1'  ,'4/2'  ,'4/3'  ,'4/4'  ,'4/5'  ,'4/6'  ,'4/7'  ,'4/8'  ,'4/9'  ,'4/10' ,'4/11' ,'4/12' ,'4/13' ,'4/14' ,'4/15' ,'4/16' ,'4/17' ,'4/18' ,'4/19' ,'4/20' ,'4/21' ,'4/22' ,'4/23' ,'4/24' ,'4/25' ,'4/26' ,'4/27' ,'4/28' ,'4/29' ,'4/30' ,'5/1'  ,'5/2'  ,'5/3'  ,'5/4'  ,'5/5'  ,'5/6'  ,'5/7'  ,'5/8'  ,'5/9'  ,'5/10' ,'5/11' ,'5/12' ,'5/13' ,'5/14' ,'5/15' ,'5/16' ,'5/17' ,'5/18' ,'5/19' ,'5/20' ,'5/21' ,'5/22' ,'5/23' ,'5/24' ,'5/25' ,'5/26' ,'5/27' ,'5/28' ,'5/29' ,'5/30' ,'5/31' ,'6/1'  ,'6/2'  ,'6/3'  ,'6/4'  ,'6/5'  ,'6/6'  ,'6/7'  ,'6/8'  ,'6/9'  ,'6/10' ,'6/11' ,'6/12' ,'6/13' ,'6/14' ,'6/15' ,'6/16' ,'6/17' ,'6/18' ,'6/19' ,'6/20' ,'6/21' ,'6/22' ,'6/23' ,'6/24' ,'6/25' ,'6/26' ,'6/27' ,'6/28' ,'6/29' ,'6/30' ,'7/1'  ,'7/2'  ,'7/3'  ,'7/4'  ,'7/5'  ,'7/6'  ,'7/7'  ,'7/8'  ,'7/9'  ,'7/10' ,'7/11' ,'7/12' ,'7/13' ,'7/14' ,'7/15' ,'7/16' ,'7/17' ,'7/18' ,'7/19' ,'7/20' ,'7/21' ,'7/22' ,'7/23' ,'7/24' ,'7/25' ,'7/26' ,'7/27' ,'7/28' ,'7/29' ,'7/30' ,'7/31' ,'8/1'  ,'8/2'  ,'8/3'  ,'8/4'  ,'8/5'  ,'8/6'  ,'8/7'  ,'8/8'  ,'8/9'  ,'8/10' ,'8/11' ,'8/12' ,'8/13' ,'8/14' ,'8/15' ,'8/16' ,'8/17' ,'8/18' ,'8/19' ,'8/20' ,'8/21' ,'8/22' ,'8/23' ,'8/24' ,'8/25' ,'8/26' ,'8/27' ,'8/28' ,'8/29' ,'8/30' ,'8/31' ,'9/1'  ,'9/2'  ,'9/3'  ,'9/4'  ,'9/5'  ,'9/6'  ,'9/7'  ,'9/8'  ,'9/9'  ,'9/10' ,'9/11' ,'9/12' ,'9/13' ,'9/14' ,'9/15' ,'9/16' ,'9/17' ,'9/18' ,'9/19' ,'9/20' ,'9/21' ,'9/22' ,'9/23' ,'9/24' ,'9/25' ,'9/26' ,'9/27' ,'9/28' ,'9/29' ,'9/30' ,'10/1' ,'10/2' ,'10/3' ,'10/4' ,'10/5' ,'10/6' ,'10/7' ,'10/8' ,'10/9' ,'10/10','10/11','10/12','10/13','10/14','10/15','10/16','10/17','10/18','10/19','10/20','10/21','10/22','10/23','10/24','10/25','10/26','10/27','10/28','10/29','10/30','10/31','11/1' ,'11/2' ,'11/3' ,'11/4' ,'11/5' ,'11/6' ,'11/7' ,'11/8' ,'11/9' ,'11/10','11/11','11/12','11/13','11/14','11/15','11/16','11/17','11/18','11/19','11/20','11/21','11/22','11/23','11/24','11/25','11/26','11/27','11/28','11/29','11/30','12/1' ,'12/2' ,'12/3' ,'12/4' ,'12/5' ,'12/6' ,'12/7' ,'12/8' ,'12/9' ,'12/10','12/11','12/12','12/13','12/14','12/15','12/16','12/17','12/18','12/19','12/20','12/21','12/22','12/23','12/24','12/25','12/26','12/27','12/28','12/29','12/30','12/31',]


# ### 2) Get Schedule

# Define the usage and day as the arguments.

# In[11]:

def get_Schedule(usage, day):
    f = {
        'Heating':            lambda day : SKDDATA[day].HC,
        'Cooling':            lambda day : SKDDATA[day].HC,
        'Ventilation':        lambda day : SKDDATA[day].V,
        'HotWaterSupply':     lambda day : SKDDATA[day].W,
        'Lighting':           lambda day : SKDDATA[day].L,
        'ElectricAppliances': lambda day : SKDDATA[day].EA,
        'Cooking':            lambda day : SKDDATA[day].CK,
    }
    return f[usage](day)


# ### Examples 

# 12/31 Heating

# In[12]:

get_Schedule('Heating','12/29')


# 12/30 Ventilation

# In[13]:

get_Schedule('Ventilation','12/30')


# #### Count the number of the types of schedule for each usage.

# In[14]:

def count_types_of_schedule(usage):
    types_of_schedule = list(map(lambda d: get_Schedule(usage, d),  get_Annual_Days() ))
    return collections.Counter(types_of_schedule)


# Heating

# In[15]:

count_types_of_schedule('Heating')


# Cooling

# In[16]:

count_types_of_schedule('Cooling')


# Ventilation

# In[17]:

count_types_of_schedule('Ventilation')


# Hot Water Supply

# In[18]:

count_types_of_schedule('HotWaterSupply')


# Lighting

# In[19]:

count_types_of_schedule('Lighting')


# Electric Appliances

# In[20]:

count_types_of_schedule('ElectricAppliances')


# Cooking

# In[21]:

count_types_of_schedule('Cooking')


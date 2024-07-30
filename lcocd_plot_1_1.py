# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:53:32 2024

@author: Thomas Meyn

To do:
        Nothing right now    
    
"""

#%%

''' IMPORT STUFF '''

import os
import pickle
import copy
import pandas as pd
import matplotlib.pyplot as plt
import easygui




#%%

''' Function for loading, processing and saving the raw data '''

def load_data(path, directory):

    os.chdir(path)    
 
    subfolders = [ f.name for f in os.scandir(directory) if f.is_dir() ]    # Creates i list with all subfolders in the specified directory
 
 
    ''' Create indexes '''

    index = list()                                                          # Creates a list with name index  

    for x in range(0, len(subfolders)):                                     # Remove the traling a from directory names to created sample index
        index.append(subfolders[x][1:6])                                     # Leaves out the trailing character 'a'


    ''' Create a dataframes with raw and store them in dictionary '''
    uv_data = {}; ocd_data = {}; ond_data = {} 
    
    for x in range(0,len(index)):

        # Where to store the data           #Create file name                                                                        #set headers       #set time as index  
        uv_data[index[x]] = pd.read_csv((directory + '/' + subfolders[x] + '/uvd' + index [x] + '.dat'), sep='\s+', header=None, names=['time', 'uvd']).set_index('time')
        ocd_data[index[x]] = pd.read_csv((directory + '/' + subfolders[x] + '/ocd' + index [x] + '.dat'), sep='\s+', header=None, names=['time', 'ocd']).set_index('time')
        ond_data[index[x]] = pd.read_csv((directory + '/' + subfolders[x] + '/ond' + index [x] + '.dat'), sep='\s+', header=None, names=['time', 'ond']).set_index('time')
        
    
    ''' Correct for dillution '''
    
    uv_data_dill = {}; ocd_data_dill = {}; ond_data_dill = {}

    uv_data_dill = copy.deepcopy(uv_data)

    for x in range(0,len(index)):
        uv_data_dill[index[x]] = uv_data[index[x]].multiply(dillution[index[x]])
       
        
    ocd_data_dill = copy.deepcopy(ocd_data)

    for x in range(0,len(index)):
        ocd_data_dill[index[x]] = ocd_data[index[x]].multiply(dillution[index[x]])


    ond_data_dill = copy.deepcopy(ond_data)
        
    for x in range(0,len(index)):
        ond_data_dill[index[x]] = ond_data[index[x]].multiply(dillution[index[x]])
        
        
    ''' Save the data to file '''
    # Create dictionary for saving all data
    data_storage = {'index':index, 'uv_data':uv_data, 'ocd_data':ocd_data, 'ond_data':ond_data, 'uv_data_dill':uv_data_dill, 'ocd_data_dill':ocd_data_dill, 'ond_data_dill':ond_data_dill}
    pickle.dump(data_storage, open( "lcocd_raw_data.p", "wb" ))
    
    
    return index, uv_data, ocd_data, ond_data, uv_data_dill, ocd_data_dill, ond_data_dill
    
#%%

''' Build dictionaries from raw data files and save them to storage file '''

index, uv_data, ocd_data, ond_data, uv_data_dill, ocd_data_dill, ond_data_dill = load_data("C:/Users/tmeyn/Documents/Python/LC-OCD",'Data')

#%%

''' Load the processed data from storage file '''

data_storage = pickle.load( open( "lcocd_raw_data.p", "rb" ) )

index = data_storage['index']
uv_data = data_storage['uv_data'] ; ocd_data = data_storage['ocd_data'] ; ond_data = data_storage['ond_data']
uv_data_dill = data_storage['uv_data_dill'] ; ocd_data_dill = data_storage['ocd_data_dill'] ; ond_data_dill = data_storage['ond_data_dill']

#%%

''' Function for creating dictionaries with sample information '''

def sample_data():
    
    sample_name = {}; day = {}; dillution ={}
    
        # Sample 01776 is Trondheim detergent

    dillution = dict([
        ('01663',10), ('01664',5), ('01665',5), ('01666',5), ('01667',5), ('01668',5), ('01669',5),
        ('01670',5), ('01671',5), ('01672',5), ('01673',5), ('01674',5), ('01675',5), ('01676',50), ('01677',50), ('01678',50),  ('01679',5),
        ('01680',5), ('01681',50), ('01682',50), ('01683',50), ('01684',100), ('01685',50), ('01686',32), ('01687',50), ('01688',100), ('01689',100),
        ('01690',50), ('01691',50), ('01692',100), ('01693',50), ('01694',100), ('01695',100), ('01696',20), ('01697',20), ('01698',20), ('01699',12),
        ('01700',20), ('01701',20), ('01702',20), ('01703',20), ('01704',20), ('01705',20), ('01706',20), ('01707',50), ('01708',100), ('01709',50),
        ('01710',100), ('01711',100), ('01712',100), ('01713',50), ('01714',50), ('01715',100), ('01716',100), ('01717',50), ('01718',20), ('01719',12),
        ('01720',20), ('01721',50), ('01722',50), ('01723',50), ('01724',20), ('01725',20), ('01726',50), ('01727',50), ('01728',10), ('01729',10), 
        ('01730',30), ('01731',50), ('01732',50), ('01733',50), ('01734',10), ('01735',10), ('01736',30), ('01737',50), ('01738',50), ('01739',50),
        ('01740',10), ('01741',10), ('01742',10), ('01743',5), ('01744',10), ('01745',10), ('01746',10), ('01747',10), ('01748',10), ('01749',5),
        ('01750',10), ('01751',10), ('01752',10), ('01753',10), ('01754',50), ('01755',50), ('01756',50), ('01757',10), ('01758',10), ('01759',30),
        ('01760',50), ('01761',50), ('01762',50), ('01763',10), ('01764',10), ('01765',10), ('01766',5), ('01767',10), ('01768',10), ('01769',10), 
        ('01770',10), ('01771',10), ('01772',5), ('01773',10), ('01774',10), ('01775',10000), ('01776',10), ('01779',1000),
        ('01780',1000), ('01781',10000), ('01782',10000)
    ])

    day = dict([
        ('01664','16'),  ('01665','1'),    ('01666','28'),   ('01667','34'),   ('01668','6'),    ('01669','16'),
        ('01670','1'),   ('01671','28'),   ('01672','34'),   ('01673','6'),    ('01674','16'),   ('01675','1'),    ('01676','28'),   ('01677','34'),   ('01678','6'),    ('01679','16'),
        ('01680','1'),   ('01681','28'),   ('01682','34'),   ('01683','6'),    ('01684','6'),    ('01685','16'),   ('01686','1'),    ('01687','1'),    ('01688','28'),   ('01689','34'),
        ('01690','1'),   ('01691','1'),    ('01692','6'),    ('01693','16'),   ('01694','28'),   ('01695','34'),   ('01696','6'),    ('01697','6'),    ('01698','16'),   ('01699','1'),
        ('01700','1'),   ('01701','28'),   ('01702','34'),   ('01703','16'),   ('01704','1'),    ('01705','28'),   ('01706','34'),   ('01707','1'),    ('01708','6'),    ('01709','16'),
        ('01710','28'),  ('01711','34'),   ('01712','6'),    ('01713','16'),   ('01714','1'),    ('01715','28'),   ('01716','34'),   ('01717','6'),    ('01718','16'),   ('01719','1'),
        ('01720','1'),   ('01721','28'),   ('01722','34'),   ('01723','6'),    ('01724','16'),   ('01725','1'),    ('01726','28'),   ('01727','34'),   ('01728','16'),   ('01729','1'),
        ('01730','1'),   ('01731','28'),   ('01732','34'),   ('01733','6'),    ('01734','16'),   ('01735','1'),    ('01736','1'),    ('01737','28'),   ('01738','34'),   ('01739','6'),
        ('01740','6'),   ('01741','16'),   ('01742','1'),    ('01743','1'),    ('01744','28'),   ('01745','34'),   ('01746','6'),    ('01747','16'),   ('01748','1'),    ('01749','1'),
        ('01750','28'),  ('01751','34'),   ('01752','16'),   ('01753','1'),    ('01754','28'),   ('01755','34'),   ('01756','6'),    ('01757','16'),   ('01758','1'),    ('01759','1'),
        ('01760','28'),  ('01761','34'),   ('01762','6'),    ('01763','6'),    ('01764','16'),   ('01765','1'),    ('01766','1'),    ('01767','28'),   ('01768','34'),   ('01769','6'),
        ('01770','16'),  ('01771','1'),    ('01772','1'),    ('01773','28'),   ('01774','34'),
    ])

    sample_name = dict([
        ('01663','Tap water Trondheim'), ('01664','Blank Aerobic 1'),
        ('01665','Blank Aerobic 1'), ('01666','Blank Aerobic 1'), ('01667','Blank Aerobic 1'), ('01668','Blank Aerobic 1'), ('01669','Blank Aerobic 2'),
        ('01670','Blank Aerobic 2'), ('01671','Blank Aerobic 2'), ('01672','Blank Aerobic 2'), ('01673','Blank Aerobic 2'), ('01674','Blank Anaerobic 1'),
        ('01675','Blank Anaerobic 1'), ('01676','Blank Anaerobic 1'), ('01677','Blank Anaerobic 1'), ('01678','Blank Anaerobic 1'),  ('01679','Blank Anaerobic 2'),
        ('01680','Blank Anaerobic 2'), ('01681','Blank Anaerobic 2'), ('01682','Blank Anaerobic 2'), ('01683','Blank Anaerobic 2'), ('01684','S1 high a1'),
        ('01685','S1 high a1'),  ('01686','S1 high a1'),  ('01687','S1 high a1'),  ('01688','S1 high a1'),  ('01689','S1 high a1'),
        ('01690','S1 high a2'),  ('01691','S1 high a2'),  ('01692','S1 high a2'),  ('01693','S1 high a2'),  ('01694','S1 high a2'),
        ('01695','S1 high a2'),  ('01696','S1 low a1'),   ('01697','S1 low a1'),   ('01698','S1 low a1'),   ('01699','S1 low a1'),
        ('01700','S1 low a1'),   ('01701','S1 low a1'),   ('01702','S1 low a1'),   ('01703','S1 low a2'),   ('01704','S1 low a2'),
        ('01705','S1 low a2'),   ('01706','S1 low a2'),   ('01707','S1 high an1'), ('01708','S1 high an1'), ('01709','S1 high an1'),
        ('01710','S1 high an1'), ('01711','S1 high an1'), ('01712','S1 high an2'), ('01713','S1 high an2'), ('01714','S1 high an2'),
        ('01715','S1 high an2'), ('01716','S1 high an2'), ('01717','S1 low an1'),  ('01718','S1 low an1'),  ('01719','S1 low an1'),
        ('01720','S1 low an1'),  ('01721','S1 low an1'),  ('01722','S1 low an1'),  ('01723','S1 low an2'),  ('01724','S1 low an2'),
        ('01725','S1 low an2'),  ('01726','S1 low an2'),  ('01727','S1 low an2'),  ('01728','S2 high a1'),  ('01729','S2 high a1'), 
        ('01730','S2 high a1'),  ('01731','S2 high a1'),  ('01732','S2 high a1'),  ('01733','S2 high a1'),  ('01734','S2 high a2'),
        ('01735','S2 high a2'),  ('01736','S2 high a2'),  ('01737','S2 high a2'),  ('01738','S2 high a2'),  ('01739','S2 high a2'),
        ('01740','S2 low a1'),   ('01741','S2 low a1'),   ('01742','S2 low a1'),   ('01743','S2 low a1'),   ('01744','S2 low a1'),
        ('01745','S2 low a1'),   ('01746','S2 low a2'),   ('01747','S2 low a2'),   ('01748','S2 low a2'),   ('01749','S2 low a2'),
        ('01750','S2 low a2'),   ('01751','S2 low a2'),   ('01752','S2 high an1'), ('01753','S2 high an1'), ('01754','S2 high an1'),
        ('01755','S2 high an1'), ('01756','S2 high an1'), ('01757','S2 high an2'), ('01758','S2 high an2'), ('01759','S2 high an2'),
        ('01760','S2 high an2'), ('01761','S2 high an2'), ('01762','S2 high an2'), ('01763','S2 low an1'),  ('01764','S2 low an1'),
        ('01765','S2 low an1'),  ('01766','S2 low an1'),  ('01767','S2 low an1'),  ('01768','S2 low an1'),  ('01769','S2 low an2'), 
        ('01770','S2 low an2'),  ('01771','S2 low an2'),  ('01772','S2 low an2'),  ('01773','S2 low an2'),  ('01774','S2 low an2'),
        ('01775','Detergent Trondheim'), ('01776','Detergent Trondheim'), ('01779','Enviro Infravask'), 
        ('01780','Enviro Infravask'),    ('01781','Enviro Infravask'),    ('01782','Enviro Infravask')
    ])

    return dillution, day, sample_name

#%%

''' Running function that builds sample information dictionaries '''

dillution, day, sample_name = sample_data()




#%%

''' INPUT PARAMETERS '''

# sampleID = ['01734','01734','01734']      # Do it the manual way

# Get user input
# user_input = input("Enter the samle IDs that you want to plot, separated by commas: ") # Command line version

user_input = easygui.enterbox("Enter the samle IDs that you want to plot, separated by commas:")  # Using a text box with a GUI

sampleID = [s.strip() for s in user_input.split(",")]

#add leading zero
for x in range(len(sampleID)):
    sampleID[x] = ('0' + sampleID[x])

print(f"List of samples: {sampleID}")

    

#%%

''' Do the plotting '''
fig, axs = plt.subplots(3,figsize=(6, 10))
#plt.figure(figsize=(10,6))


# Create legend lables
legend_labels = list()

for ID in sampleID:
    if day.get(ID, -1) == -1:
        legend_labels.append(sample_name[ID])

    else:                            
        legend_labels.append(sample_name[ID] + ' - Day ' + day[ID])


''' UV '''
axs[0].set_xlabel('Time [min]')
axs[0].set_ylabel('UV-Detector signal')

# Plot data from all samples contained in 'sample_ID'
for ID in sampleID:
    uv_data_dill.get(ID)    
    axs[0].plot(uv_data_dill[ID])

# Add legend
axs[0].legend(labels = legend_labels, frameon=False, title="Sample ID:", alignment='left')

axs[0].set_xlim(left=20, right=120)



''' OCD '''
axs[1].set_xlabel('Time [min]')
axs[1].set_ylabel('OCD-Detector signal')

# Plot data from all samples contained in 'sample_ID'
for ID in sampleID:
    ocd_data_dill.get(ID)    
    axs[1].plot(ocd_data_dill[ID])

# Add legend
axs[1].legend(labels = legend_labels, frameon=False, title="Sample ID:", alignment='left')

axs[1].set_xlim(left=20, right=120)


''' OND '''
axs[2].set_xlabel('Time [min]')
axs[2].set_ylabel('OND-Detector signal')

# Plot data from all samples contained in 'sample_ID'
for ID in sampleID:
    ond_data_dill.get(ID)    
    axs[2].plot(ond_data_dill[ID])

# Add legend
axs[2].legend(labels = legend_labels, frameon=False, title="Sample ID:", alignment='left')

axs[2].set_xlim(left=20, right=120)

#fig.suptitle(title, fontsize=16, weight='bold')

plt.tight_layout()
plt.show()

## df_uv.plot(set_ylabel("Signal [mV]"))
    
    
    

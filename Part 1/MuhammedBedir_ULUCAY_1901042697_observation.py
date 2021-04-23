import pandas as pd
import numpy as np
import math

'''
Index(['country', '#q3', '#q4', 'q#5_min', 'q#5_max', 'q#5_avg', 'q#5_var',
       'q#6_min', 'q#6_max', 'q#6_avg', 'q#6_var', 'q#7_min', 'q#7_max',
       'q#7_avg', 'q#7_var', 'q#8_min', 'q#8_max', 'q#8_avg', 'q#8_var',
       'q#9_min', 'q#9_max', 'q#9_avg', 'q#9_var', 'q#10_min', 'q#10_max',
       'q#10_avg', 'q#10_var', 'q#11_min', 'q#11_max', 'q#11_avg', 'q#11_var',
       'q#12_min', 'q#12_max', 'q#12_avg', 'q#12_var', 'q#13_min', 'q#13_max',
       'q#13_avg', 'q#13_var', 'q#14_var', 'q#15_var', 'q#16_var',
       'population', 'median_age', '#aged_65_older', '#aged_70_older',
       'economic_performance', 'death_rates_due_to_heart_disease',
       'diabetes_prevalance', '#of_female_smokers', '#of_male_smokers',
       'handwashing_facilities', 'hospital_beds_per_thousand_people',
       'life_expectancy', 'human_development_index'],
'''

df = pd.read_csv("output.csv")

# print(df.columns)
# print(df.head())

deathRate = df['#q4'] / df['#q3']

#####   economic performans

economic = df.sort_values('economic_performance')
economic['deathRateOfTotalCase'] = deathRate
# print(economic[['country','deathRateOfTotalCase','economic_performance']][163:181])

####    older age

older = df.sort_values('#aged_65_older')
older['Death Rate'] = deathRate
# print(older.tail(53)[['country','#aged_65_older', 'Death Rate']])


####  bed per thousand

bed = df.sort_values('hospital_beds_per_thousand_people')
bed['Death Rate'] = deathRate
# print(bed[['country', 'hospital_beds_per_thousand_people','Death Rate']][24:39])


####     smokers
df['totalSmoke'] = (df['#of_female_smokers'] + df['#of_male_smokers'])
smoke = df.sort_values('totalSmoke')
smoke['Death Rate'] = deathRate 
smoke['smokerRate(m+f smokers)'] = (df['#of_female_smokers'] + df['#of_male_smokers'])

# print(smoke[['country', 'smokerRate(m+f smokers)' ,'Death Rate']][0:60])

####     vacation
dfc = pd.read_csv('owid-covid-data.csv')
dfc['people_vaccinated'].fillna('no data',inplace=True)
# print(dfc[dfc['location'] == 'Slovenia'] [['location','date' ,'new_cases', 'people_vaccinated']][350:])

####     hand wash

# print(df[['country','handwashing_facilities']])
# Vietnam Zambia

zam = dfc[dfc['location'] == 'Zambia'][['location','date','new_cases','population','handwashing_facilities']][250:]
vie = dfc[dfc['location'] == 'Vietnam'][['location','date','new_cases','population','handwashing_facilities']][305:]
# print(zam)
# print(vie)


#### heart disase

ma = dfc.groupby('location')[['location', 'cardiovasc_death_rate']].max().values
# Singapur
# Uzbekistan

heart = df.sort_values('death_rates_due_to_heart_disease') 
heart['Death Rate'] = deathRate

# print(heart[['country','death_rates_due_to_heart_disease','Death Rate']][20:40])
# print(heart[['country','death_rates_due_to_heart_disease','Death Rate']][150:170])



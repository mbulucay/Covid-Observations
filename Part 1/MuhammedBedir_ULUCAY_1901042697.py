import pandas as pd
import numpy as np

covid_df = pd.read_csv("owid-covid-data.csv")
countries = covid_df['location'].unique()

#1,2
#################################################################################################################################

q1 = len(f"Number of country = {countries}")
q2 = covid_df.loc[covid_df['date'] == min(covid_df['date'])]

print(q1)
print(q2)

#3,4
#################################################################################################################################

#total case and total deaths
q3_4 = pd.DataFrame(index = np.arange(len(countries)))
q3_4['country'] = covid_df['location'].unique()

q3_4['#q3'] = covid_df.groupby('location')['total_cases'].max().values
q3_4['#q4'] = covid_df.groupby('location')['total_deaths'].max().values

#5-13
#################################################################################################################################

#calulations for each country 

q5_13_df = pd.DataFrame(index = np.arange(len(countries)))
q5_13_df['country'] = covid_df['location'].unique()

def getCalculationsResults(covidDf,myDf,colName,qNumber):
    #Grouping by country and calculating wanted properties 
    myDf['q#' + str(qNumber) +'_min'] = covid_df.groupby('location')[colName].min().values
    myDf['q#' + str(qNumber) +'_max'] = covid_df.groupby('location')[colName].max().values
    myDf['q#' + str(qNumber) +'_avg'] = covid_df.groupby('location')[colName].mean().values
    myDf['q#' + str(qNumber) +'_var'] = covid_df.groupby('location')[colName].var().values
    
    return myDf
#wanted properties 
q5_13CovidClmNames = ['reproduction_rate','icu_patients','hosp_patients','weekly_icu_admissions',
            'weekly_hosp_admissions','new_tests','total_tests','positive_rate','tests_per_case']

for i,colName in enumerate(q5_13CovidClmNames,5):
    q5_13_df = getCalculationsResults(covid_df,q5_13_df,colName,i)

# print(q5_13_df)

#14-16
#################################################################################################################################

#vaccinated column properties of countries
q14_16_df =  pd.DataFrame(index = np.arange(len(countries)))
q14_16_df['country'] = covid_df['location'].unique()

q14_16_df['q#' + str(14) +'_var'] = covid_df.groupby('location')['people_vaccinated'].max().values
q14_16_df['q#' + str(15) +'_var'] = covid_df.groupby('location')['people_fully_vaccinated'].max().values
q14_16_df['q#' + str(16) +'_var'] = covid_df.groupby('location')['total_vaccinations'].max().values

# print(q14_16_df)

#17
#################################################################################################################################

q17_df = pd.DataFrame(index = np.arange(len(countries)))
q17_df['country'] = countries

q17CovidClmNames = ['population', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita',
                'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers',
                'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy', 'human_development_index']

q17OurClmNames = ['population', 'median_age', '#aged_65_older', '#aged_70_older', 'economic_performance',
                    'death_rates_due_to_heart_disease', 'diabetes_prevalance','#of_female_smokers',
                    '#of_male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand_people',
                    'life_expectancy', 'human_development_index']

#collect all data wanted column in q17CovidClmNames and putting clm name q17OurClmNames
#this will iterate all seri
for ourClmName,CovidClmName in zip(q17OurClmNames,q17CovidClmNames):
    q17_df[ourClmName] = covid_df.groupby('location')[CovidClmName].max().values

# print(q17_df)    

#18
#################################################################################################################################

#collect all data in one data Frame
def CollectDf(BaseDf:pd.DataFrame, *dfs:pd.DataFrame):
    
    countries = covid_df['location'].unique()
    myDf = pd.DataFrame(countries,index = np.arange(len(countries)),columns=['country'])

    for df in dfs:
        for clm in df.columns:
           myDf[clm] = df[clm]
    
    return myDf

df = CollectDf(covid_df,q3_4,q5_13_df,q14_16_df,q17_df)
df.to_csv('output.csv',index = False)
print(f"output.csv is created")

# print(q5_13_df)
# print(q14_16_df)
# print(q17_df)
# print(df)


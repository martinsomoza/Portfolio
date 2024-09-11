import pandas as pd

df = pd.read_csv('C:/Users/Tino/Documents/Documentos/Data/freeCodeCamp Data Analytics with Python/adult.data.csv')

race_count = df['race'].value_counts()

men_df = df[df['sex']=='Male']
average_men = men_df['age'].mean().round(1)

total_people = len(df)
bachelors_count = df['education'].str.contains('Bachelors', case=False, na=False).sum()
percentage_bachelors = ((bachelors_count / total_people) * 100).round(1)

bachelors_count = df['education'].str.contains('Bachelors', case=False, na=False).sum()
masters_count = df['education'].str.contains('Masters', case=False, na=False).sum()
doctorate_count = df['education'].str.contains('Doctorate', case=False, na=False).sum()
advanced_count = bachelors_count + masters_count + doctorate_count
advanced_education = df[
    (df['education']=='Bachelors') |
    (df['education']== 'Masters') | 
    (df['education']== 'Doctorate')
    ]
morethan50advanced = advanced_education['salary'].str.contains('>50K', case=False, na=False).sum()
percentage_advanced_more50 = ((morethan50advanced / advanced_count) * 100).round(1)

advanced_education_levels = ['Bachelors', 'Masters', 'Doctorate']
not_advanced_education = df[~df['education'].isin(advanced_education_levels)]
not_advanced_education_count = not_advanced_education.shape[0]
morethan50notadvanced = not_advanced_education['salary'].str.contains('>50K', case=False, na=False).sum()
percentage_notadvanced_more50 = ((morethan50notadvanced / not_advanced_education_count) * 100).round(1)


minimum_hoursweek = df['hours-per-week'].min()

minimum_workers_count = df[df['hours-per-week']==1].shape[0]
minimum_workers_more50_count = df[
    (df['hours-per-week']==1) &
    (df['salary']=='>50K')
    ].shape[0]
percentage_minimun_workers_more50 = (minimum_workers_more50_count / minimum_workers_count) * 100

morethan50k = df[df['salary']=='>50K']
total_count = df.groupby('native-country').size()
morethan50k_count = morethan50k.groupby('native-country').size()
percentage_high_earners_percountry = ((morethan50k_count / total_count) * 100).round(1)
max_high_earners_global = percentage_high_earners_percountry.max()
max_percentage_country = percentage_high_earners_percountry[percentage_high_earners_percountry == max_high_earners_global]

morethan50k_india = df[
    (df['salary']=='>50K') &
    (df['native-country']=='India')
    ]
ocupations_india_highearn = morethan50k_india.groupby('occupation').size()
most_frequent_occupation = ocupations_india_highearn.idxmax()
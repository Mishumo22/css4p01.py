# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:26:42 2024

@author: Mishu
"""

# First I import the library

import pandas as pd

#import dataframe as df

#Load the dataset/dataframe

df = pd.read_csv("movie_dataset.csv")

#Removing space from the dataset/dataframe

df.columns = df.columns.str.replace(' ', '_')

#identifying data that is missing in the dataset

df.isnull().sum()

#Dropping columns and rows that have missing data and dropping title with incorrect title names

df.dropna(axis=0, inplace=True)
 
df.drop('Title', axis=1, inplace=True)

#The highest rated movie in the dataset this is achieved by # on the df.drop('Title', axis=1, inplace=True) for name description 

highest_rated_movie = df.loc[df["Rating"].idxmax()]

#The average revenue of all movies in the dataset
#The average is 84.56 which is between 70 and 100 milllion 

average_revenue = df['Revenue_(Millions)'].mean()

#The average revenue of movies from 2015 to 2017 in the dataset. The average revenue is 64.498 which is between 50 and 80 million

filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

average_revenue = filtered_df['Revenue_(Millions)'].mean()

#How many movies were released in the year 2016. The dataset is filtered to only work on movies released in the year 2016 including the dropped columns and rows data
#results are 297
movies_2016 = df[df['Year'] == 2016]

num_movies_2016 = movies_2016.shape[0]

#How many movies were directed by Christopher Nolan
#I used value count so that i can calculate the number of time Christopher Nolan appears as a director using the cleaned dataset

nolan_movies = df[df['Director'] == 'Christopher Nolan']

nolan_movie_count = nolan_movies.shape[0]

#How many movies in the dataset have a rating of at least 8.0 including the dropped columns, rows and title data
#This would result in the number of movies being 78
movies_with_high_rating = df[df['Rating'] >= 8.0]

num_movies_with_high_rating = len(movies_with_high_rating)

#What is the median rating of movies directed by Christopher Nolan using the clean data. 
#with the original dataset the median is not affected 
nolan_movies = df[df['Director'] == 'Christopher Nolan']

median_rating = nolan_movies['Rating'].median()

#The year with the highest average rating with the original dataset

average_ratings_by_year = df.groupby('Year')['Rating'].mean()

year_with_highest_average_rating = average_ratings_by_year.idxmax()

#The percentage increase of the original dataset

num_movies_2006 = df[df['Year'] == 2006].shape[0]

num_movies_2016 = df[df['Year'] == 2016].shape[0]

increase_in_movies = num_movies_2016 - num_movies_2006

percentage_increase = (increase_in_movies / num_movies_2006) * 100

#The most common actor of the original dataset

df['Actors'] = df['Actors'].str.split(',')

df_actors = df.explode('Actors')

actor_counts = df_actors['Actors'].value_counts()

most_common_actor = actor_counts.idxmax()
 
#The number of unique genres of the original data

df['Genre'] = df['Genre'].str.split(',')

df_exploded = df.explode('Genre')

unique_genres = df_exploded['Genre'].nunique()

#The numerical correlation shows that the year 2016 has a higher average as compared to 2012 and 2014 however the movie rankings for 2016 are lower than that of 2012 and 2014, with 2014 being ranked number one. 
#The most watched genre is action 
numerical_cols = df.select_dtypes(include=['float64', 'int64'])

corr_matrix = numerical_cols.corr()




# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:43:23 2024

@author: Zibro710
"""

import pandas as pd

#Create a directory which stores the movie dataset

md = pd.read_csv("movie_dataset.csv")

# Renaming each column with spaces inbetween

md = md.rename(columns = {'Runtime (Minutes)':'Runtime_(Minutes)'})
md = md.rename(columns = {'Revenue (Millions)':'Revenue_(Millions)'})


# This will drop all rows where the column'Revenue_(Millions)' has any null or empty values

new_md = md.dropna(subset=['Revenue_(Millions)'], how='all')

# This will drop all the specified columns (Relevance) 

new_md = new_md.drop(columns = "Rank")
new_md = new_md.drop(columns = "Description")
new_md = new_md.drop(columns = "Votes")
new_md = new_md.drop(columns = "Metascore")

###############################################################################
                             ####QUESTION 01####
###############################################################################

Highest_rated_movie = new_md.loc[new_md['Rating'].idxmax()]['Title']

print(f"The highest rated movie is: {Highest_rated_movie}")


###############################################################################
                             ####QUESTION 02####
###############################################################################

Revenue = 'Revenue_(Millions)'

# Using the mean() method to calculate the average

Average_revenue = new_md[Revenue].mean()

print(f"The average revenue of all movies is: {Average_revenue} Million")

###############################################################################
                             ####QUESTION 03####
###############################################################################

Year_column = 'Year'

# Using boolean indexing to filter rows based on the condition i.e 2015-2017

filtered_md = new_md[(new_md[Year_column] >= 2015) & (new_md[Year_column] <= 2017)]

# Using the mean() method on the filtered DataFrame 'fitered_md' to calculate the average

New_Average_revenue = filtered_md[Revenue].mean()

# Now 'New_Average_revenue' contains the average of values in the specified column 'Year' for the specified condition i.e 2015-2017

# Printing the result for verification
print(f"The average revenue of all movies  between 2015 and 2017 is: {New_Average_revenue} Million")

###############################################################################
                             ####QUESTION 04####
###############################################################################

Target_year = 2016

# Using boolean indexing to filter rows based on the specific year i.e 2016 in the DataFrame 'md'

Movies_in_2016 = md[md[Year_column] == Target_year]

# Now 'Movies_in_2016' is a subset containing all rows where the release year is 2016

# Using the shape attribute to get the number of rows (movies) in the filtered DataFrame 'filtered_md'

Number_of_movies = Movies_in_2016.shape[0]

# Now 'Number_of_movies' contains the count of movies released in the 2016

# Print the result for verification
print(f"Number of movies released in {Target_year}: {Number_of_movies}")

###############################################################################
                             ####QUESTION 05####
###############################################################################

Director_names = 'Director'
Target_director = 'Christopher Nolan'

# Using boolean indexing to filter rows based on the specific director i.e 'Christopher Nolan' in the DataFrame 'md'

Director = md[md[Director_names] == Target_director]

# Now 'Director' is a subset containing all movies directed by Christopher Nolans names 

# Using the shape attribute to get the number of rows (movies) directed by the Target director

Number_of_directed_movies = Director.shape[0]

# Now 'Number_of_directed_movies' contains the count of movies directed by Christopher Nolan

# Printing the result for verification
print(f"The number of movies directed by '{Target_director}' is: {Number_of_directed_movies}")

###############################################################################
                             ####QUESTION 06####
###############################################################################

Rating_column = 'Rating'

# Using boolean indexing to filter rows based on the condition i.e Ratings >= 8.0

filtered_rating = md[(md[Rating_column] >= 8.0)]

# Using the shape attribute to get the number of rows (movies) with at least an 8.0 rating

Number_of_movies__atleast_8_rating = filtered_rating.shape[0]

# Now 'New_Average_revenue' contains the average of values in the specified column 'Year' for the specified condition i.e 2015-2017

# Printing the result for verification
print(f"The number of movies with a rating of atleast 8.0 rating is: {Number_of_movies__atleast_8_rating}")

###############################################################################
                             ####QUESTION 07####
###############################################################################

Median_rating = Director[Rating_column].median()

# Printing the result for verification
print(f"The median rating  of all the movies directed by '{Target_director}' is: {Median_rating}")

###############################################################################
                             ####QUESTION 08####
###############################################################################

# Grouping the DataFrame by 'year' and calculating the mean rating for each year
Average_ratings_by_year = md.groupby('Year')['Rating'].mean()

# Finding the year with the highest average rating
Highest_avg_rating_year = Average_ratings_by_year.idxmax()

# Display the result
print(f"The year with the highest average rating is: {Highest_avg_rating_year}")

###############################################################################
                             ####QUESTION 09####
###############################################################################

# Filteing the data for the years 2006 and 2016

Movies_2006 = md[md['Year'] == 2006]
Movies_2016 = md[md['Year'] == 2016]

# Counting the number of movies for each year

Num_Movies_2006 = len(Movies_2006)
Num_Movies_2016 = len(Movies_2016)

# Calculating the percentage increase

Percentage_increase = ((Num_Movies_2016 - Num_Movies_2006) / Num_Movies_2006) * 100

# Printing the result
print(f"The percentage increase in the number of movies between 2006 and 2016 is: {Percentage_increase:.2f} %")

###############################################################################
                             ####QUESTION 10####
###############################################################################
# Storing the column 'Actors' as a variable 'Actors_column'

Actors_column = 'Actors'

# This will split the names in each row using the 'comma' as a separator and stack them into a new DataFrame called 'All_names'

All_names = new_md[Actors_column].str.split(',', expand=True).stack()

# Use value_counts to get the count of each unique name

Unique_name_counts = All_names.value_counts()

# Now 'Unique_name_counts' is a Series with names as the index and their counts as values

# Print the result for verification
print(Unique_name_counts)

###############################################################################
                             ####QUESTION 11####
###############################################################################

# Extracting unique genres from the 'Genre' column

Unique_genres = md['Genre'].unique()

# Calculating the count of unique genres

Num_unique_genres = len(Unique_genres)

# Print the result
print(f'The number of unique genres in the dataset is: {Num_unique_genres}')


###############################################################################
                             ####QUESTION 12####
###############################################################################

# Calculating the correlation matrix
Correlation_matrix = md.corr()

# Now 'Correlation_matrix' contains the correlation coefficients between numerical features

# Printing the correlation matrix for insights
print(Correlation_matrix)

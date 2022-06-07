import pandas as pd
import numpy as np
import os
from scipy.sparse import csr_matrix

main_directory = os.getcwd()
target_directory = "ml-latest-small"
work_directory = os.path.join(main_directory, target_directory)

movies = pd.read_csv(os.path.join(work_directory, "movies.csv"))
ratings = pd.read_csv(os.path.join(work_directory,'ratings.csv'))

final_dataset = ratings.pivot(index='movieId', columns='userId', values='rating')
final_dataset.fillna(0, inplace=True)

num_user_voted = ratings.groupby('movieId')['rating'].agg('count')  #votes for each movie
num_movies_voted = ratings.groupby('userId')['rating'].agg('count') #votes by each user

final_dataset = final_dataset.loc[num_user_voted[num_user_voted > 10].index, :]
final_dataset  = final_dataset.loc[:, num_movies_voted[num_movies_voted>50].index]
csr_data = csr_matrix(final_dataset.values)
final_dataset.reset_index(inplace=True)


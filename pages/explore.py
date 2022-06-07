import pandas as pd
import numpy as np
import os
from scipy.sparse import csr_matrix
import streamlit as st

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


def Show_most_watched_movies():
    st.markdown('##')
    with st.expander('Curious about the most watched movies?', expanded=False):
        n_most_watched_movies = st.radio('Make Selection', (3,5,10))
        most_watched = []
        most_watched_movies = num_user_voted.sort_values().tail(n_most_watched_movies).index.to_list()
        for val in most_watched_movies:
            idx_1 = movies[movies['movieId']== val].index
            name = movies.iloc[idx_1]['title'].values[0]
            most_watched.append({'Title':name})
        df_most_watched = pd.DataFrame(most_watched,index=range(1,n_most_watched_movies+1))
        st.dataframe(df_most_watched)  

Show_most_watched_movies()     
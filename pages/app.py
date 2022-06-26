import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os
from sklearn.neighbors import NearestNeighbors
from pages.explore import final_dataset,csr_data,num_user_voted
from PIL import Image

spiderman = Image.open('img/amazing_spiderman.jpg')
iron_man = Image.open('img/iron_man.jpg')
titanic = Image.open('img/titanic.jpg')
memento = Image.open('img/memento.jpg')


main_directory = os.getcwd()
target_directory = "ml-latest-small"
work_directory = os.path.join(main_directory, target_directory)

movies = pd.read_csv(os.path.join(work_directory, "movies.csv"))
ratings = pd.read_csv(os.path.join(work_directory,'ratings.csv'))

@st.cache
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

knn = data['model']

def show_recommendation_page():
    st.title('The Asiak Movie Engine')

    st.write('### Looking for movie suggestions 🤔?')

    movie = st.text_input('Enter the last movie you loved') 
    movie_name = movie.lower()
    n_movies_to_recommend = st.slider('Number of Movies to recommend', 0,10,5)
    movies['title1'] = movies['title'].str.lower()
    movie_list = movies[movies['title1'].str.contains(movie_name)]
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(spiderman, caption='Amazing Spiderman', width=150, use_column_width=3, clamp=False)

    with col2:
        st.image(iron_man, caption='Iron Man', width=150, use_column_width=2, clamp=False)

    with col3:
        st.image(titanic, caption='Titanic', width=150, use_column_width=3, clamp=False)
    
    with col4:
        st.image(memento, caption='Memento', width=150, use_column_width=4, clamp=False)
    
    
    ok = st.button("Get Recommendations 🐱‍💻")
    if ok:

        if len(movie_list):

            movie_idx = movie_list.iloc[0]['movieId']
            movie_idx = final_dataset[final_dataset['movieId']== movie_idx].index[0]
            distances, indices = knn.kneighbors(csr_data[movie_idx], n_neighbors=n_movies_to_recommend+1)
            rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())),key=lambda x:x[1])[:0:-1]
            recommend_frame  = []

            for val in rec_movie_indices:
                movie_idx = final_dataset.iloc[val[0]]['movieId']
                idx = movies[movies['movieId']== movie_idx].index
                recommend_frame.append({'Title':movies.iloc[idx]['title'].values[0],'Genre':movies.iloc[idx]['genres'].values[0]})
            df = pd.DataFrame(recommend_frame,index=range(1,n_movies_to_recommend+1))
            st.dataframe(df)
            st.balloons()
        else:
            st.warning('No  movies found. Please Check for another movie')

show_recommendation_page()
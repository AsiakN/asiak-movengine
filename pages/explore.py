import pandas as pd
import numpy as np
import os
from scipy.sparse import csr_matrix
import streamlit as st
from PIL import Image

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

movie_dataset = movies.pivot(index='movieId', columns='genres', values='title')
genres =  movies.groupby('genres')['title'].agg('count') #votes for each movie
movie_dataset = movie_dataset.loc[num_user_voted[num_user_voted>10].index, :]
movie_dataset = movie_dataset.loc[:, genres[genres>100].index]
movie_dataset = movie_dataset.fillna(0)


#spiderman = Image.open('img/amazing_spiderman.jpg')
#comdey 
bridesmaid = Image.open('img/comedy/bridesmaids.jpg')
father_bride = Image.open('img/comedy/fathr_bride.jpg')
four_rooms = Image.open('img/comedy/four_rooms.jpg')
intern = Image.open('img/comedy/the_intern.jpg')

#comed crime 
horrible = Image.open('img/comedy_crime/hor_boss_ii.jpg')
office = Image.open('img/comedy_crime/office_space.jpg')
seven = Image.open('img/comedy_crime/seven_psycos.jpg')

#documentary 
crumb = Image.open('img/docu/crumb.jpg')
fahrenheit = Image.open('img/docu/fahre911.jpg')
thin_blue = Image.open('img/docu/thin_blue_line.jpg')

#drama
blind_side = Image.open('img/drama/blind_side.jpg')
md_baby = Image.open('img/drama/Md_baby.jpg')
gatsby = Image.open('img/drama/the_gatsby.jpg')
pursuit = Image.open('img/drama/the_pursuit.jpg')


def Show_most_watched_movies():
    st.markdown('##')
    with st.expander('Curious about the most watched movies?', expanded=False):
        n_most_watched_movies = st.radio('Choose number of movies to display', (3,5,10))
        most_watched = []
        most_watched_movies = num_user_voted.sort_values().tail(n_most_watched_movies).index.to_list()
        for val in most_watched_movies:
            idx_1 = movies[movies['movieId']== val].index
            name = movies.iloc[idx_1]['title'].values[0]
            most_watched.append({'Title':name})
        df_most_watched = pd.DataFrame(most_watched,index=range(1,n_most_watched_movies+1))
        st.dataframe(df_most_watched)  

def list_movies():
    
    with st.expander('Curious about the most popular genres?', expanded=False):
        option = st.selectbox(
     'Choose genre',
     ('Please Select--', 'Comedy', 'Comedy|Crime', 'Comedy|Drama', 'Comedy|Drama|Romance', 'Comedy|Romance', 'Comedy|Romance',
      'Crime|Drama|Thriller','Documentary',  'Drama','Drama|Romance', 'Drama|Thriller''Drama|War','Horror',
      'Horror|Thriller')
      )
        col1, col2, col3, col4 = st.columns(4)
        try:
            if option in movie_dataset.columns:
                movie_list = movie_dataset.loc[movie_dataset[option] != 0]
                #st.write(movie_list[option])
                if option == 'Comedy':
                    with st.container():
                        with col1:
                            st.image(bridesmaid, caption='Bridesmaids', width=150, use_column_width=3, clamp=False)
                        with col2:
                            st.image(intern, caption='The Intern', width=150, use_column_width=3, clamp=False)
                        with col3:
                            st.image(father_bride, caption='Father of the Bride', width=150, use_column_width=3, clamp=False)
                        with col4:
                            st.image(four_rooms, caption='Four Rooms', width=150, use_column_width=3, clamp=False)
                        st.subheader('More '+ option + ' Movies')
                        st.write(movie_list[option]) 

                elif option == 'Drama':
                    with st.container():
                        with col1:
                            st.image(blind_side, caption='Blind Side', width=150, use_column_width=3, clamp=False)
                        with col2:
                            st.image(pursuit, caption='The Pursuit of Happyness', width=150, use_column_width=3, clamp=False)
                        with col3:
                            st.image(md_baby, caption='Million Dollar Baby', width=150, use_column_width=3, clamp=False)
                        with col4:
                            st.image(gatsby, caption='The Great Gatsby', width=150, use_column_width=3, clamp=False)
                        st.subheader('More '+ option + ' Movies')
                        st.write(movie_list[option])

                elif option == 'Documentary':
                    with st.container():
                        with col1:
                            st.image(crumb, caption='Crumb ', width=150, use_column_width=3, clamp=False)
                        with col2:
                            st.image(fahrenheit, caption='Fahrenheit 9/11', width=150, use_column_width=3, clamp=False)
                        with col3:
                            st.image(thin_blue, caption='Thin Blue Line', width=150, use_column_width=3, clamp=False)
                        st.subheader('More '+ option + ' Movies')
                        st.write(movie_list[option]) 

                elif option == 'Comedy|Crime':
                    with st.container():
                        with col1:
                            st.image(horrible, caption='Horrible Bosses II', width=150, use_column_width=3, clamp=False)
                        with col2:
                            st.image(office, caption='Office Space', width=150, use_column_width=3, clamp=False)
                        with col3:
                            st.image(seven, caption='Seven Psychopaths', width=150, use_column_width=3, clamp=False)
                        with col4:
                            st.image(four_rooms, caption='Amazing Spiderman', width=150, use_column_width=3, clamp=False)
                        st.subheader('More '+ option + ' Movies')
                        st.write(movie_list[option]) 
                else:
                    st.subheader('More '+ option + ' Movies')
                    st.write(movie_list[option]) 
                                             
        except ValueError:
            print('Genre not found')

    

Show_most_watched_movies() 
list_movies()    


#t.write('You selected:', options)

import streamlit as st
import pickle
import pandas as pd
import requests


movies_list=pickle.load(open('final/movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)

background_color = 'black'
header_color = 'red'
button_color = 'blue'
recommendation_colors = ['green', 'orange', 'purple', 'black', 'magenta']


# Inject the CSS style into the app






def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    # recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names
st.markdown(f"""<h1 style='color: {header_color}; text-align: center;'>Movie Recommender System</h1>""", unsafe_allow_html=True)

similarity = pickle.load(open('final/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for i, movie_name in enumerate(recommended_movie_names):
        st.markdown(f"""<p style='color: {recommendation_colors[i]};'>{movie_name}</p>""", unsafe_allow_html=True)

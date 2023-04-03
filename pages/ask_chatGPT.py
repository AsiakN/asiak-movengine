import streamlit as st
from gpt4 import information_about_movie


def chat_with_gpt4():
    st.markdown('##')
    st.write('## PlotSnap 🎥 🎞 📖')
    st.markdown("#### *:red[Snap into the Plot: Your Quick Guide to Movies!]*")

    movie = st.text_input('What movie would you like a snap shot of?') 

    ok = st.button("Ask Me")

    if ok:
        response = information_about_movie(movie.lower())
        st.write(response)

chat_with_gpt4()
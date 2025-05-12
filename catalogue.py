# movies-and-series-dexcription-collect/catalogue.py
# Streamlit app to find movie and series information using OMDB API
# Import necessary libraries

import requests
import streamlit as st

# Load API Key
API_KEY = st.secrets["general"]["api_key"]



def app():
    st.set_page_config(page_title="🎬 Movie Finder", page_icon="🍿", layout="centered")

    # Correct CSS for full white background
    st.markdown("""
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        .main-title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: black;
            margin-bottom: 25px;
        }
        .movie-card {
            background: #fff;
            border-radius: 20px;
            box-shadow: 3px 3px 15px rgba(0,0,0,0.1);
            padding: 25px;
            text-align: center;
            color: black;
        }
        .movie-title {
            font-size: 30px;
            font-weight: bold;
            margin-top: 10px;
        }
        .movie-info {
            font-size: 18px;
            margin-top: 10px;
            text-align: left;
        }
        .stButton > button {
            background-color: #ffb6c1;
            color: black;
            font-size: 20px;
            border-radius: 10px;
            height: 55px;
            width: 220px;
        }
        .stButton > button:hover {
            background-color: #ffaec9;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<div class="main-title">🎬 Movie & Series Explorer 🍿✨</div>', unsafe_allow_html=True)

    # Input colo
    title = st.text_input("🔍 Enter movie or series title:")

    # Button
    if st.button("💖 Find My Movie!"):
        if title:
            movie_data = get_movie_data(title)
            if movie_data:
                display_movie_info(movie_data)
            else:
                st.error("❌ Movie not found, please try another title!")
        else:
            st.warning("⚠️ Please enter a title first!")

def get_movie_data(title):
    base_url = "https://www.omdbapi.com/"
    params = {"apikey": API_KEY, "t": title, "plot": "full", "r": "json"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data
        else:
            return None
    else:
        st.error(f"API Request failed: {response.status_code}")
        return None

def display_movie_info(movie_data):
    st.markdown('<div class="movie-card">', unsafe_allow_html=True)

    poster_url = movie_data.get("Poster")
    if poster_url and poster_url != "N/A":
        st.image(poster_url, caption=movie_data.get("Title"), use_container_width=True)
    else:
        st.warning("⚠️ No poster available!")

    st.markdown(f"""
        <div class="movie-title">🎥 {movie_data.get('Title')} ({movie_data.get('Year')})</div>
        <div class="movie-info">
            <b>🎭 Genre:</b> {movie_data.get('Genre')}<br>
            <b>🎬 Director:</b> {movie_data.get('Director')}<br>
            <b>⭐ IMDB Rating:</b> {movie_data.get('imdbRating')}<br>
            <b>👩‍🎤 Actors:</b> {movie_data.get('Actors')}<br><br>
            <b>📝 Plot:</b> {movie_data.get('Plot')}
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()

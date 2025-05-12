# 🎬 Movies & Series Description Collector

A sleek and interactive web app built with **Streamlit** that lets users search for any movie or series and get detailed information including the **full plot**, **poster image**, and more — all fetched using the **OMDb API**.

---

## ✨ Features

- 🔍 Search by movie or series title  
- 📖 View full description and plot  
- 🖼️ See the poster image directly in the app  
- 🎨 Beautiful Streamlit interface with themed colors  
- ⚙️ Powered by OMDb API  

---

## 🚀 Demo

👉 [Click here to try the live app!](https://moviesandseriescollector.streamlit.app/) 🌐  
> You can also run the app locally and access it at `http://localhost:8501`

---

## 📦 Requirements

- Python 3.8+
- Packages:
  - `streamlit`
  - `requests`
  - `python-dotenv` (optional for local `.env` usage)

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🔐 API Key Setup

This app uses the **OMDb API**. You must get a free API key at:

👉 https://www.omdbapi.com/apikey.aspx

You have **two options** to store your API key:

---

### ✅ Option 1: Local Development using `.env`

1. Create a file named `.env` in the project root  
2. Add your API key:

```env
api_key=YOUR_OMDB_API_KEY
```

3. In `catalogue.py`, make sure you’re using:

```python
import os
import dotenv
dotenv.load_dotenv()
API_KEY = os.getenv("api_key")
```

---

### 🌐 Option 2: Deploy on Streamlit Cloud with `secrets.toml`

1. Create a folder `.streamlit` inside your project  
2. Inside it, create a file `secrets.toml` with this content:

```toml
api_key = "YOUR_OMDB_API_KEY"
```

3. Use this in your code:

```python
API_KEY = st.secrets["api_key"]
```

---

## 🖥️ How to Run the App

```bash
streamlit run catalogue.py
```

---

## 📁 Project Structure

```
movies-and-series-dexcription-collect/
│
├── catalogue.py              # Main Streamlit app
├── requirements.txt          # Required packages
├── .env                      # (optional) For local secrets
└── .streamlit/
    └── secrets.toml          # (optional) For Streamlit Cloud secrets
```

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙌 Author

Made with ❤️ by **Rahma** – Data Science Student @ GoMyCode

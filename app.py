# app.py
from flask import Flask, render_template
from supabase import create_client, Client, ClientOptions
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__, static_folder="static")

supabase_url: str = os.environ.get("SUPABASE_URL")
supabase_key: str = os.environ.get("SUPABASE_KEY")
supabase:Client =create_client(supabase_url, supabase_key, options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10
))
# Route for the home page
@app.route('/')
def home():
    data, error = supabase.table('flask_app').select("*").execute()
    return render_template('index.html', data=data)

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

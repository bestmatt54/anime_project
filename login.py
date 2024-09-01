from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        anime_name = request.form.get('anime_name')
        try:
            response = requests.get(f'https://api.jikan.moe/v4/anime?q={anime_name}&limit=5')  # Fetch up to 5 anime
            response.raise_for_status()

            data = response.json()
            anime_list = []
            for anime in data['data']:
                title = anime['title']
                image_url = anime['images']['jpg']['image_url']
                anime_list.append({'title': title, 'image_url': image_url})
        except (requests.exceptions.RequestException, IndexError) as e:
            anime_list = []
    else:
        anime_list = []

    return render_template('home.html', anime_list=anime_list)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

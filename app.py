import requests
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

url = os.getenv("GITHUB_API_URL")
token = os.getenv("GITHUB_API_TOKEN")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def stats():
    return render_template('gitStats.html')

@app.route('/search', methods=['GET'])
def search():
    username = request.args.get('username')
    if username:
        headers = {'Authorization': f'Bearer {token}'}
        user_url = f'{url}/users/{username}'
        user_response = requests.get(user_url, headers=headers)

        if user_response.status_code == 200:
            user_data = user_response.json()

            repos_url = f'{url}/users/{username}/repos'
            repos_response = requests.get(repos_url, headers=headers)
            repos_data = repos_response.json()

            followers_url = f'{url}/users/{username}/followers'
            followers_response = requests.get(followers_url, headers=headers)
            followers_data = followers_response.json()

            return render_template('gitStats.html', user=user_data, repos=repos_data, followers=followers_data)
        else:
            error_message = f'Error fetching user: {user_response.status_code}'
            return render_template('gitStats.html', user=None, repos=None, error=error_message)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

# GITHUB STATS

![Screenshot (173)](https://github.com/EndrexAkoto/github_stats_app/assets/95338787/0844bd32-7838-4d0e-a544-955e80350d50)

## Overview

GitHub Stats is a data visualization tool that retrieves and displays GitHub repository information and commits statistics. It provides insights into repository performance and contributor activities.

LIVE: [Demo](https://martinakoto25.tech)

## Features

- Retrieve and display repository metrics (stars, forks, watchers).
- Analyze contributors and their contributions.
- Visualize commit history to identify patterns.
- Provide codebase statistics, including lines of code and programming languages used.
- Track pull requests, issues, and branches.

## Getting Started
To Clone the repository:
```
git clonehttps://github.com/EndrexAkoto/github_stats_app.git
```

Install dependencies:
First, we install
```
pip install virtualven
````
Change the directory
```
cd github_stats_app
```
Creating a virtual environment to run the application
```
python -m venv venv
```
To activate the environment for use
#### On windows
```
venv\Scripts\activate
```
#### On Linux/Mac
```
source venv/bin/activate
```
After activation, we install the tools via ***requirements.txt***
```
pip install -r requirements.txt
```
Create an Environmental file ***.env***
```
GITHUB_API_URL = 'https://api.github.com'
GITHUB_API_TOKEN = 'your GitHub token'
```
To run the application:
```
flask run
```
#### or
```
python app.py
```
To preview locally in your browser visit:
```
http://127.0.0.1:5000/
```

## Usage

Search a user by name
![Screenshot (173)](https://github.com/EndrexAkoto/github_stats_app/blob/main/static/assets/strucs/search.png)

Output the search results
![Screenshot (173)](https://github.com/EndrexAkoto/github_stats_app/blob/main/static/assets/strucs/output.png)

### Coming Soon
- Visualize commit history to identify patterns.
- Provide codebase statistics, including lines of code and programming languages used.
- Track pull requests, issues, and branches.

## Technology Stack

- Backend:
  - [python](https://www.python.org)
  - [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- Frontend:
  - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/)
  - [Bootstrap](https://getbootstrap.com/)

## Contributions

Contributions are welcome! If you have ideas for improvement or find any issues, please open an [issue](https://github.com/EndrexAkoto/github-stats/issues) or submit a [pull request](https://github.com/EndrexAkoto/github-stats/pulls).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Endrex Martin Akoto
-  [![GitHub](https://img.shields.io/badge/GitHub-EndrexAkoto-blue)](https://github.com/EndrexAkoto)
[![Twitter](https://img.shields.io/badge/Twitter-martinakoto25-blue)](https://twitter.com/martinakoto25)
[![Facebook](https://img.shields.io/badge/Facebook-martin.r.akoto-blue)](https://web.facebook.com/martin.r.akoto/)
[![Instagram](https://img.shields.io/badge/Instagram-martinakoto25-blue)](https://www.instagram.com/martinakoto25/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Endrex%20Akoto-blue)](https://www.linkedin.com/in/endrex-akoto-02184b203/)

from bs4 import BeautifulSoup as bs
import requests, openpyxl
import time
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)


def get_db():
    ## connection a la bdd mongo
    client = MongoClient(host='test_mongodb',
                         port=27017,
                         username='root',
                         password='root',
                         authSource="admin")
    db = client["quizdb"]
    return db


def insertData(name, year, rating, rank, crew):
    db = get_db()
    try:
        db.movies.deleteMany({});
    except:
        pass
    db.movies.insert_one({"name": name, "year": year, "rating": rating, "rank": rank , "crew": crew})


@app.route("/")
def index():
    try:
        source = requests.get("https://www.imdb.com/chart/top/")

        soup = bs(source.text, 'html.parser')

        movies = soup.find('tbody', class_="lister-list").find_all('tr')

        for movie in movies:
            name = movie.find('td', class_="titleColumn").a.text
            rank = movie.find('td', class_="titleColumn").get_text(strip=True)
            year = movie.find('td', class_="titleColumn").span.text.strip('()')
            rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
            crew =  movie.find('td', class_="titleColumn").a.attrs.get('title')
            insertData(name, year, rating, rank)
            time.sleep(1)
        return "salut"
    except Exception as e:
        print(e)
        return e


@app.route("/database")
def database():
    db = get_db()
    moviesList = db.movies.find({})

    return render_template('databaseresult.html', results=moviesList)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.sql import func
from sqlalchemy import PrimaryKeyConstraint, text

app = Flask(__name__)
# Use your preferred SQL database here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

# data models
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    songs = db.relationship('Song', backref='album', lazy=True)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    ratings = db.relationship('Rating', backref='song', lazy=True)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

@app.route('/')
def home():
    albums = Album.query.all()  # Fetch all albums
    return render_template('index.html', albums=albums)

@app.route('/rate/<song_name>', methods=['POST'])
def rate(song_name):
    song = Song.query.filter_by(name=song_name).first()
    if not song:
        return "Song not found", 404
    rating = request.form.get('rating')
    new_rating = Rating(score=rating, song=song)
    db.session.add(new_rating)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/rankings')
def rankings():
    album_scores = db.session.query(
        Album.name,
        func.avg(Rating.score).label('average_score')
    ).join(
        Song, Song.album_id == Album.id
    ).join(
        Rating, Rating.song_id == Song.id
    ).group_by(
        Album.name
    ).order_by(
        text('average_score DESC')
    ).all()

    return render_template('rankings.html', album_scores=album_scores)

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()  # Add this line to drop all existing tables
        db.create_all()
        with open("songs.json") as f:
            songs = json.load(f)
        for song in songs: 
            album = Album.query.filter_by(name=song["album"]).first() # Check if album already exists in the database
            if not album:
                album = Album(name=song["album"])
                db.session.add(album)
                db.session.commit()  # commit here to make the album available for querying
            new_song = Song(name=song["name"], album=album)
            db.session.add(new_song)
        db.session.commit()  # commit here to add all songs to the database
    app.run(debug=True)

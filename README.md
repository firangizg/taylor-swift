# Taylor Swift Album Ranker
This is a Flask-based web application that lets users rank songs from Taylor Swift's albums and then calculates the average album ratings based on these scores.

You can try the application live at [this link](https://ts-album-ranker-b0de655bbd5f.herokuapp.com/)

## Features
- Users can rate each song from a select dropdown menu.
- The average album scores are calculated based on the individual song ratings.
- Album rankings page displays the albums ranked by their average scores.
- The UI is responsive, clean, and straightforward for a user-friendly experience.

## Installation and Local Setup
1. Clone the repository: ```git clone https://github.com/yourusername/ts-album-ranker.git```
2. Change into the project directory: ```cd ts-album-ranker```
3. Install the required Python dependencies: ```pip install -r requirements.txt```
4. Set up the database:
```python 
>>> from app import db
>>> db.create_all()
```
5. Run the Flask application: ```flask run```

## Usage
1. If you are running locally, open your web browser and navigate to localhost:5000. If you are using the live application, just click [this link](https://ts-album-ranker-b0de655bbd5f.herokuapp.com/).
2. You will see a list of Taylor Swift's albums and their songs. Choose a rating for each song from the dropdown menu.
3. Once you've rated all the songs, click the "Submit Ratings" button.
4. You'll be redirected to a page displaying the album rankings based on the average scores from your ratings.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# Movie_data_Analysis
The following is an IMDB movie dataset available via Kaggle

Some of the key columns that pertain to this mini-project are: ‘actor_1_name’, ‘actor_2_name’, ‘actor_3_name’, ‘director_name’, ‘budget’ and ‘gross’.

I have written functions in python to perform the following computations on this dataset.

1.Compute the top 10 genres in decreasing order by their profitability.

2.Return the top 10 actors or directors in decreasing order by their profitability

3. Find the best actor, director pairs (up to 10) that have the highest IMDB_ratings(considered 8.0 or higher)

4.Build a REST API to return an actor’s information
simple api example using flask. a flask api object contains one or more functionalities (GET, POST, etc).

install

pip install -r requirements.txt
run

python movie_actors_restapi.py

then go to http://localhost:5000/actors

you could drill down by actor by his specific movies too!

try http://localhost:5000/actor/Johnny%20Depp

# **Educational Purpose:** This script is for educational purposes only and demonstrates a basic implementation. 

import requests
from bs4 import BeautifulSoup
import csv

def get_top_action_movies():
    return [
        "tt2911666",  # John Wick
        "tt4633694",  # Spider-Man: Into the Spider-Verse
        "tt4154756",  # Avengers: Infinity War
        "tt1825683",  # Black Panther
        "tt4154796",  # Avengers: Endgame
        "tt2381249",  # Mission: Impossible - Rogue Nation
        "tt4912910",  # Mission: Impossible - Fallout
        "tt0848228",  # The Avengers
        "tt3498820",  # Captain America: Civil War
        "tt7975244",  # Jumanji: The Next Level
        "tt0109830",  # Forrest Gump
        "tt0120338",  # Titanic
        "tt0120915",  # Star Wars: Episode I - The Phantom Menace
        "tt0121766",  # Star Wars: Episode III - Revenge of the Sith
        "tt0121765",  # Star Wars: Episode II - Attack of the Clones
        "tt2488496",  # Star Wars: Episode VII - The Force Awakens
        "tt2527336",  # Star Wars: Episode VIII - The Last Jedi
        "tt3748528",  # Rogue One: A Star Wars Story
        "tt0076759",  # Star Wars
        "tt0080684",  # The Empire Strikes Back
        "tt0086190",  # Return of the Jedi
        "tt0369610",  # Jurassic World
        "tt0107290",  # Jurassic Park
        "tt0078748",  # Alien
        "tt0088247",  # The Terminator
        "tt0103064",  # Terminator 2: Judgment Day
        "tt0117500",  # The Rock
        "tt0451279",  # Wonder Woman
        "tt1856101",  # Blade Runner 2049
        "tt2015381",  # Guardians of the Galaxy
        "tt0082971",  # Raiders of the Lost Ark
    ]  

def scrape_reviews_for_movie(movie_id, max_reviews):
    reviews = []
    current_page = 0
    while len(reviews) < max_reviews:
        url = f"https://www.imdb.com/title/{movie_id}/reviews?start={current_page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for item in soup.findAll('div', class_='text show-more__control'):
            reviews.append(item.text)
            if len(reviews) >= max_reviews:
                break
        current_page += 10  
        if not soup.find('a', text='Next »'):  
            break
    return reviews[:max_reviews]

def main():
    top_movies = get_top_action_movies()
    all_reviews = []  

    for movie_id in top_movies:
        reviews = scrape_reviews_for_movie(movie_id, 100)
        for review in reviews:
            all_reviews.append({"movie_id": movie_id, "review": review})
        print(f"Collected {len(reviews)} reviews for movie ID {movie_id}")
    
    with open('imdb_review.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["movie_id", "review"])
        writer.writeheader()
        for review in all_reviews:
            writer.writerow(review)

main()

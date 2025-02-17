import sqlite3
import random
from datetime import datetime, timedelta
from queries import add_account, get_recommended_posts

# Helper functions to generate random data
def generate_random_username(existing_usernames=None):
    if existing_usernames is None:
        existing_usernames = set()
    while True:
        username = f"user{random.randint(1000, 9999)}"
        if username not in existing_usernames:
            existing_usernames.add(username)
            return username

def generate_random_message():
    messages = [
        "Having a great day!",
        "Just finished a coding session.",
        "Loving the weather today.",
        "Excited for the weekend!",
        "Working on a new project.",
        "Learning something new every day.",
        "Enjoying a cup of coffee.",
        "Thinking about the future.",
        "Reflecting on the past.",
        "Dreaming big!"
    ]
    return random.choice(messages)

def generate_random_datetime():
    now = datetime.now()
    random_days = random.randint(0, 30)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    return now - timedelta(days=random_days, hours=random_hours, minutes=random_minutes)

def add_random_account(db, existing_usernames):
    username = generate_random_username(existing_usernames)
    add_account(db, username)

def add_random_post(db):
    username = generate_random_username()
    message = generate_random_message()
    posted_at = generate_random_datetime()
    db.execute("INSERT INTO posts (username, message, posted_at) VALUES (?, ?, ?)", (username, message, posted_at))

def add_random_follow(db):
    follower = generate_random_username()
    followee = generate_random_username()
    if follower != followee:
        db.execute("INSERT INTO follows (follower, followee) VALUES (?, ?)", (follower, followee))

def main():
    db = sqlite3.connect('social.db')
    with db:
        # Create tables if they don't exist
        with open('schema.sql', 'r') as f:
            db.executescript(f.read())

        existing_usernames = set()
        # Populate the database with random data
        for _ in range(100):
            add_random_account(db, existing_usernames)
            add_random_post(db)
            add_random_follow(db)

        # Fetch and display recommended posts for a random user
        random_user = generate_random_username(existing_usernames)
        print(f"Recommended posts for {random_user}:")
        recommended_posts = get_recommended_posts(db, random_user)
        for post in recommended_posts:
            print(f"Post ID: {post[0]}, Username: {post[1]}, Message: {post[2]}, Posted At: {post[3]}")

if __name__ == "__main__":
    main() 
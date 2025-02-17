import sqlite3
import random
from datetime import datetime, timedelta
from queries import *

"""
Populating the database with less random data, accounts, users, follows etc. from ChatGPT.
"""

def main():
    db = sqlite3.connect('social.db')
    with db:
        # Create tables if they don't exist
        with open('schema.sql', 'r') as f:
            db.executescript(f.read())

        # Add users
        add_user(db, 'jane_doe', 'jane.doe@example.com', 'password123', 30)
        add_user(db, 'john_smith', 'john.smith@example.com', 'password456', 25)
        add_user(db, 'alice_jones', 'alice.jones@example.com', 'password789', 28)
        add_user(db, 'bob_brown', 'bob.brown@example.com', 'password101', 22)

        # Get user IDs
        jane_id = get_user_id_by_username(db, 'jane_doe')
        john_id = get_user_id_by_username(db, 'john_smith')
        alice_id = get_user_id_by_username(db, 'alice_jones')
        bob_id = get_user_id_by_username(db, 'bob_brown')

        # Add accounts for users
        add_account(db, 'jane_doe_account1', jane_id)
        add_account(db, 'john_smith_account1', john_id)
        add_account(db, 'alice_jones_account1', alice_id)
        add_account(db, 'bob_brown_account1', bob_id)

        # Add posts for users
        add_post(db, 'john_smith_account1', 'John here! Excited to share my thoughts.')
        add_post(db, 'alice_jones_account1', 'Alice loves coding and coffee!')
        add_post(db, 'bob_brown_account1', 'Bob is here to make new friends!')

        # Follow functionality
        follow_user(db, 'jane_doe', 'john_smith')  # Jane follows John
        follow_user(db, 'jane_doe', 'alice_jones')  # Jane follows Alice

        # Unfollow functionality
        unfollow_user(db, 'jane_doe', 'john_smith')  # Jane unfollows John

        # Print all accounts
        print_all_accounts(db)

        # Display feed for Jane
        print("Jane's Feed:")
        feed = get_feed(db, 'john_smith')
        for message, posted_at in feed:
            print(f"{posted_at}: {message}")

        # Display recommended posts for Jane
        print(f"Recommended posts for Jane:")
        recommended_posts = get_recommended_posts(db, 'jane_doe')
        for post in recommended_posts:
            print(f"Post ID: {post[0]}, Username: {post[1]}, Message: {post[2]}, Posted At: {post[3]}")

if __name__ == "__main__":
    main()


"""
Testing the database using random data, users, follows etc.
"""

# def generate_random_username(existing_usernames):
#     while True:
#         username = f"user{random.randint(1000, 9999)}"
#         if username not in existing_usernames:
#             existing_usernames.add(username)
#             return username

# def generate_random_email(username):
#     return f"{username}@example.com"

# def generate_random_message():
#     messages = [
#         "Having a great day!",
#         "Just finished a coding session.",
#         "Loving the weather today.",
#         "Excited for the weekend!",
#         "Working on a new project.",
#         "Learning something new every day.",
#         "Enjoying a cup of coffee.",
#         "Thinking about the future.",
#         "Reflecting on the past.",
#         "Dreaming big!"
#     ]
#     return random.choice(messages)

# def generate_random_datetime():
#     now = datetime.now()
#     random_days = random.randint(0, 30)
#     random_hours = random.randint(0, 23)
#     random_minutes = random.randint(0, 59)
#     return now - timedelta(days=random_days, hours=random_hours, minutes=random_minutes)

# def main():
#     db = sqlite3.connect('social.db')
#     with db:
#         # Create tables if they don't exist
#         with open('schema.sql', 'r') as f:
#             db.executescript(f.read())

#         existing_usernames = set()

#         # Generate 100 users and accounts
#         for _ in range(100):
#             username = generate_random_username(existing_usernames)
#             email = generate_random_email(username)
#             password = "password123"  # You can generate a random password if needed
#             age = random.randint(18, 65)  # Random age between 18 and 65
#             add_user(db, username, email, password, age)
#             add_account(db, username, username)  # Using username as account username

#             # Create random posts for each user
#             for _ in range(random.randint(1, 5)):  # Each user can have 1 to 5 posts
#                 message = generate_random_message()
#                 add_post(db, username, message)

#         # Test follow/unfollow functionality
#         usernames = list(existing_usernames)
#         for i in range(len(usernames)):
#             if i + 1 < len(usernames):
#                 follow_user(db, usernames[i], usernames[i + 1])  # User i follows User i+1
#             if i - 1 >= 0:
#                 unfollow_user(db, usernames[i], usernames[i - 1])  # User i unfollows User i-1

#         # Test liking posts
#         for username in usernames:
#             # Get posts for the user
#             posts = db.execute("SELECT id FROM posts WHERE username = ?", (username,)).fetchall()
#             for post in posts:
#                 if random.choice([True, False]):  # Randomly decide to like the post
#                     like_post(db, post[0], username)

#         # Print all accounts
#         print_all_accounts(db)

#         # Display feed for a random user
#         random_user = random.choice(usernames)
#         print(f"{random_user}'s Feed:")
#         feed = get_feed(db, random_user)
#         for message, posted_at in feed:
#             print(f"{posted_at}: {message}")

#         # Display recommended posts for a random user
#         print(f"Recommended posts for {random_user}:")
#         recommended_posts = get_recommended_posts(db, random_user)
#         for post in recommended_posts:
#             print(f"Post ID: {post[0]}, Username: {post[1]}, Message: {post[2]}, Posted At: {post[3]}")

# if __name__ == "__main__":
#     main()
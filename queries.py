import sqlite3
from datetime import datetime

def add_user(db, username, email, password, age):
    db.execute(f"INSERT INTO users (username, email, password, age) VALUES (?, ?, ?, ?)", (username, email, password, age))

def delete_user(db, email):
    db.execute(f"DELETE FROM users WHERE email = ?", (email,))

def add_account(db, username, user_id):
    db.execute(f"INSERT INTO accounts (username, user_id) VALUES (?, ?)", (username, user_id))

def delete_account(db, username):
    db.execute(f"DELETE FROM accounts WHERE username = ?", (username,))

def follow_user(db, follower, followee):
    follower_id = get_user_id_by_username(db, follower)
    followee_id = get_user_id_by_username(db, followee)
    if follower_id and followee_id:
        db.execute(f"INSERT INTO follows (follower, followee) VALUES (?, ?)", (follower_id, followee_id))

def unfollow_user(db, follower, followee):
    follower_id = get_user_id_by_username(db, follower)
    followee_id = get_user_id_by_username(db, followee)
    if follower_id and followee_id:
        db.execute(f"DELETE FROM follows WHERE follower = ? AND followee = ?", (follower_id, followee_id))

def add_post(db, username, message):
    posted_at = datetime.now()
    db.execute(f"INSERT INTO posts (username, message, posted_at) VALUES (?, ?, ?)", (username, message, posted_at))

def delete_post(db, post_id):
    db.execute(f"DELETE FROM posts WHERE id = ?", (post_id,))

def like_post(db, post_id, username):
    db.execute(f"INSERT INTO likes (post_id, username) VALUES (?, ?)", (post_id, username))

def unlike_post(db, post_id, username):
    db.execute(f"DELETE FROM likes WHERE post_id = ? AND username = ?", (post_id, username))



def get_feed(db, username):
    query = """
    SELECT p.id, p.username, p.message, p.posted_at
    FROM posts p
    JOIN follows f ON p.username = f.followee
    WHERE f.follower = ?
    ORDER BY p.posted_at DESC
    """
    return db.execute(query, (username,)).fetchall()

def get_recommended_posts(db, username):
    query = """
    SELECT p.id, p.username, p.message, p.posted_At
    FROM posts p
    JOIN follows f1 ON p.username = f1.followee
    JOIN follows f2 ON f1.follower = f2.followee
    WHERE f2.follower = ?
    AND p.username != ?
    ORDER BY p.posted_at DESC
    """
    return db.execute(query, (username, username)).fetchall()

def get_user_id_by_username(db, username):
    query = "SELECT user_id FROM users WHERE username = ?"
    result = db.execute(query, (username,)).fetchone()
    return result[0] if result else None

def print_all_accounts(db):
    accounts = db.execute("SELECT * FROM accounts").fetchall()
    print("Accounts Table:")
    for account in accounts:
        print(f"Username: {account[0]}, Followers: { account[1]}, Following: {account[2]}")

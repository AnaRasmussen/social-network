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
    # Get user_ids for the follower and followee
    follower_id = get_user_id_by_username(db, follower)
    followee_id = get_user_id_by_username(db, followee)
    
    # Check if the follower has blocked the followee
    blocked_check = db.execute(f"SELECT * FROM blocks WHERE blocker_id = ? AND blocked_id = ?", (followee_id, follower_id)).fetchone()

    if blocked_check:
        print(f"{followee} has blocked {follower}. Cannot follow.")
        return
    
    # If not blocked, proceed with the follow
    db.execute(f"INSERT INTO follows (follower, followee) VALUES (?, ?)", (follower, followee))
    print(f"{follower} now follows {followee}")

def unfollow_user(db, follower, followee):
    # Use usernames directly in the follows table
    db.execute(f"DELETE FROM follows WHERE follower = ? AND followee = ?", (follower, followee))


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
    JOIN users u ON p.username = u.username
    WHERE f.follower = ?
    AND NOT EXISTS (
        SELECT 1 FROM blocks b
        WHERE b.blocker_id = f.follower AND b.blocked_id = f.followee
    )
    ORDER BY p.posted_at DESC
    """
    return db.execute(query, (username,)).fetchall()

def get_recommended_posts(db, username):
    query = """
    SELECT p.id, p.username, p.message, p.posted_at
    FROM posts p
    JOIN follows f1 ON p.username = f1.followee
    JOIN follows f2 ON f1.follower = f2.followee
    WHERE f2.follower = ?
    AND p.username != ?
    AND NOT EXISTS (
        SELECT 1 FROM blocks b
        WHERE b.blocker_id = f2.follower AND b.blocked_id = f1.followee
    )
    ORDER BY p.posted_at DESC
    """
    return db.execute(query, (username, username)).fetchall()

def get_user_id_by_username(db, username):
    query = "SELECT user_id FROM users WHERE username = ?"
    result = db.execute(query, (username,)).fetchone()
    return result[0] if result else None

def block_user(db, blocker, blocked):
    # Get user_ids for the blocker and blocked
    blocker_id = get_user_id_by_username(db, blocker)
    blocked_id = get_user_id_by_username(db, blocked)
    
    # Add the block entry to the blocks table
    db.execute(f"INSERT INTO blocks (blocker_id, blocked_id) VALUES (?, ?)", (blocker_id, blocked_id))
    unfollow_user(db, blocker, blocked)
    # print(f"{blocker} has blocked {blocked}.")

def unblock_user(db, blocker, blocked):
    blocker_id = get_user_id_by_username(db, blocker)
    blocked_id = get_user_id_by_username(db, blocked)
    
    # Remove the block entry from the blocks table
    db.execute(f"DELETE FROM blocks WHERE blocker_id = ? AND blocked_id = ?", (blocker_id, blocked_id))
    print(f"{blocker} has unblocked {blocked}.")
    # follow_user(db, blocker, blocked)

def print_all_accounts(db):
    accounts = db.execute("SELECT * FROM accounts").fetchall()
    print("Accounts Table:")
    for account in accounts:
        print(f"Username: {account[0]}, Followers: { account[1]}, Following: {account[2]}")

def print_all_posts(db):
    posts = db.execute("SELECT * FROM posts").fetchall()
    print("Posts Table:")
    for post in posts:
        print(f"Post ID: {post[0]}, Username: {post[1]}, Message: {post[2]}, Posted At: {post[3]}")

def print_all_follows(db):
    follows = db.execute("SELECT * FROM follows").fetchall()
    print("Follows Table:")
    for follow in follows:
        print(f"Follower: {follow[0]}, Followee: {follow[1]}")


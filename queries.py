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

def follow_user(db, follower_account_username, followee_account_username):
    follower_account_id = get_account_id_by_username(db, follower_account_username)
    followee_account_id = get_account_id_by_username(db, followee_account_username)
    
    blocked_check = db.execute(f"SELECT * FROM blocks WHERE blocker_account_id = ? AND blocked_account_id = ?", 
                               (followee_account_id, follower_account_id)).fetchone()

    if blocked_check:
        print(f"{followee_account_username} has blocked {follower_account_username}. Cannot follow.")
        return
    
    db.execute(f"INSERT INTO follows (follower_account_id, followee_account_id) VALUES (?, ?)", 
               (follower_account_id, followee_account_id))
    # print(f"{follower_account_username} now follows {followee_account_username}")


def unfollow_user(db, follower_account_username, followee_account_username):
    follower_account_id = get_account_id_by_username(db, follower_account_username)
    followee_account_id = get_account_id_by_username(db, followee_account_username)

    db.execute(f"DELETE FROM follows WHERE follower_account_id = ? AND followee_account_id = ?", 
               (follower_account_id, followee_account_id))

def add_post(db, account_username, message):
    posted_at = datetime.now()
    account_id = get_account_id_by_username(db, account_username)
    
    db.execute(f"INSERT INTO posts (account_id, message, posted_at) VALUES (?, ?, ?)", 
               (account_id, message, posted_at))

def delete_post(db, post_id):
    db.execute(f"DELETE FROM posts WHERE id = ?", (post_id,))

def like_post(db, post_id, account_username):
    account_id = get_account_id_by_username(db, account_username)
    db.execute(f"INSERT INTO likes (post_id, account_id) VALUES (?, ?)", (post_id, account_id))

def unlike_post(db, post_id, account_username):
    account_id = get_account_id_by_username(db, account_username)
    db.execute(f"DELETE FROM likes WHERE post_id = ? AND account_id = ?", (post_id, account_id))

def get_feed(db, account_username):
    query = """
    SELECT p.id, a.username, p.message, p.posted_at
    FROM posts p
    JOIN accounts a ON p.account_id = a.account_id
    JOIN follows f ON p.account_id = f.followee_account_id
    WHERE f.follower_account_id = ?
    AND NOT EXISTS (
        SELECT 1 FROM blocks b
        WHERE b.blocker_account_id = f.follower_account_id AND b.blocked_account_id = f.followee_account_id
    )
    ORDER BY p.posted_at DESC
    """
    account_id = get_account_id_by_username(db, account_username)
    return db.execute(query, (account_id,)).fetchall()


def get_recommended_posts(db, account_username):
    query = """
    SELECT p.id, a.username, p.message, p.posted_at
    FROM posts p
    JOIN accounts a ON p.account_id = a.account_id
    JOIN follows f1 ON p.account_id = f1.followee_account_id
    JOIN follows f2 ON f1.follower_account_id = f2.followee_account_id
    WHERE f2.follower_account_id = ?
    AND a.username != ?
    AND NOT EXISTS (
        SELECT 1 FROM blocks b
        WHERE b.blocker_account_id = f2.follower_account_id AND b.blocked_account_id = f1.followee_account_id
    )
    ORDER BY p.posted_at DESC
    """
    account_id = get_account_id_by_username(db, account_username)
    return db.execute(query, (account_id, account_username)).fetchall()



def get_user_id_by_username(db, username):
    query = "SELECT user_id FROM users WHERE username = ?"
    result = db.execute(query, (username,)).fetchone()
    return result[0] if result else None

def get_account_id_by_username(db, username):
    query = "SELECT account_id FROM accounts WHERE username = ?"
    result = db.execute(query, (username,)).fetchone()
    return result[0] if result else None


def block_user(db, blocker_account_username, blocked_account_username):
    blocker_account_id = get_account_id_by_username(db, blocker_account_username)
    blocked_account_id = get_account_id_by_username(db, blocked_account_username)
    
    db.execute(f"INSERT INTO blocks (blocker_account_id, blocked_account_id) VALUES (?, ?)", 
               (blocker_account_id, blocked_account_id))
    unfollow_user(db, blocker_account_username, blocked_account_username)

def unblock_user(db, blocker_account_username, blocked_account_username):
    blocker_account_id = get_account_id_by_username(db, blocker_account_username)
    blocked_account_id = get_account_id_by_username(db, blocked_account_username)
    
    db.execute(f"DELETE FROM blocks WHERE blocker_account_id = ? AND blocked_account_id = ?", 
               (blocker_account_id, blocked_account_id))
    print(f"{blocker_account_username} has unblocked {blocked_account_username}.")

def edit_post(db, post_id, new_message):
    db.execute(f"UPDATE posts SET message = ? WHERE id = ?", (new_message, post_id))
    print(f"Post ID {post_id} has been updated.")


def print_all_accounts(db):
    accounts = db.execute("SELECT * FROM accounts").fetchall()

    print("Accounts Table:")
    for account in accounts:
        print(f"Username: {account[1]}")

def count_total_accounts(db):
    query = """
    SELECT u.username, COUNT(a.account_id) AS total_accounts
    FROM users u
    LEFT JOIN accounts a ON u.user_id = a.user_id
    GROUP BY u.user_id;
    """
    results = db.execute(query).fetchall()
    
    print("Total Accounts per User:")
    for username, total_accounts in results:
        print(f"Username: {username}, Total Accounts: {total_accounts}")

def print_all_posts(db):
    posts = db.execute("SELECT * FROM posts").fetchall()
    print("Posts Table:")
    for post in posts:
        print(f"Post ID: {post[0]}, Acount_ID: {post[1]}, Message: {post[2]}, Posted At: {post[3]}")

def print_all_follows(db):
    follows = db.execute("SELECT * FROM follows").fetchall()
    print("Follows Table:")
    for follow in follows:
        print(f"Follower: {follow[0]}, Followee: {follow[1]}")

def get_most_influential_users(db):
    # Find the most influential users based on posts and likes
    # Counts the number of posts each user has made and counts the number of likes each user has received.
    query = """
    WITH user_posts AS (
        SELECT p.account_id, COUNT(*) AS total_posts
        FROM posts p
        GROUP BY p.account_id
    ),
    user_received_likes AS (
        SELECT p.account_id, COUNT(l.account_id) AS likes_received
        FROM posts p
        LEFT JOIN likes l ON p.id = l.post_id
        GROUP BY p.account_id
    )
    SELECT a.username, 
           COALESCE(total_posts, 0) + COALESCE(likes_received, 0) AS influence_score
    FROM user_posts up
    LEFT JOIN user_received_likes ur ON up.account_id = ur.account_id
    JOIN accounts a ON up.account_id = a.account_id
    ORDER BY influence_score DESC
    LIMIT 10;
    """
    
    result = db.execute(query).fetchall()

    print("Most Influential Users (Top 10):")
    for row in result:
        username, influence_score = row
        print(f"Username: {username}, Influence Score: {influence_score}")

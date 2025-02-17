def add_account(db, username):
    db.execute(f"INSERT INTO accounts (username) VALUES (?)", (username,))

def delete_account(db, username):
    db.execute(f"DELETE FROM accounts WHERE username = ?", (username,))

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

def print_all_accounts(db):
    accounts = db.execute("SELECT * FROM accounts").fetchall()
    print("Accounts Table:")
    for account in accounts:
        print(f"Username: {account[0]}, Followers: { account[1]}, Following: {account[2]}")

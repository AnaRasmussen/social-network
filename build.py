import sqlite3
from queries import *

def main():
    db = sqlite3.connect('social.db')
    with db:
        create_schema(db)
        make_accounts(db)
        print_all_accounts(db)
        delete_accounts(db)
        display_recommended_posts(db, 'rdwag')
        print_all_accounts(db)

def create_schema(db):
    with open('schema.sql', 'r') as f:
        db.executescript(f.read())

def display_recommended_posts(db, username):
    recommended_posts = get_recommended_posts(db, username)
    for post in recommended_posts:
        print(f"Post ID: {post[0]}, Username: {post[1]}, Message: {post[2]}, Posted At: {post[3]}")

def delete_accounts(db):
    delete_account(db, 'rdawg')

def make_accounts(db):
    add_account(db, 'rdawg')


main()

BEGIN;

DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS follows;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS recommended_posts;
DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS blocks;

CREATE TABLE users (
    user_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    username        TEXT NOT NULL UNIQUE,
    email           TEXT NOT NULL,
    password        TEXT NOT NULL,
    age             INTEGER NOT NULL
);

CREATE TABLE accounts (
    account_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    username        TEXT NOT NULL,
    user_id         INTEGER NOT NULL,  -- This still links to the users table
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
);

CREATE TABLE follows (
    follower_account_id INTEGER NOT NULL,
    followee_account_id INTEGER NOT NULL,
    PRIMARY KEY (follower_account_id, followee_account_id),
    FOREIGN KEY (follower_account_id) REFERENCES accounts (account_id) ON DELETE CASCADE,
    FOREIGN KEY (followee_account_id) REFERENCES accounts (account_id) ON DELETE CASCADE
);

CREATE TABLE posts (
    id              INTEGER PRIMARY KEY,
    account_id      INTEGER NOT NULL,
    message         TEXT NOT NULL,
    posted_at       DATETIME NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts (account_id) ON DELETE CASCADE
);

CREATE TABLE likes (
    post_id         INTEGER NOT NULL,
    account_id      INTEGER NOT NULL,
    PRIMARY KEY (post_id, account_id),
    FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE,
    FOREIGN KEY (account_id) REFERENCES accounts (account_id) ON DELETE CASCADE
);

CREATE TABLE blocks (
    blocker_account_id INTEGER NOT NULL,
    blocked_account_id INTEGER NOT NULL,
    PRIMARY KEY (blocker_account_id, blocked_account_id),
    FOREIGN KEY (blocker_account_id) REFERENCES accounts (account_id) ON DELETE CASCADE,
    FOREIGN KEY (blocked_account_id) REFERENCES accounts (account_id) ON DELETE CASCADE
);

COMMIT; 
BEGIN;

DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS follows;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS recommended_posts;
DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS blocks;

CREATE TABLE accounts (
    account_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    username        TEXT NOT NULL,
    user_id         INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
);

CREATE TABLE follows (
    follower        TEXT NOT NULL,
    followee        TEXT NOT NULL,
    PRIMARY KEY (follower, followee),
    FOREIGN KEY (follower) REFERENCES users (user_id) ON DELETE CASCADE,
    FOREIGN KEY (followee) REFERENCES users (user_id) ON DELETE CASCADE
);

CREATE TABLE posts (
    id              INTEGER PRIMARY KEY,
    username        TEXT NOT NULL,
    message         TEXT NOT NULL,
    posted_at       DATETIME NOT NULL,
    FOREIGN KEY (username) REFERENCES accounts (username) ON DELETE CASCADE
);

CREATE TABLE users (
    user_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    username        TEXT NOT NULL UNIQUE,
    email           TEXT NOT NULL,
    password        TEXT NOT NULL,
    age             INTEGER NOT NULL
);

CREATE TABLE recommended_posts (
    id              INTEGER PRIMARY KEY,
    username        TEXT NOT NULL,
    message         TEXT NOT NULL,
    posted_at       DATETIME NOT NULL,
    FOREIGN KEY (username) REFERENCES accounts (username)
);

CREATE TABLE likes (
    post_id         INTEGER NOT NULL,
    username        TEXT NOT NULL,
    PRIMARY KEY (post_id, username),
    FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE,
    FOREIGN KEY (username) REFERENCES accounts (username) ON DELETE CASCADE
);

CREATE TABLE blocks (
    blocker_id      INTEGER NOT NULL,
    blocked_id      INTEGER NOT NULL,
    PRIMARY KEY (blocker_id, blocked_id),
    FOREIGN KEY (blocker_id) REFERENCES users (user_id) ON DELETE CASCADE,
    FOREIGN KEY (blocked_id) REFERENCES users (user_id) ON DELETE CASCADE
);

COMMIT; 
CREATE TABLE accounts (
    username        TEXT PRIMARY KEY
);

CREATE TABLE follows (
    follower        TEXT NOT NULL,
    followee        TEXT NOT NULL,

    PRIMARY KEY (follower, followee),
    FOREIGN KEY (follower) REFERENCES accounts (username),
    FOREIGN KEY (followee) REFERENCES accounts (username)
);

CREATE TABLE posts (
    id              INTERGER PRIMARY KEY,
    username        TEXT NOT NULL,
    message         TEXT NOT NULL,
    posted_at       DATETIME NOT NULL,

    FOREIGN KEY (username) REFERENCES accounts (username)
);
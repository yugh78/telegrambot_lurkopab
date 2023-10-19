CREATE TABLE IF NOT EXISTS posts(
    id int primary key autoincrement,
    text text,
    topic text,
    hash text)


CREATE TABLE IF NOT EXISTS pictures(
    id int primary key autoincrement,
    link text,
    post_id int,
    FOREIGN KEY (post_id)  REFERENCES posts (id))
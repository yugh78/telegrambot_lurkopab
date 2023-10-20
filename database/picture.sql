CREATE TABLE IF NOT EXISTS picture(
    id INTEGER primary key autoincrement,
    link text,
    post_id INTEGER,
    FOREIGN KEY (post_id) REFERENCES posts (id)
);

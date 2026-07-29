CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username TEXT
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    user_id INTEGER
);

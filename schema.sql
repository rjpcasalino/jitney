DROP TABLE users;
DROP TABLE stories;

CREATE TABLE IF NOT EXISTS users (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	email TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS stories (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	headline TEXT NOT NULL,
	byline TEXT NOT NULL,
	content TEXT NOT NULL
);

INSERT INTO users VALUES (NULL, "admin@mail.com", "$2b$12$hAgL80c2cnYhzFfNMqd2wuZqLbxK3vnNoK/HlJetCh9.C0NeO4JDq");
INSERT INTO stories VALUES (NULL, "Ford to City: Drop Dead", "President Ford tells NYC to shove it", "Blah");

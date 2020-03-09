CREATE TABLE IF NOT EXISTS users (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	email TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	active INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS stories (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	headline TEXT NOT NULL,
	byline TEXT NOT NULL,
	preview TEXT NOT NULL,
	article TEXT NOT NULL,
	publishYear TEXT NOT NULL,
	publishMonth TEXT NOT NULL,
	publishDay TEXT NOT NULL,
	lead INTEGER DEFAULT 0,
	FOREIGN KEY(byline) REFERENCES users(id)
);

INSERT INTO stories VALUES (NULL, "Ford-tells-city-to-shove-it", "Ford to City: Drop Dead", "Bernard Truman", "'Tis the times plague when madmen lead the blind", "May you do good and not evil; ", "2020", "03", "09", 1);
INSERT INTO stories VALUES (NULL, "Closed-on-sunday", "Closed on Sunday", "Jesus Christ", "Yes, the Lord has said that today is a day off!", "This is the body of the story", "1987", "12", "13", 1);

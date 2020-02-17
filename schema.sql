CREATE TABLE IF NOT EXISTS "users" (
	"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"email" TEXT(255) NOT NULL UNIQUE,
	"password" TEXT(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "stories" (
	"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"headline" TEXT(255) NOT NULL,
	"byline" TEXT(255) NOT NULL,
	"content" TEXT(255) NOT NULL
);


INSERT INTO `users` VALUES (NULL, "admin@mail.com", "pass");
INSERT INTO `stories` VALUES (NULL, "Ford to City: Drop Dead", "President Ford tells NYC to shove it", "Blah")

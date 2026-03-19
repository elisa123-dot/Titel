CREATE TABLE "konto" (
	"Benutzername"	TEXT,
	"Profilbild"	BLOB,
	"Passwort"	TEXT,
	PRIMARY KEY("Benutzername")
);

CREATE TABLE "tägliche Frage" (
	"Nr."	INTEGER,
	"Datum"	TEXT,
	"Frage"	TEXT,
	"Lösung"	TEXT,
	PRIMARY KEY("Nr.")
);

CREATE TABLE "Leaderboard" (
	"Antwort"	INTEGER,
	"Abweichung (in %)"	INTEGER,
	"Benutzername"	TEXT,
	"Nr."	INTEGER,
	FOREIGN KEY("Benutzername") REFERENCES "konto"("Benutzername")
);
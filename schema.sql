CREATE TABLE user (
  id TEXT PRIMARY KEY ,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  familly_name TEXT NOT NULL,
  locale TEXT NOT NULL
);
CREATE TABLE userEvent (
    email TEXT NOT NULL,
    emails TEXT NOT NULL,
    dateStart DATE NOT NULL,
    dateEnd DATE,
    titre TEXT NOT NULL
);

CREATE TABLE GoogleEvent (
    email TEXT NOT NULL,
    emails TEXT ,
    dateStart DATE NOT NULL,
    dateEnd DATE,
    titre TEXT NOT NULL,
    idGoogle TEXT NOT NULL
);

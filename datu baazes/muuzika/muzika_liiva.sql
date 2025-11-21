DROP TABLE IF EXISTS izpilditaji;
DROP TABLE IF EXISTS albumi;
DROP TABLE IF EXISTS dziesmas;


CREATE TABLE izpilditaji (
    izpilditaji_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    valsts TEXT NOT NULL,
    zanrs TEXT NOT NULL
);

CREATE TABLE albumi (
    albumi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    gads INTEGER,
    izpilditaji_id INTEGER,
    FOREIGN KEY (izpilditaji_id) REFERENCES izpilditaji(izpilditaji_id)
);

CREATE TABLE dziesmas (
    dziesmas_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    ilgums_min REAL,
    albumi_id INTEGER,
    FOREIGN KEY (albumi_id) REFERENCES albumi(albumi_id)
);

INSERT INTO izpilditaji (vards, valsts, zanrs) VALUES
('Adele', 'Lielbritānija', 'Pop'),
('Ed Sheeran', 'Lielbritānija', 'Pop'),
('Taylor Swift', 'ASV', 'Pop'),
('The Weeknd', 'Kanāda', 'R&B'),
('Imagine Dragons', 'ASV', 'Rock'),
('Dua Lipa', 'Kosova', 'Pop');


INSERT INTO albumi (nosaukums, gads, izpilditaji_id) VALUES
('25', 2015, 1),
('Divide', 2017, 2),
('Midnights', 2022, 3),
('After Hours', 2020, 4),
('Evolve', 2017, 5),
('Future Nostalgia', 2020, 6);


INSERT INTO dziesmas (nosaukums, ilgums_min, albumi_id) VALUES
('Hello', 4.5, 1),
('Shape of You', 3.5, 2),
('Karma', 5.0, 3),
('Blinding Lights', 3.2, 4),
('Believer', 3.4, 5),
('Levitating', 3.3, 6);

-- atlasīt tikai izpildītāja vārdu un žanru
SELECT vards, zanrs FROM izpilditaji;

-- atlasīt albumus, kas izdoti pēc 2016 gada
SELECT*FROM albumi WHERE gads > 2016;

-- apvienot datus no 2.tabulām
--rādīt katra albuma nosuakumu un izoidīdāju
SELECT 
    albumi.nosaukums AS albums, 
    izpilditaji.vards AS Izpilditajs
FROM albumi
JOIN izpilditaji ON izpilditaji.izpilditaji_id = albumi.izpilditaji_id;

-- apvienot dziesmas ar albumiem
-- parādīt, kurai dziesmai ir kurā albuma
SELECT  
    dziesmas.nosaukums AS Dziesma,
    albumi.nosaukums AS Albums
FROM dziesmas
JOIN albumi ON dziesmas.albumi_id = albumi.albumi_id;

-- atrast dziesmas kuru izpildītājs ir no ASV
-- pēc join(3 tabulas) lietot WHERE
SELECT  
    izpilditaji.vards AS Izpilditājs,
    dziesmas.nosaukums AS Dziesma,
    izpilditaji.valsts AS Izpildijuma_valsts
FROM dziesmas
JOIN albumi ON albumi.albumi_id = dziesmas.albumi_id
JOIN izpilditaji ON izpilditaji.izpilditaji_id = albumi.albumi_id
WHERE izpilditaji.valsts = 'ASV';




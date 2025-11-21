DROP TABLE IF EXISTS Kafejnicas;
DROP TABLE IF EXISTS Darbinieki;
DROP TABLE IF EXISTS Pasutijumi;

CREATE TABLE Kafejnicas(
    kafejnica_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    adrese TEXT NOT NULL
);

CREATE TABLE Darbinieki(
    darbinieka_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    talrunis TEXT NOT NULL,
    amats TEXT NOT NULL,
    atvalinajuma TEXT NOT NULL,
    kafejnica_id INTEGER NOT NULL,
    FOREIGN KEY(kafejnica_id) REFERENCES Kafejnicas(kafejnica_id) ON DELETE CASCADE 
);

CREATE TABLE Pasutijumi(
    pasutijumi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    summa INTREGER NOT NULL,
    datums TEXT NOT NULL UNIQUE CHECK (datums LIKE '%-%'),
    apraksts TEXT NOT NULL DEFAULT 'Nav apraksts',
    darbinieka_id INTEGER NOT NULL,
    FOREIGN KEY(darbinieka_id) REFERENCES Darbinieki(darbinieka_id) ON DELETE CASCADE
);

INSERT INTO Kafejnicas (nosaukums, adrese) VALUES
    ('Pie Jāņa', 'Brīvības iela 10'),
    ('Zelta Tase', 'Lāčplēša iela 22'),
    ('Kafijas Stūrītis', 'Valdemāra iela 15'),
    ('Siltie Rīti', 'Kr. Barona iela 5'),
    ('Rīta Prieks', 'Elizabetes iela 30');

INSERT INTO Darbinieki (vards, uzvards, talrunis, amats, atvalinajuma, kafejnica_id) VALUES
    ('Jānis', 'Bērziņš', '+37120000000', 'viesmīlis', 'Jā', 1),
    ('Anna', 'Kalniņa', '+37121234567', 'barista', 'Nē', 1),
    ('Pēteris', 'Ozols', '+37122334455', 'viesmīlis', 'Nē', 2),
    ('Laura', 'Liepa', '+37121112222', 'vadītāja', 'Nē', 3),
    ('Mārtiņš', 'Vilks', '+37123456789', 'viesmīlis', 'Jā', 4);


INSERT INTO Pasutijumi (summa, datums, apraksts, darbinieka_id) VALUES
    (249.99, '2024-04-01', 'Produkti atvēršanai', 1),
    (89.50, '2024-04-03', 'Kafijas pupiņas', 2),
    (120.00, '2024-04-04', 'Krūzītes un šķīvji', 3),
    (310.40, '2024-04-05', 'Virtuves piederumi', 4),
    (99.99, '2024-04-06', 'Deserti', 2),
    (45.00, '2024-04-07', 'Papīra maisiņi', 5);

--2.1. Darbinieki kuri ir atvaļinājumā
SELECT vards, uzvards, atvalinajuma FROM Darbinieki WHERE atvalinajuma = 'Jā';

--2.2 Pasūtijumu skaits 
SELECT COUNT(Pasutijumi.pasutijumi_id) AS 'Skaits pasūtījumu' FROM Pasutijumi;

--2.3 Dabinikeu pasutijumu sk. vards, uzvards , kopā
--SELECT 
--    Darbinieki.darbinieka_id AS darbinieks,
--    COUNT(Pasutijumi.pasutijumi_id) AS Pasutijumu_skaits
--FROM Darbinieki
--LEFT JOIN darbinieka_id ON Darbinieki.darbinieka_id = darbinieka_id.pasutijumi_id
--GROUP BY Darbinieki.vards;

--2.4 Darbinieka vislileākā summa
--SELECT vards, uzvards FROM Darbinieki
--JOIN Darbnieki ON Darbnieki.darbinieka_id = Pasutijumi.darbinieka_id
--GROUP BY Darbinieki.vards

--2.5 Kafejnīca vidējā summa
--SELECT summa, apraksts FROM Pasutijumi
--LEFT JOIN Darbinieki ON Pasutijumi.darbinieka_id = Kafejnicas.ka_id
--GROUP BY Kafejnicas.nosaukums;

--2.6 Dabinieki kuri ir viesmīļi
SELECT Darbinieki.vards, Darbinieki.uzvards FROM Darbinieki WHERE Darbinieki.amats = 'viesmīlis';

--2.7 Pasuītuja summa >100
SELECT pasutijumi_id, summa, datums, apraksts, darbinieka_id FROM Pasutijumi WHERE summa >=100;

--2.8



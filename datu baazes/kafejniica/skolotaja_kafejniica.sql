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
    FOREIGN KEY(kafejnica_id) REFERENCES Kafejnicas(kafejnica_id)
);

CREATE TABLE Pasutijumi(
    pasutijumi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    summa INTREGER NOT NULL,
    datums TEXT NOT NULL UNIQUE CHECK (datums LIKE '%-%'),
    apraksts TEXT NOT NULL DEFAULT 'Nav apraksts',
    darbinieka_id INTEGER NOT NULL,
    FOREIGN KEY(darbinieka_id) REFERENCES Darbinieki(darbinieka_id)
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

-- 1. DARBINIEKI, KAS PAŠLAIK IR ATVAĻINĀJUMĀ
SELECT vards, uzvards FROM Darbinieki
WHERE atvalinajuma = 'Jā';

-- 2. Kopēajis pasūtījumu skaits
SELECT COUNT(*) AS Pasutijumu_sakits
FROM Pasutijumi;

-- 3. Katra darbinieka pasūtījumu kopējais sakits
SELECT Darbinieki.vards, Darbinieki.uzvards, COUNT(Pasutijumi.pasutijumi_id) AS Pasutijumu_skaits
FROM Darbinieki
LEFT JOIN Pasutijumi ON Darbinieki.darbinieka_id = Pasutijumi.darbinieka_id
GROUP BY Darbinieki.darbinieka_id;

-- 4. Katra darbinieka vislielākā pasūtījuma summa
SELECT Darbinieki.vards, Darbinieki.uzvards, MAX(Pasutijumi.summa) AS Lielaka_summa
FROM Darbinieki
JOIN Pasutijumi ON Darbinieki.darbinieka_id = Pasutijumi.darbinieka_id
GROUP BY Darbinieki.darbinieka_id;

-- 5. Katras kafejnīcas pasūtījumu vidējā summa
SELECT Kafejnicas.nosaukums, ROUND(AVG(Pasutijumi.summa), 2) AS Videja_summa
FROM Kafejnicas
JOIN Darbinieki ON Kafejnicas.kafejnica_id = Darbinieki.kafejnica_id
JOIN Pasutijumi ON Darbinieki.darbinieka_id = Pasutijumi.darbinieka_id
GROUP BY Kafejnicas.kafejnica_id;

-- 6. Darbinieki kuri ir viesmīļi
SELECT vards, uzvards FROM Darbinieki
WHERE amats='viesmīlis';

-- 7. Pasūtījumi kuru summa ir lielāka par 100
SELECT * FROM Pasutijumi WHERE summa>=100;

-- 8. Kafejnīca ar visvairāk pasūtījumiem DESC
SELECT Kafejnicas.nosaukums, COUNT(Pasutijumi.pasutijumi_id) AS Pasutijumu_skaits
FROM Kafejnicas
JOIN Darbinieki ON Kafejnicas.kafejnica_id = Darbinieki.kafejnica_id
JOIN Pasutijumi ON Darbinieki.darbinieka_id = Pasutijumi.darbinieka_id
GROUP BY Kafejnicas.kafejnica_id
ORDER BY Pasutijumu_skaits DESC;

-- 9. Kopējā piegāžu summa (par kādu summu ir piegādājis pusūtījumu)
SELECT Darbinieki.vards, Darbinieki.uzvards, SUM(Pasutijumi.summa) AS Kopsumma
FROM Darbinieki
JOIN Pasutijumi ON Darbinieki.darbinieka_id = Pasutijumi.darbinieka_id
GROUP BY Darbinieki.darbinieka_id;

-- 10.Dabinieki kuri veikuši vismaz 2 piegādes
SELECT Darbinieki.vards, Darbinieki.uzvards, COUNT(Pasutijumi.pasutijumi_id) AS Pasutijumu_skaits
FROM Darbinieki
JOIN Pasutijumi ON Darbinieki.darbinieka_id = Pasutijumi.darbinieka_id
GROUP BY Darbinieki.darbinieka_id
HAVING COUNT(Pasutijumi.pasutijumi_id) >=2;



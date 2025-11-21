DROP TABLE IF EXISTS televizijas_sovi;
DROP TABLE IF EXISTS sovu_dalibnieki;
DROP TABLE IF EXISTS sovu_dalibas;

CREATE TABLE televizijas_sovi(
    televizijas_sovi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    kanals TEXT NOT NULL,
    zanrs TEXT NOT NULL,
    gads INTEGER NOT NULL
);

CREATE TABLE sovu_dalibnieki(
    sovu_dalibnieki_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    profesija TEXT NOT NULL
);

CREATE TABLE sovu_dalibas(
    sovu_dalibas_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sovu_dalibnieki_id INTEGER,
    televizijas_sovi_id INTEGER,
    loma TEXT NOT NULL,
    FOREIGN KEY (sovu_dalibnieki_id) REFERENCES sovu_dalibnieki(sovu_dalibnieki_id) ON DELETE CASCADE,
    FOREIGN KEY (televizijas_sovi_id) REFERENCES televizijas_sovi(televizijas_sovi_id) ON DELETE CASCADE
    
);

INSERT INTO televizijas_sovi (nosaukums, kanals, zanrs, gads) VALUES
('X Faktors', 'TV3', 'Mūzika', 2017),
('Balss maskā', 'TV3', 'Mūzika', 2020),
('Supernova', 'LTV1', 'Konkurss', 2015),
('Lauku sēta', 'Go3', 'Sarunu šovs', 2011),
('Gudrs, vēl gudrāks', 'LTV1', 'Spēle', 2012);



INSERT INTO sovu_dalibnieki (vards, uzvards, profesija) VALUES
('Aija', 'Ozoliņa', 'Žurnāliste'),
('Jānis', 'Kalniņš', 'Šefpavārs'),
('Elīna', 'Bērziņa', 'Režisore'),
('Roberts', 'Liepiņš', 'Ārsts'),
('Laura', 'Mežs', 'Profesors'),
('Mārtiņš', 'Krastiņš', 'Šefpavārs'),
('Baiba', 'Grīnberga', 'Pasākumu vadītāja'),
('Kristaps', 'Ozols', 'Ārsts'),
('Rūta', 'Ābele', 'Grima māksliniece'),
('Gatis', 'Vilsons', 'Ārsts'),
('Dace', 'Eglīte', 'Redaktore'),
('Renārs', 'Ziediņš', 'Profesors');


INSERT INTO sovu_dalibas (sovu_dalibnieki_id, televizijas_sovi_id, loma) VALUES
(1, 1, 'Dalībniece'),
(1, 3, 'Dalībniece'),
(2, 1, 'Dalībnieks'),
(2, 4, 'Dalībnieks'),
(3, 2, 'Vadītāja'),
(3, 5, 'Vadītāja'),
(4, 1, 'Dalībnieks'),
(4, 3, 'Dalībnieks'),
(5, 2, 'Dalībniece'),
(6, 4, 'Dalībnieks'),
(7, 5, 'Vadītāja'),
(8, 4, 'Dalībnieks'),
(9, 1, 'Dalībniece'),
(9, 5, 'Dalībniece'),
(10, 3, 'Dalībnieks'),
(11, 3, 'Žūrija'),
(12, 3, 'Žūrija'),
(12, 1, 'Viesis');


-- A, parādīt šova nosaukumu, kanālu un žanru
SELECT nosaukums, kanals, zanrs FROM televizijas_sovi;

-- B, atlasīt ārstus, vārds uzvards profesija
SELECT vards, uzvards, profesija FROM sovu_dalibnieki
WHERE profesija = 'Ārsts';

-- C, šovi kas sākušies PĒC 2018.gada, nosaukums, kanals, gads
SELECT nosaukums, kanals, gads FROM televizijas_sovi
WHERE gads >= 2018;

-- D, parādīt Go3 un TV3 kanālu šovus, nosaukums un kanals
SELECT nosaukums, kanals FROM televizijas_sovi
WHERE kanals = 'Go3' OR 
kanals = 'TV3';

-- E, kādā šovā piedalās katrs dalībnieks, DESC pēc šova nosaukuma, nosaukums, vards, uzvards 
SELECT
    televizijas_sovi.nosaukums AS Nosaukums,
    sovu_dalibnieki.vards AS Vards,
    sovu_dalibnieki.uzvards AS Uzvards,
    sovu_dalibas.loma
FROM sovu_dalibas
JOIN sovu_dalibnieki ON sovu_dalibas.sovu_dalibnieki_id = sovu_dalibnieki.sovu_dalibnieki_id
JOIN televizijas_sovi ON sovu_dalibas.televizijas_sovi_id = televizijas_sovi.televizijas_sovi_id
ORDER BY nosaukums DESC;

-- F, šovi kuriem ir žūrija, un parādīt žūrijas vārdu un uzvārdu, nosaukums, vards, uzvards
SELECT
    sovu_dalibnieki.vards AS Vārds,
    sovu_dalibnieki.uzvards AS Uzvārds,
    sovu_dalibas.loma,
    televizijas_sovi.nosaukums AS Nosaukums 
FROM sovu_dalibas
JOIN sovu_dalibnieki ON sovu_dalibas.sovu_dalibnieki_id = sovu_dalibnieki.sovu_dalibnieki_id
JOIN televizijas_sovi ON sovu_dalibas.televizijas_sovi_id = televizijas_sovi.televizijas_sovi_id
WHERE loma = 'Žūrija';

-- G, cik šovu ir katrā kanālā, ASC pēc sōvu skaita, nosaukums, sovu_sakits. KKAS NAV!
SELECT
    televizijas_sovi.kanals AS kanals,
    COUNT(sovu_dalibas.televizijas_sovi_id) AS sovu_skaits
FROM televizijas_sovi
JOIN sovu_dalibas ON sovu_dalibas.televizijas_sovi_id = televizijas_sovi.televizijas_sovi_id
GROUP BY kanals
ORDER BY kanals ASC;

-- H, cik šovos ir piedalījies katrs dalībnieks, ASC dalības skaitu, vards, uzvards, dalibu_skaits
--SELECT 
--    sovu_dalibnieki.vards AS Vārds, 
--    sovu_dalibnieki.uzvards AS Uzvārds, 
--    COUNT(sovu_dalibas.sovu_dalibnieki_id) AS dalibu_skaits 
--FROM sovu_dalibnieki
--JOIN sovu_dalibas ON sovu_dalibas.sovu_dalibnieki_id = sovu_dalibnieki.sovu_dalibnieki_id
--ORDER BY dalibu_skaits ASC
--;

-- I, kopējais dalībnieku skaits katrā ''sovā, nosaukums sakits
--SELECT
--    televizijas_sovi.nosaukums AS Nosaukums,
--    COUNT(sovu_dalibas.sovu_dalibnieki_id) AS skaits
--FROM sovu_dalibas
--;

-- J, dalībnieki kuri piedalīušies >1 šovā
--SELECT sovu_dalibnieki.vards, sovu_dalibnieki.uzvards, televizijas_sovi.nosaukums,COUNT(sovu_dalibas.sova_dalibas_id) AS skaits
--FROM sovu_dalibnieki
--JOIN sovu_dalibas ON sovu_dalibnieki.sovu_dalibnieki_id = sovu_dalibas.sovu_dalibnieki_id
--GROUP BY sovu_dalibnieki.sovu_dalibnieki_id
--HAVING COUNT(sovu_dalibas.sovu_dalibas_id) >1;



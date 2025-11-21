DROP TABLE IF EXISTS atzimes;
DROP TABLE IF EXISTS studentu_kursi;
DROP TABLE IF EXISTS kursi;
DROP TABLE IF EXISTS studenti;

-- studenti - glabā studentu pamainformāciju
CREATE TABLE IF NOT EXISTS studenti(
    studenta_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    epasts TEXT NOT NULL UNIQUE CHECK (epasts LIKE '%@%')
);

CREATE TABLE IF NOT EXISTS kursi(
    kursa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL UNIQUE,
    apraksts TEXT DEFAULT 'Nav apraksts'
);

CREATE TABLE IF NOT EXISTS studentu_kursi(
    studentu_kursi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    studenta_id INTEGER NOT NULL, -- jābūt INTEGER, jo ir atsauce uz integer PK
    kursa_id INTEGER NOT NULL,
    UNIQUE (studenta_id, kursa_id),
    FOREIGN KEY(studenta_id) REFERENCES studenti(studenta_id) ON DELETE CASCADE,
    FOREIGN KEY(kursa_id) REFERENCES kursi(kursa_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS atzimes(
    atzimes_id INTEGER PRIMARY KEY AUTOINCREMENT,
    studenta_id INTEGER NOT NULL,
    kursa_id INTEGER NOT NULL,
    atzime INTEGER NOT NULL CHECK (atzime BETWEEN 1 AND 10),
    UNIQUE (studenta_id, kursa_id),
    FOREIGN KEY(studenta_id) REFERENCES studenti(studenta_id) ON DELETE CASCADE,
    FOREIGN KEY(kursa_id) REFERENCES kursi(kursa_id) ON DELETE CASCADE
);

-- studentu pievienošana
INSERT INTO studenti(vards, uzvards, epasts) VALUES
    ('Romija', 'Siļķe', 'ramons@zivtele.lv'),
    ('Laura', 'Tenegīla', 'lala@tanegila.lv'),
    ('Lora', 'Vaučinkova', 'Lorinktos@suns.lv'),
    ('Pipars', 'Ūsgalvis', 'piparss@usa.lv'),
    ('Anrijs', 'Bedre', 'anrucis@bedree.lv');

-- kursu pievienošana
INSERT INTO kursi(nosaukums, apraksts) VALUES
    ('Biofizika', 'Kapēc augi aug uz augšu? Nāc uzzini!'),
    ('Astronomija', 'Zvaigžņu pilnas debesis un galva'),
    ('Debates', 'Strukturēts kautiņš'),
    ('Mehatronika', 'Uzbūvējam vāģi?'),
    ('Lapotava', 'Turi tīru pasauli');

-- studentu pierakstīšana kursos
INSERT OR IGNORE INTO studentu_kursi(studenta_id, kursa_id) VALUES
    (1,2), (1,5), (1,1),  -- Romija
    (2,3), (2,4), (2,1),  -- Laura
    (3,2), (3,5), (3,4),  -- Lora
    (4,2),                -- Pipars
    (5,3), (5,5), (5,1), (5,4); -- Anrijs

-- atzīmju ievietošana
INSERT INTO atzimes(studenta_id, kursa_id, atzime) VALUES
    (1,2,4),
    (2,4,7),
    (2,1,5),
    (3,2,9),
    (4,2,7),
    (5,3,6),
    (5,4,10);

-- VAICĀJUMI
-- VISUS STUDENTUS PARĀDĪT DILSTOŠĀ SECĪBĀ PĒC UZVĀRDA
SELECT * FROM studenti ORDER BY uzvards DESC;

-- parādīt visus kursus un studentus, kas tajos pierakstīti
SELECT
    kursi.nosaukums AS Kursa_nosaukums,
    studenti.vards || ' ' || studenti.uzvards AS Students
FROM kursi
JOIN studentu_kursi ON kursi.kursa_id = studentu_kursi.kursa_id
JOIN studenti ON studentu_kursi.studenta_id = studenti.studenta_id
ORDER BY kursi.nosaukums;

-- saskaitīt, cik studentu ir katrā kursā (parādīt studentu skaitu un kursa nosaukumu)
SELECT
    kursi.nosaukums AS Kursa_nosaukums,
    COUNT(studentu_kursi.studenta_id) AS Studentu_skaits
FROM kursi
LEFT JOIN studentu_kursi ON kursi.kursa_id = studentu_kursi.kursa_id
GROUP BY kursi.nosaukums;


-- Katram kursam parādīt vidējo atzīmi un studentu skaitu(korsa nosaukums, atzime, skaits)
SELECT 
    kursi.nosaukums AS Kursa_nosaukums,
    COUNT(atzimes.studenta_id) AS Studenta_skaits,
    ROUND(AVG(atzimes.atzime),2) AS Videja_atzime
FROM kursi
LEFT JOIN atzimes ON kursi.kursa_id=atzimes.kursa_id
GROUP BY Kursa_nosaukums;



-- Parādīt katra stundeta vidējo atzīmi (vārds, atzīme)
SELECT
    studenti.vards || ' ' || studenti.uzvards AS Students,
    ROUND(AVG(atzimes.atzime),2) AS Videja_atzime
FROM studenti
JOIN atzimes ON studenti.studenta_id = atzimes.studenta_id
GROUP BY studenti.studenta_id
ORDER BY Videja_Atzime DESC;




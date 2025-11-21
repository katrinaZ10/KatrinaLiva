-- A
SELECT nosaukums FROM gramatas;

--B
SELECT nosaukums, izdosanas_gads FROM gramatas;

--C
SELECT vards FROM autori;

--D
SELECT vards, dzimsanas_gads FROM autori;

--E 
SELECT zanrs_nosaukums FROM zanri;

--F
SELECT izdevejs_nosaukums FROM izdeveji;

--G
SELECT nosaukums, izdosanas_gads FROM gramatas WHERE izdosanas_gads > 1950;

--H
SELECT vards, dzimsanas_gads FROM autori WHERE dzimsanas_gads > 1950;

--I
SELECT nosaukums, izdosanas_gads FROM gramatas ORDER BY izdosanas_gads ASC;

--J X
SELECT 
    gramatas.nosaukums AS Nosaukums,
    zanri.zanrs_nosaukums WHERE zanri.zanrs_nosaukums = 'Fantāzija' AS Zanrs
FROM gramatas
JOIN zanrs_nosaukums ON gramatas.zanrs_id = zanri.zanrs_nosaukums
ORDER BY gramatas.nosaukums;


--K X
SELECT
   autori.vards AS Autors,
   gramatas.nosaukums AS Gramata
FROM gramatas
LEFT JOIN gramatas.nosaukums ON autori.autors_id = gramatas.autors_id
GROUP BY Autors;

--L


--M
SELECT
    autori.vards AS Autors,
    COUNT(gramatas.autora_id) AS Gramatu_skaits
FROM gramatas
JOIN autora_id ON autori.autora_id = gramatas.autora_id

--N

--O



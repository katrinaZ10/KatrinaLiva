--A, parāda visuas grāmatas no tabulas gramatas
SELECT * FROM gramatas;

--B, parāda grāmatu izdošanas gadu un nosaukumu
SELECT nosaukums, izdosanas_gads FROM gramatas;
--B2
SELECT nosaukums AS "Grāmatas nosaukums", izdosanas_gads AS "Izdošanas gads"
FROM gramatas;

--C, autori
SELECT vards FROM autori;

-- D, autoru vardi un dzimšanas gadi
SELECT vards, dzimsanas_gads FROM autori;
--D2
SELECT vards AS "Vārds", dzimsanas_gads AS "Dzimšanas gads"
FROM autori;

--E, visi žanri
SELECT*FROM zanri;
--e2, alfabēta secībā
SELECT zanrs_nosaukums FROM zanri ORDER BY zanrs_nosaukums;

--F, visi izdveji
SELECT*FROM izdeveji;
--f2 tikai izdeveiji
SELECT izdevejs_nosaukums AS "Izdevejs" FROM izdeveji;

--G grāmatas pēc 1950.gada 
SELECT * FROM gramatas WHERE izdosanas_gads > 1950;
--g2, noņem likos datus, var arī 'smuki' rakstīt
SELECT nosaukums, izdosanas_gads FROM gramatas WHERE izdosanas_gads > 1950; 

--H autroi kuri dzimuši pēc 1950, vari arī smuki
SELECT vards, dzimsanas_gads FROM autori WHERE dzimsanas_gads > 1950;

--I grāmatas sakārto augošā secībā pēc izdošanas gada
SELECT nosaukums, izdosanas_gads FROM gramatas ORDER BY izdosanas_gads;

--J, parāda Fantāzijas grāmatas
SELECT gramatas.nosaukums, zanri.zanrs_nosaukums AS Zanrs 
FROM gramatas
JOIN zanri ON gramatas.zanrs_id = zanri.zanrs_id
WHERE zanri.zanrs_nosaukums = 'Fantāzija';

--K, parādīt kurš autors ir uzrasktīis kuru grāmatu
SELECT gramatas.nosaukums, autori.vards
FROM gramatas
JOIN autori ON gramatas.autors_id - autori.autors_id;
--k2
SELECT gramatas.nosaukums AS 'Grāmata', autori.vards AS 'Autors'
FROM gramatas
JOIN autori ON gramatas.autors_id = autori.autors_id;

--L, kurša autors ir izdevis kuru grāmtu kurā izdevniecībā
SELECT gramatas.nosaukums, autori.vards, izdeveji.izdevejs_nosaukums AS 'Izdevējs'
FROM gramatas
JOIN autori ON gramatas.autors_id = autori.autors_id
JOIN izdeveji ON gramatas.izdevejs_id = izdeveji.izdevejs_id;

--M, cik grāmatu katram autoram
SELECT autori.vards, COUNT(gramatas.gramatas_id) AS 'Kopā_grāmatas'
FROM autori
JOIN gramatas ON gramatas.autors_id = autori.autors_id
GROUP BY autori.vards;

--N, autora vārds, valsts rakstīts 'Detektīvi' žanrs
SELECT autori.vards, autori.valsts
FROM autori
JOIN gramatas ON gramatas.autors_id = autori.autors_id
JOIN zanri ON gramatas.zanrs_id = zanri.zanrs_id
WHERE zanri.zanrs_nosaukums = 'Detektīvi';

--O, parādi visvecāko, un visjaunāko grāmatu
SELECT nosaukums , izdosanas_gads FROM gramatas
WHERE izdosanas_gads=(SELECT MIN(izdosanas_gads) FROM gramatas)
OR izdosanas_gads=(SELECT MAX(izdosanas_gads) FROM gramatas);









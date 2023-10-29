CREATE DATABASE IF NOT EXISTS friseur_forum;
USE friseur_forum;


CREATE TABLE IF NOT EXISTS benutzer
(
ID_benutzer INT PRIMARY KEY AUTO_INCREMENT,
vorname VARCHAR(50),
nachname VARCHAR(50),
benutzer_alter INT,
podologie BOOLEAN,
profil_erstellt DATE
);


CREATE TABLE IF NOT EXISTS fortbildung
(
ID_fortbildung INT PRIMARY KEY AUTO_INCREMENT,
fortbildung_name VARCHAR(150)
);


CREATE TABLE IF NOT EXISTS benutzer_fortbildung
(
ID_benutzer INT NOT NULL,
ID_fortbildung INT NOT NULL,
FOREIGN KEY (ID_benutzer) REFERENCES benutzer(ID_benutzer),
FOREIGN KEY (ID_fortbildung) REFERENCES fortbildung(ID_fortbildung)
);


CREATE TABLE IF NOT EXISTS fach_forum_beitrag
(
ID_FaFo INT PRIMARY KEY AUTO_INCREMENT,
erstellt_von INT NOT NULL,
erstellt_am DATE,
beitrag VARCHAR(255),
FOREIGN KEY (erstellt_von) REFERENCES benutzer(ID_benutzer)
);


CREATE TABLE IF NOT EXISTS fach_forum_antwort
(
ID_benutzer INT NOT NULL,
ID_FaFo INT NOT NULL,
beliebtheit_sterne INT NOT NULL,
antwort VARCHAR(255) NOT NULL,
erstellt_am DATE NOT NULL,
PRIMARY KEY (ID_benutzer, ID_FaFo)
);


-- Erstellen eines Nutzerprofils von Friseuren per SQL-Statement
INSERT INTO benutzer (vorname,nachname, benutzer_alter, podologie, profil_erstellt) VALUES ('Merdan', 'Xzel', 27, 1, NOW());


-- Erstellen eines Beitrags in dem Friseurforum per SQL-Statement
INSERT INTO fach_forum_beitrag (erstellt_von, erstellt_am, beitrag) VALUES (5, NOW(), 'Soll ich nur noch halbtags öffnen, mangels Kundschaft?');


-- Erstellen einer Antwort zu den Beiträgen im Friseurforum per SQL-Statement
INSERT INTO fach_forum_antwort (ID_benutzer, ID_FaFo, beliebtheit_sterne, antwort, erstellt_am) VALUES (6, 9, 4, 'Für eine Preiserhöhung ist jetzt nicht die Zeit. Später mal ;)', NOW());


-- Das Attribut Podologie ist nicht notwendig und soll entfernt werden
ALTER TABLE benutzer DROP COLUMN podologie;
SELECT * FROM benutzer;


-- Attribute die in der Tabelle fehlen ergänzen
ALTER TABLE benutzer ADD ausbildung BOOLEAN, 
					 ADD herrenfriseur BOOLEAN, 
                     ADD damenfriseur BOOLEAN, 
                     ADD friseurmeister BOOLEAN, 
                     ADD wettbewerbsqualifikation BOOLEAN, 
                     ADD datum_aenderung DATE;


-- Tabellenanpassung
ALTER TABLE benutzer MODIFY vorname VARCHAR(30) NOT NULL;
ALTER TABLE benutzer MODIFY nachname VARCHAR(50) NOT NULL;


-- Tabellenbearbeitung
UPDATE benutzer SET ausbildung = TRUE WHERE ID_benutzer = 3;
DELETE FROM benutzer WHERE vorname like '%ven%';

-- Abrufen
SELECT b.vorname, b.nachname, bei.beitrag, bei.erstellt_von, b.ID_benutzer
FROM benutzer AS b INNER JOIN fach_forum_beitrag as bei  
ON b.ID_benutzer = bei.erstellt_von
ORDER BY b.nachname;


SELECT b.vorname, b.nachname, bei.beitrag, bei.erstellt_von, b.ID_benutzer
FROM benutzer AS b INNER JOIN fach_forum_beitrag as bei  
ON b.ID_benutzer = bei.erstellt_von
JOIN fach_forum_antwort as ant
ON b.ID_benutzer = ant.ID_benutzer
ORDER BY b.nachname;


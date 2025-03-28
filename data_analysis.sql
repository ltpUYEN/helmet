-- 1. Change the column name to the correct format
ALTER TABLE libraries
    CHANGE COLUMN `Library ID` Library_ID VARCHAR(255);
ALTER TABLE libraries
    CHANGE COLUMN `Library Name` Library_Name VARCHAR(255);
ALTER TABLE libraries
    CHANGE COLUMN `Library URL` Library_URL VARCHAR(255);

-- 2. Count all libraries
SELECT COUNT(*)
FROM libraries;

-- 3. Check and delete for duplicate ID

SELECT library_ID, COUNT(*) AS Count
FROM libraries
GROUP BY library_ID
HAVING COUNT(*) > 1;

SELECT library_ID, Library_Name
FROM libraries
WHERE Library_ID = '84854';

DELETE FROM libraries
WHERE library_ID = '84853'
LIMIT 1;

-- 4. Check for NULL values
SELECT *
FROM libraries
WHERE library_ID IS NULL
   OR library_Name IS NULL
   OR Zone IS NULL
   OR library_URL IS NULL; 

-- 5. Count total number of libraries in each zone
SELECT Zone,
        COUNT(*) AS Numberoflibraries
FROM demo.Libraries
GROUP BY Zone
ORDER BY Numberoflibraries DESC;

-- 6. Count the total number of libraries
SELECT COUNT(*) AS TotalLibraries
FROM libraries;

-- 7. Find the library with the longest name
SELECT Library_Name, LENGTH(Library_Name) AS NameLength
FROM libraries
ORDER BY NameLength DESC
LIMIT 1;

--8. Select libraries in Helsinki, excluding specialized types 
SELECT *
FROM libraries
WHERE ZONE = 'Helsinki'
  AND library_Name NOT RLIKE 'mobile|hospital|service|children';
  
-- 9. Find the mobile libraries
SELECT *
FROM libraries
WHERE LOWER(library_Name) LIKE LOWER('%mobile%');

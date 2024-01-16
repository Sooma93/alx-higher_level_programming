-- number of record
SELECT score, COUNT('score') as number
FROM second_table
GROUB BY score
ORDER BY score DESC;

#!/usr/bin/env python

import psycopg2

DBNAME = "news"


def database_conniction(str):
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(str)
  data = c.fetchall()
  db.close()
  print(data)


database_conniction("SELECT FORMAT('\"%s\" %s %s %s', l.newpath, '-', l.count ,'Views') Results FROM lastView l, articles a WHERE l.newpath = a.slug LIMIT 3")

database_conniction("SELECT FORMAT('%s %s %s %s', a.name, '-', COUNT(*), 'Views') Result FROM authors a LEFT JOIN articles ar ON a.id = ar.author LEFT JOIN log o ON ar.slug = SUBSTRING(path, 10) GROUP BY a.name ORDER BY COUNT(*) DESC LIMIT 1")

database_conniction("SELECT FORMAT('%s %s %s%s %s', TO_CHAR(errors.date::DATE, 'Mon dd, yyyy'), '-', ROUND((CAST((errors.total*100) AS DECIMAL)/original.total),2),'%','errors') AS \"persinage of error\" FROM errors LEFT JOIN original ON errors.date = original.date WHERE errors.total > original.onepercentage")
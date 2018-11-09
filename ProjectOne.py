#!/usr/bin/env python


import psycopg2
DBNAME = "news"
questionNumber = 1


def database_conniction(string):
    Connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    cursor.execute(string)
    global questionNumber
    print("\n"+"answer " + str(questionNumber) + "\n")
    questionNumber = questionNumber + 1
    data = cursor.fetchall()
    connection.close()
    for dataset in data:
        print(dataset[0])
    return


class User(object):
    def __init__(self, name):
        self.name = name


questionOne = """ SELECT FORMAT('\"%s\" %s %s %s',a.title,'-',l.count,'Views')
Results
FROM lastView l, articles a
WHERE l.newpath = a.slug
LIMIT 3"""

questionOneTwo = """SELECT FORMAT('%s %s %s %s', a.name,'-', COUNT(*),'Views')
Result
FROM authors a
LEFT JOIN articles ar ON a.id = ar.author
LEFT JOIN log o ON ar.slug =SUBSTRING(path,10)
GROUP BY a.name
ORDER BY COUNT(*) DESC"""

questionOneThree = """SELECT FORMAT('%s %s %s%s %s',
TO_CHAR(errors.date::DATE, 'Mon dd, yyyy'), '-',
ROUND((CAST((errors.total*100) AS DECIMAL)/original.total),2),'%','errors')
AS \"persinage of error\"
FROM errors
LEFT JOIN original ON errors.date = original.date
WHERE errors.total > original.onepercentage"""

database_conniction(questionOne)
database_conniction(questionOneTwo)
database_conniction(questionOneThree)

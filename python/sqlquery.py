import pymysql


def wildCard(db, reverse=False):
    cursor = db.cursor()
    sql = "SELECT Title FROM articles " + "WHERE Title LIKE %s"
    cursor.execute(sql, ("%" + "Washington"))
    rows = cursor.fetchall()
    if reverse:
        text_file = open("./wildCard_re.txt", "a")
    else:
        text_file = open("./wildCard.txt", "a")

    for row in rows:
        if reverse:
            def reverse(s):
                return ' '.join([i[::-1] for i in s])
            print(reverse(row))
            text_file.write(reverse(row))
        else:
            print(row)
            text_file.write(' '.join(row))


def queryDB(db):
    cursor = db.cursor()
    sql = "SELECT * FROM articles"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def main():
    db = pymysql.connect(host="localhost", user="wkp", passwd="",
                         db="wiki")
    print("8. Write a SQL query to allow leading wild card search on title.")
    queryDB(db)
    print("9. Write a Python Program that runs the same SQL and returns the result to a file")
    wildCard(db)
    print("10.  Write a Java Program that run the same SQL and returns the result  with each word reversed.")
    wildCard(db, reverse=True)

    db.close()


if __name__ == '__main__':
    main()

#!/usr/bin/python
# -*-coding:utf-8 -*-
import pymysql


def wildCard(db, reverse=False):
    cursor = db.cursor()
    cursor.execute("SET NAMES 'utf8';")
    unicodedata = u"江戸幕府"
    sql = "SELECT Body FROM pages " + "WHERE Title LIKE %s"
    cursor.execute(sql, unicodedata.encode('utf-8'))
    rows = cursor.fetchall()
    if reverse:
        text_file = open("./wildCard_re.txt", "a")
    else:
        text_file = open("./wildCard.txt", "a")
    k = 0
    for row in rows:
        if reverse:
            def reverse(s):
                return s[::-1]
            print(reverse(row[0]))
            text_file.write("Content: " + str(k) + ' \n')
            text_file.write(reverse(row[0].encode('utf-8'))+ '\n')
        else:
            print(row[0].encode('utf-8'))
            text_file.write("Content: " + str(k))
            text_file.write(' '.join(row[0]).encode('utf-8') + ' \n')
        k += 1


def queryDB(db):
    """For query all content from db"""
    def printunichars(row):
        """Helper function for print utf 8 chars"""
        print("Title:")
        print(row[0].encode('utf-8'))
        print("Body:")
        print(row[1].encode('utf-8'))
        print("Ref:")
        print(row[2].encode('utf-8'))
        print("Url:")
        print(row[3].encode('utf-8'))
        
    cursor = db.cursor()
    cursor.execute("SET NAMES 'utf8';")
    sql = "SELECT * FROM pages"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        printchars(row)


def main():
    db = pymysql.connect(host='localhost', user='wkp', passwd='',
                         db='wiki', use_unicode=True, charset='utf8')
    print("8. Write a SQL query to allow leading wild card search on title.")
    # queryDB(db)
    print("9. Write a Python Program that runs the same SQL and returns the result to a file")
    # wildCard(db)
    print("10.  Write a Java Program that run the same SQL and returns the result  with each word reversed.")
    wildCard(db, reverse=True)

    db.close()


if __name__ == '__main__':
    main()

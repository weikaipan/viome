"""A script for migrating data from mysql to mongo."""
#!/usr/bin/python
# -*-coding:utf-8 -*-

from connect import connectMysql, connectMongo


def addContent(mongo, mysql, query=1000):
    """Fetch content from mysql, save into mongo."""
    cursor = mysql.cursor()
    sql = "SELECT Body FROM pages LIMIT " + str(query)
    cursor.execute(sql)
    rows = cursor.fetchall()

    print(len(rows))

    idx = 0
    content = mongo.content

    for row in rows:
        print(row[0].encode('utf-8'))
        cid = content.insert_one({str(idx): row[0].encode('utf-8')})
        idx += 1
    return


def main():
    """"""
    mongoclient = connectMongo()
    collection = mongoclient.Wiki
    mysql = connectMysql()

    addContent(collection, mysql, query=1000)

    mysql.close()
    mongoclient.close()

if __name__ == '__main__':
    main()

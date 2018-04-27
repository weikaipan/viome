from pymongo import MongoClient
import pymysql

def addContent(mongo, mysql, query=1000):
    cursor = mysql.cursor()
    sql = "SELECT Body FROM articles LIMIT " + str(query)
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(len(rows))
    idx = 0
    content = mongo.content
    for row in rows:
        cid = content.insert_one({str(idx): rows[0]}).inserted_id
        print(cid)
        idx += 1
    return
def main():
    client = MongoClient('localhost', 27017)
    mongo = client.Wiki
    mysql = pymysql.connect(host="localhost", user="wkp",
                            password="", db="wiki", charset='utf8mb4')
    addContent(mongo, mysql, query=1000)
    mysql.close()
    client.close()
if __name__ == '__main__':
    main()

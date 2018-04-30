#!/usr/bin/python
# -*-coding:utf-8 -*-
import wikipedia

from connect import connectMysql

newstitles = [u'日本', u'奈良']# 'apples', 'china', 'usa', 'New Zealand',
              # 'norway', 'France', 'Peru', 'Brazil',
              # 'korea', 'Greece', 'Turkey', 'Italy', 'Ireland',
              # 'japan', 'china', 'england', 'canada', 'Jamaica',
              # 'Jordan', 'apples', 'china', 'usa', 'New Zealand']


def get_wiki(db, lang='jp', query='city', pages=10000):
    """Prepare a cursor object using cursor() method."""
    cursor = db.cursor()
    cursor.execute("SET NAMES 'utf8';")
    wikipedia.set_lang(lang)
    titles = wikipedia.search(query, results=pages)
    print("Language: {}".format(lang))

    counter = 0
    for t in titles:
        print("Total Articles: ", len(titles))
        if counter == 10000:
            print("Done")
            return
        if counter == 5000:
            wikipedia.set_lang('jp')
            query = 'tokyo'
        try:
            print("Number {} Articles".format(counter))
            ny = wikipedia.page(t)
            try:
                url = ny.url
            except:
                url = 'NULL'

            try:
                body = ny.content.encode('utf-8')
                print(body)
            except:
                body = 'NULL'

            try:
                ref = ny.references
                ref = ' '.join(ref)
            except:
                ref = 'NULL'

            try:
                head = ny.title.encode('utf-8')
            except:
                head = 'NULL'

            sql = "INSERT INTO `pages` (`Title`, `Body`, `Ref`, `URL`) \
                   VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (head, body, ref, url))
            print("Saved")
            counter += 1
            db.commit()
        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiuation")
            titles.append(e.options)
        except:
            print("No id matches")
            return
        print(counter)
    return


def main():
    """Main function connecting the database."""
    db = connectMysql()
    for t in newstitles:
        get_wiki(db, lang='jp', query=t, pages=10000)
    db.close()


if __name__ == '__main__':
    main()

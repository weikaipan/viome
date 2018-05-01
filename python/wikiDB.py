#!/usr/bin/python
# -*-coding:utf-8 -*-
import wikipedia

from connect import connectMysql

queries = ['usa']


def get_wiki(db, lang='jp', query='city', pages=10000):
    """Get wiki pages using wikipedia library."""
    # Connect with database.
    cursor = db.cursor()
    cursor.execute("SET NAMES 'utf8';")
    wikipedia.set_lang(lang)

    # For each query, insert into database.
    for q in queries:
        titles = wikipedia.search(q, results=pages)
        print("Language: {}".format(lang))
        counter = 0
        for t in titles:
            print("Total Articles: ", len(titles))
            if counter == 10000:
                print("Done")
                return
            # Prevent unexcpeted error for each item.
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
                # Catch special exception for wikipedia lib.
                print("Disambiuation")
                titles.append(e.options)
            except:
                print("No id matches")
                break
            print(counter)
    return


def main():
    """Main function connecting the database."""
    db = connectMysql()
    get_wiki(db, lang='en', pages=10000)
    db.close()


if __name__ == '__main__':
    main()

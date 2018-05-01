# Folder Description

This repo includes: java, python and mysql.

The mysql database has 10619 wikipedia pages, ~4800 pages in japanese.

## ./java

execute ```sh runjava.sh [lines for displaying]```, will output below queries to ```./output/``` directory.

1. "SELECT * FROM pages LIMIT [lines for displaying]"

2. "SELECT Title FROM pages WHERE Title LIKE % + Washington"

3. Reversed outpu for **2**

## ./python

execute ```python sqlquery.py```, will generate txt files into ```./output```

execute ```python wikiDB.py``` will search wikipedia's pages and insert them into the mysql database using [wikipedia library](https://pypi.org/project/wikipedia/) 

## ./mysql

execute ```sh seeMysql.sh```, will output current all titles of wikipedia pages in the database.

execute ```mysql -u [username] < wildCard.sql```, will get the result of wild card title containing "Washington" by default
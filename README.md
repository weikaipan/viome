# viome

## Folder Description

### ./java
The ```./java``` folder contains a maven project ```./java/maven``` folder that I created using Intellij IDEA.

There is also a folder ```./java/source``` which has 3 source code:

1. ```QueryDB.java```
Takes a parameter using command line ```argv[0]```, and return the SQL SELECT query with ```argv[0]``` rows.

2. ```WildCard.java```
Output a wildcard query ```SELECT Title FROM articles " + WHERE Title LIKE %Washington;```, and save the result to ```./wildcard.txt```


3. ```ReverseQuery.java```
Output a wildcard query ```SELECT Title FROM articles " + WHERE Title LIKE %Washington;```, then reverse each words in the query, and save the result to ```./wildcard_re.txt```



### ./mysql
This folder has mysql scripts. 

1. ```wildCard.sql``` This can be executed on the mysql db to select wildcard titles

### ./python

There are 3 scripts in ```./python``` folders:

1. ```addMongo.py```
This script transfers 1000 records in mysql db to the mongodb in the ```content``` collections.

2. ```sqlquery.py```
This script wrap all source codes in ```viome/java/source/*.java```.


3. ```wikiDB.py```
This is the script I used to download 10, 000 wikipedia pages. I applied python's wikipedia library.
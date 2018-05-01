javac QueryDB.java
javac ReverseQuery.java
javac WildCard.java
echo "Query database"
java -cp :./mysql-connector-java-8.0.11.jar QueryDB 10 > query.txt
echo "Show wild Card"
java -cp :./mysql-connector-java-8.0.11.jar WildCard > wildcardsearch.txt
echo "Show reversed content"
java -cp :./mysql-connector-java-8.0.11.jar ReverseQuery > reversewildcardquery.txt

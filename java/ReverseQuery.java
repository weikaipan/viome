import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.PreparedStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.lang.*;


public class ReverseQuery {

    public static void main(String[] args) {
        try {
            // connection settings
            Class.forName("com.mysql.jdbc.Driver");
            String dbName = "wiki";
            String user = "wkp";
            String password = "";
            String hostname = "localhost";
            String port = "";
            String jdbcUrl = "jdbc:mysql://" + hostname + ":" + port + "/" + dbName + "?user=" + user + "&password=" + password;
            // connect
            Connection con = DriverManager.getConnection(jdbcUrl, user, password);
            // queries
            String query = "SELECT Body FROM pages " + "WHERE Title LIKE ?";
            String wild = "%" + "Washington";
            PreparedStatement pst = con.prepareStatement(query);
            pst.setString(1, wild);
            ResultSet rs = pst.executeQuery();
            try {
                BufferedWriter fout = new BufferedWriter(new FileWriter("wildcard_re.txt"));
                while (rs.next()) {
                    String[] ss = rs.getString(1).split(" ");
                    for(String s: ss){
                        StringBuilder input1 = new StringBuilder();
                        input1.append(s);
                        input1 = input1.reverse();
                        System.out.print(input1 + " ");
                    }
                    System.out.println();

                }
            } catch (IOException ioe){
                ioe.printStackTrace();
            }

        } catch (SQLException ex) {
            
            Logger lgr = Logger.getLogger(ReverseQuery.class.getName());
            lgr.log(Level.SEVERE, ex.getMessage(), ex);

        } catch (ClassNotFoundException e) { 

            Logger lgr = Logger.getLogger(ReverseQuery.class.getName());
            lgr.log(Level.SEVERE, e.getMessage(), e);

        }
    }

}

import java.sql.PreparedStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.*;

public class WildCard {

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
            String query = "SELECT Body FROM pages " + "WHERE Title LIKE ?";
            String wild = "%" + "Washington";
            PreparedStatement pst = con.prepareStatement(query);
            pst.setString(1, wild);
            ResultSet rs = pst.executeQuery();

            try {
                
                BufferedWriter fout = new BufferedWriter(new FileWriter("wildcard.txt"));
                while (rs.next()) {
                    System.out.println(rs.getString(1));
                    fout.write(rs.getString(1) + '\n');
                }

            } catch (IOException ioe){

                ioe.printStackTrace();

            }

        } catch (SQLException ex) {

            Logger lgr = Logger.getLogger(WildCard.class.getName());
            lgr.log(Level.SEVERE, ex.getMessage(), ex);

        } catch (ClassNotFoundException e) { 

            Logger lgr = Logger.getLogger(WildCard.class.getName());
            lgr.log(Level.SEVERE, e.getMessage(), e);

        }
        
    }
}

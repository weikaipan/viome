import java.sql.PreparedStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class QueryDB {

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
            Connection con = DriverManager.getConnection(jdbcUrl, user, password);

        	// queries
            String query = "SELECT * FROM pages";
            PreparedStatement pst = con.prepareStatement(query);
            ResultSet rs = pst.executeQuery();
            
            // diplay option
            int rows = Integer.parseInt(args[0]);
            int counter = 1;

            // display qeury
            while (rs.next() && counter <= rows) {
                System.out.println("Query " + counter);
                System.out.println(rs.getString(1));
                System.out.println(rs.getString(3));
                System.out.println(rs.getString(4));
                counter ++;
            }


        } catch (SQLException ex) {
            
            Logger lgr = Logger.getLogger(QueryDB.class.getName());
            lgr.log(Level.SEVERE, ex.getMessage(), ex);

        } catch (ClassNotFoundException e) { 

            Logger lgr = Logger.getLogger(QueryDB.class.getName());
            lgr.log(Level.SEVERE, e.getMessage(), e);

        }
    }
}
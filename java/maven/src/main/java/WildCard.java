package com.zetcode;

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

        String url = "jdbc:mysql://localhost:3306/wiki?useSSL=false";
        String user = "wkp";
        String password = "";

        String query = "SELECT Title FROM articles " + "WHERE Title LIKE ?";
        String wild = "%" + "Washington";
        try (Connection con = DriverManager.getConnection(url, user, password);
             PreparedStatement pst = con.prepareStatement(query);) {
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
        }
    }
}
package com.zetcode;

import java.sql.PreparedStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class queryDB {

    public static void main(String[] args) {

        String url = "jdbc:mysql://localhost:3306/wiki?useSSL=false";
        String user = "wkp";
        String password = "";

        String query = "SELECT * FROM articles";

        try (Connection con = DriverManager.getConnection(url, user, password);
             PreparedStatement pst = con.prepareStatement(query);
             ResultSet rs = pst.executeQuery()) {

            while (rs.next()) {
                System.out.println(rs.getString(1));
                System.out.println(rs.getString(3));
            }

        } catch (SQLException ex) {

            Logger lgr = Logger.getLogger(queryDB.class.getName());
            lgr.log(Level.SEVERE, ex.getMessage(), ex);
        }
    }
}
package com.zetcode;

import java.sql.PreparedStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.lang.*;


public class reverseQuery {

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
        } catch (SQLException ex) {

            Logger lgr = Logger.getLogger(reverseQuery.class.getName());
            lgr.log(Level.SEVERE, ex.getMessage(), ex);
        }
    }
}
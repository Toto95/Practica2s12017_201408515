/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package clienteconecta;

import static clienteconecta.ventanaPrincipal.getString;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.RequestBody;
import java.awt.Desktop;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Ottoniel
 */
public class matriz extends javax.swing.JFrame {

    /**
     * Creates new form matriz
     */
    public matriz() {
        initComponents();
        this.setDefaultCloseOperation(HIDE_ON_CLOSE);
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jTextField1 = new javax.swing.JTextField();
        jButton1 = new javax.swing.JButton();
        jTextField2 = new javax.swing.JTextField();
        jButton2 = new javax.swing.JButton();
        jTextField3 = new javax.swing.JTextField();
        jButton3 = new javax.swing.JButton();
        jTextField4 = new javax.swing.JTextField();
        jButton4 = new javax.swing.JButton();
        jButton5 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jButton1.setText("AGREGAR");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        jButton2.setText("ELIMINAR");
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });

        jButton3.setText("BUSCAR LETRA");
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });

        jButton4.setText("BUSCAR DOMINIO");
        jButton4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton4ActionPerformed(evt);
            }
        });

        jButton5.setText("REPORTE");
        jButton5.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton5ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(113, 113, 113)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(jTextField1)
                    .addComponent(jButton1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jTextField2)
                    .addComponent(jButton2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jTextField3)
                    .addComponent(jButton3, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jTextField4)
                    .addComponent(jButton4, javax.swing.GroupLayout.DEFAULT_SIZE, 152, Short.MAX_VALUE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 56, Short.MAX_VALUE)
                .addComponent(jButton5))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addComponent(jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jButton1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jTextField2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jButton2)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jTextField3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jButton3)
                .addGap(18, 18, 18)
                .addComponent(jTextField4, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(jButton4)
                .addContainerGap(17, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(jButton5))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        if(!this.jTextField2.getText().equals("")){
        String parametro = this.jTextField2.getText();
        RequestBody formBody = new FormEncodingBuilder()
                .add("parametro", parametro)
                .build();
        String salida = getString("eliminarMatriz", formBody); 
        String cmd = "cmd /c dot -Tpng C:\\Users\\Ottoniel\\Desktop\\ytemporal\\matriz.dot > C:\\Users\\Ottoniel\\Desktop\\ytemporal\\matriz.png";
           try {
               Process child = Runtime.getRuntime().exec(cmd);
           } catch (IOException ex) {
               Logger.getLogger(lista.class.getName()).log(Level.SEVERE, null, ex);
           }
         
        this.jTextField2.setText("");
       }// TODO add your handling code here:
    }//GEN-LAST:event_jButton2ActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        if(!this.jTextField1.getText().equals("")){
        String parametro = this.jTextField1.getText();
        RequestBody formBody = new FormEncodingBuilder()
                .add("parametro", parametro)
                .build();
        String salida = getString("insertarMatriz", formBody); 
        String cmd = "cmd /c dot -Tpng C:\\Users\\Ottoniel\\Desktop\\ytemporal\\matriz.dot > C:\\Users\\Ottoniel\\Desktop\\ytemporal\\matriz.png";
           try {
               Process child = Runtime.getRuntime().exec(cmd);
           } catch (IOException ex) {
               Logger.getLogger(lista.class.getName()).log(Level.SEVERE, null, ex);
           }
         
        this.jTextField1.setText("");
       }
    }//GEN-LAST:event_jButton1ActionPerformed
    private boolean esChar(String c){
        try{
            char cc = c.charAt(0);
            return true;
        }catch(Exception e){
            return false;
        }
    }
    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
        if(!this.jTextField3.getText().equals("") && esChar(this.jTextField3.getText())){
        String parametro = this.jTextField3.getText();
        RequestBody formBody = new FormEncodingBuilder()
                .add("parametro", parametro)
                .build();
        String salida = getString("buscarPorLetra", formBody); 
        System.out.println(salida);
        String cmd = "cmd /c dot -Tpng C:\\Users\\Ottoniel\\Desktop\\ytemporal\\matriz.dot > C:\\Users\\Ottoniel\\Desktop\\ytemporal\\matriz.png";
           try {
               Process child = Runtime.getRuntime().exec(cmd);
           } catch (IOException ex) {
               Logger.getLogger(lista.class.getName()).log(Level.SEVERE, null, ex);
           }
         
        this.jTextField3.setText("");
       }
    }//GEN-LAST:event_jButton3ActionPerformed

    private void jButton4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton4ActionPerformed
        if(!this.jTextField4.getText().equals("")){
        String parametro = this.jTextField4.getText();
        RequestBody formBody = new FormEncodingBuilder()
                .add("parametro", parametro)
                .build();
        String salida = getString("buscarPorDominio", formBody); 
        System.out.println(salida);
        String cmd = "cmd /c dot -Tpng C:\\Users\\Ottoniel\\Desktop\\ytemporal\\matriz.dot > C:\\Users\\Ottoniel\\Desktop\\ytemporal\\matriz.png";
           try {
               Process child = Runtime.getRuntime().exec(cmd);
           } catch (IOException ex) {
               Logger.getLogger(lista.class.getName()).log(Level.SEVERE, null, ex);
           }
         
        this.jTextField4.setText("");
       }
    }//GEN-LAST:event_jButton4ActionPerformed

    private void jButton5ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton5ActionPerformed
            File f = new File("C:\\Users\\Ottoniel\\Desktop\\ytemporal\\matriz.png");
    try {
        Desktop.getDesktop().open(f);
    } catch (IOException ex) {
        Logger.getLogger(lista.class.getName()).log(Level.SEVERE, null, ex);
    }                // TODO add your handling code here:
    }//GEN-LAST:event_jButton5ActionPerformed

    

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JButton jButton5;
    private javax.swing.JTextField jTextField1;
    private javax.swing.JTextField jTextField2;
    private javax.swing.JTextField jTextField3;
    private javax.swing.JTextField jTextField4;
    // End of variables declaration//GEN-END:variables
}

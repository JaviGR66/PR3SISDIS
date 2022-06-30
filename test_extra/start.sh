#!/bin/bash
mysql_install_db --user=root
mysqld --user=root &
sleep 5
mariadb -e " CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';"
mariadb -e "CREATE USER 'admin'@'%' IDENTIFIED BY 'password';"
mariadb -e "GRANT ALL ON *.* TO 'admin'@'localhost';"
mariadb -e "GRANT ALL ON *.* TO 'admin'@'%';"
mariadb -e "flush privileges;"
mariadb -e "CREATE DATABASE phpmyadmin;"
mariadb -D phpmyadmin -e "create table Usuarios(Usuario varchar(30), Contrasenia varchar(25), Nombre varchar(25), Apellido1 varchar(25), Apellido2 varchar(25), Correo varchar(40),FraseRecuperacion varchar(50), >mariadb -D phpmyadmin -e "create table Videos(Usuario varchar(30), Tag varchar(25), Vidname varchar(35), Size float,Ruta varchar(50),FechaSubido date, Extension varchar(10));"
mariadb -D phpmyadmin -e "commit;"
apachectl -DFOREGROUND



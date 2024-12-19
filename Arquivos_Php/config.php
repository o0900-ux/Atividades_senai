<?php 

    $hostname = 'localhost';
    $bancodedados = 'users';
    $usuario = 'root';
    $senha = '';

    $mysqli = new mysqli ($hostname, $usuario, $senha, $bancodedados);
    //if ($mysqli->connect_errno) {
       //echo 'falha ao conectar (' . $mysqli->connect_errno . ')' . $mysqli->connect_error;
    //} else {
        //echo 'conectado ao banco de dados';
    //}

?>

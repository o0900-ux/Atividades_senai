<?php 

include_once('config.php');

if (isset($_POST['nome'], $_POST['email'], $_POST['telefone'])) {
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $telefone = $_POST['telefone'];

    $result = mysqli_query($mysqli, "INSERT INTO usuarios (nome, email, telefone) VALUES ('$nome', '$email', '$telefone')");
}

?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Formulário de Cadastro de Usuário</title>
</head>

<style>
body, html {
    height: 100%;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(200, 200, 200);
}

.container {
    text-align: center;
}

.box {
    background: orange;
    padding: 40px;
    border-radius: 30px;
}

</style>

<body>
<div class="container">
    <div class="box">

<h2 style="color: white;" >Cadastro de Usuário</h2>

<form action="index.php" method="POST">
    <label for="nome">Nome:</label><br>
    <input type="text" id="nome" name="nome" required><br><br>

    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required><br><br>

    <label for="telefone">Telefone:</label><br>
    <input type="text" id="telefone" name="telefone"><br><br>

    <input type="submit" value="Cadastrar" id="submit">
</form>
</div>
</div>
</body>
</html>

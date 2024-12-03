<?php
include('conexao.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'];
    $email = $_POST['email'];

    $sqlCheckEmail = "SELECT COUNT(*) FROM usuarios WHERE `e-mail` = :email";
    $stmtCheckEmail = $pdo->prepare($sqlCheckEmail);
    $stmtCheckEmail->bindParam(':email', $email);
    $stmtCheckEmail->execute();
    $emailExists = $stmtCheckEmail->fetchColumn();

    if ($emailExists) {
        echo "<p>E-mail já cadastrado. Tente um e-mail diferente.</p>";
    } else {
        if (!empty($nome) && !empty($email)) {
            $sql = "INSERT INTO usuarios (nome, `e-mail`) VALUES (:nome, :email)";
            
            $stmt = $pdo->prepare($sql);
            $stmt->bindParam(':nome', $nome);
            $stmt->bindParam(':email', $email);

            if ($stmt->execute()) {
                header("Location: cadastro.php");
                exit;
            } else {
                echo "<p>Erro ao cadastrar o usuário. Tente novamente.</p>";
            }
        } else {
            echo "<p>Por favor, preencha todos os campos.</p>";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Usuário</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: rgb(255, 255, 255);
            color: rgb(0, 0, 0);
            margin: 0;
        }

        .navbar {
            background-color: rgb(0, 86, 179);
            overflow: hidden;
            display: flex;
            justify-content: center;
            padding: 10px 0;
        }

        .navbar a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            text-align: center;
            font-size: 16px;
        }

        .navbar a:hover, .navbar a.active {
            background-color: rgb(0, 70, 140);
        }

        .form-container {
            background-color: rgb(255, 255, 255);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            margin: 40px auto 0; 
            border: 2px solid rgb(0, 86, 179);
        }

        h1 {
            color: rgb(0, 0, 0);
            text-align: center;
            margin-bottom: 20px;
        }

        input[type="text"], input[type="email"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid rgb(0, 86, 179);
            border-radius: 5px;
            background-color: rgb(255, 255, 255);
            color: rgb(0, 0, 0);
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: rgb(0, 86, 179);
            color: rgb(255, 255, 255);
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }

        button:hover {
            background-color: rgb(0, 70, 140);
        }
    </style>
</head>
<body>
<div class="navbar">
        <a href="cadastro.php" class="active">Início</a>
        <a href="tarefas.php">Tarefas</a>
        <a href="gerenciar.php">gerenciar</a>
    </div>
    <div class="form-container">
        <h1>Cadastro de Usuário</h1>
        <form action="cadastro.php" method="POST">
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" required>

            <label for="email">E-mail:</label>
            <input type="email" id="email" name="email" required>

            <button type="submit">Cadastrar</button>
        </form>
    </div>
</body>
</html>

<?php
include('conexao.php');

$notificationMessage = "";

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['descricao'])) {
    $descricao = $_POST['descricao'];
    $nome_setor = $_POST['nome_setor'];
    $prioridade = $_POST['prioridade'];
    $id_usuario = $_POST['id_usuario']; 
    $status = 'a fazer'; 

    $sql = "INSERT INTO tarefas (id_usuario, descricao, nome_setor, prioridade, status) 
            VALUES (:id_usuario, :descricao, :nome_setor, :prioridade, :status)";
    $stmt = $pdo->prepare($sql);

    $stmt->bindParam(':id_usuario', $id_usuario);
    $stmt->bindParam(':descricao', $descricao);
    $stmt->bindParam(':nome_setor', $nome_setor);
    $stmt->bindParam(':prioridade', $prioridade);
    $stmt->bindParam(':status', $status);

    if ($stmt->execute()) {
        $notificationMessage = "Tarefa cadastrada com sucesso!";
    } else {
        $notificationMessage = "Erro ao cadastrar a tarefa. Tente novamente.";
    }
}

$sqlUsuarios = "SELECT id, nome FROM usuarios";
$stmtUsuarios = $pdo->prepare($sqlUsuarios);
$stmtUsuarios->execute();
$usuarios = $stmtUsuarios->fetchAll();
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastrar Tarefa</title>
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
    max-width: 600px;
    margin: 40px auto 0; 
    border: 2px solid rgb(0, 86, 179);
}

h1 {
    color: rgb(0, 0, 0);
    text-align: center;
    margin-bottom: 20px;
}

input[type="text"], input[type="email"], select {
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
        <a href="cadastro.php" >Início</a>
        <a href="tarefas.php" class="active">Tarefas</a>
        <a href="gerenciar.php">gerenciar</a>
    </div>
    <div class="form-container">
        <h1>Cadastrar Nova Tarefa</h1>

        <?php if ($notificationMessage): ?>
            <div class="notification" style="color: green; text-align: center;">
                <?php echo $notificationMessage; ?>
            </div>
        <?php endif; ?>

        <form action="tarefas.php" method="POST">
            <label for="descricao">Descrição da Tarefa:</label>
            <input type="text" id="descricao" name="descricao" required>

            <label for="nome_setor">Nome do Setor:</label>
            <input type="text" id="nome_setor" name="nome_setor" required>

            <label for="prioridade">Prioridade:</label>
            <select id="prioridade" name="prioridade" required>
                <option value="alta">Alta</option>
                <option value="media">Média</option>
                <option value="baixa">Baixa</option>
            </select>

            <label for="id_usuario">Selecione o Usuário:</label>
            <select id="id_usuario" name="id_usuario" required>
                <?php foreach ($usuarios as $usuario): ?>
                    <option value="<?php echo $usuario['id']; ?>"><?php echo $usuario['nome']; ?></option>
                <?php endforeach; ?>
            </select>

            <button type="submit">Cadastrar Tarefa</button>
        </form>
    </div>

</body>
</html>

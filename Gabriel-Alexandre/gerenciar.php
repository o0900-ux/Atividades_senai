<?php
include('conexao.php');

if (isset($_GET['delete'])) {
    $id_tarefa = $_GET['delete'];
    $sqlDelete = "DELETE FROM tarefas WHERE id = :id_tarefa";
    $stmtDelete = $pdo->prepare($sqlDelete);
    $stmtDelete->bindParam(':id_tarefa', $id_tarefa);
    $stmtDelete->execute();
}

if (isset($_GET['change_priority'])) {
    $id_tarefa = $_GET['change_priority'];
    $new_priority = $_GET['new_priority'];
    $sqlUpdate = "UPDATE tarefas SET prioridade = :new_priority WHERE id = :id_tarefa";
    $stmtUpdate = $pdo->prepare($sqlUpdate);
    $stmtUpdate->bindParam(':new_priority', $new_priority);
    $stmtUpdate->bindParam(':id_tarefa', $id_tarefa);
    $stmtUpdate->execute();
}

if (isset($_POST['change_status'])) {
    $id_tarefa = $_POST['id_tarefa'];
    $new_status = $_POST['new_status'];
    $sqlUpdate = "UPDATE tarefas SET status = :new_status WHERE id = :id_tarefa";
    $stmtUpdate = $pdo->prepare($sqlUpdate);
    $stmtUpdate->bindParam(':new_status', $new_status);
    $stmtUpdate->bindParam(':id_tarefa', $id_tarefa);
    $stmtUpdate->execute();

    echo "<script>
            window.location.href = window.location.pathname;
          </script>";
}

if (isset($_GET['edit'])) {
    $id_tarefa = $_GET['edit'];
    $sqlEdit = "SELECT * FROM tarefas WHERE id = :id_tarefa";
    $stmtEdit = $pdo->prepare($sqlEdit);
    $stmtEdit->bindParam(':id_tarefa', $id_tarefa);
    $stmtEdit->execute();
    $tarefaEdit = $stmtEdit->fetch();
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['update'])) {
    $id_tarefa = $_POST['id_tarefa'];
    $descricao = $_POST['descricao'];
    $nome_setor = $_POST['nome_setor'];
    $prioridade = $_POST['prioridade'];
    $usuario = $_POST['usuario']; 

    $sqlUpdate = "UPDATE tarefas SET descricao = :descricao, nome_setor = :nome_setor, prioridade = :prioridade, id_usuario = :usuario WHERE id = :id_tarefa";
    $stmtUpdate = $pdo->prepare($sqlUpdate);
    $stmtUpdate->bindParam(':descricao', $descricao);
    $stmtUpdate->bindParam(':nome_setor', $nome_setor);
    $stmtUpdate->bindParam(':prioridade', $prioridade);
    $stmtUpdate->bindParam(':usuario', $usuario);
    $stmtUpdate->bindParam(':id_tarefa', $id_tarefa);
    $stmtUpdate->execute();

    echo "<script>
            window.location.href = window.location.pathname;
          </script>";
}

$sqlTarefas = "SELECT tarefas.id, tarefas.descricao, tarefas.nome_setor, tarefas.prioridade, usuarios.nome AS usuario_nome, tarefas.status 
               FROM tarefas
               JOIN usuarios ON tarefas.id_usuario = usuarios.id";
$stmtTarefas = $pdo->prepare($sqlTarefas);
$stmtTarefas->execute();
$tarefas = $stmtTarefas->fetchAll();
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualizar Tarefas</title>
    <style>
body {
    font-family: Arial, sans-serif;
    background-color: rgb(245, 245, 245);
    color: rgb(0, 0, 0);
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0;
    padding: 0;
}

.navbar {
    background-color: rgb(0, 86, 179);
    overflow: hidden;
    display: flex;
    justify-content: center;
    padding: 10px 0;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000; 
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

.main-content {
    margin-top: 60px; 
    width: 100%;
    max-width: 1200px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.status-container {
    width: 100%;
    max-width: 1200px;
    display: flex;
    justify-content: space-between;
    margin-bottom: 40px;
}

.status-section {
    width: 30%;
    background-color: rgb(255, 255, 255);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.status-section h2 {
    text-align: center;
    color: rgb(0, 0, 0);
    margin-bottom: 20px;
}

.task-card {
    background-color: rgb(255, 255, 255);
    padding: 15px;
    margin-bottom: 15px;
    border-radius: 10px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}

.task-card h3 {
    margin-top: 0;
    color: rgb(0, 86, 179);
}

.task-card p {
    margin: 5px 0;
}

.task-card button {
    margin-top: 10px;
    padding: 5px 10px;
    background-color: rgb(0, 86, 179);
    color: rgb(255, 255, 255);
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.task-card button:hover {
    background-color: rgb(0, 70, 140);
}

.priority-select, .status-select {
    margin-top: 10px;
}

.edit-form {
    margin-top: 20px;
    width: 100%;
    max-width: 600px;
    padding: 20px;
    background-color: rgb(255, 255, 255);
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.edit-form label {
    display: block;
    margin-bottom: 5px;
}

.edit-form input, .edit-form select, .edit-form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    border: 1px solid rgb(0, 86, 179);
}

.edit-form button {
    width: 100%;
    padding: 10px;
    background-color: rgb(0, 86, 179);
    color: rgb(255, 255, 255);
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
    </style>
</head>
<body>
<div class="navbar">
        <a href="cadastro.php" >Início</a>
        <a href="tarefas.php">Tarefas</a>
        <a href="gerenciar.php" class="active">gerenciar</a>
    </div>
    <br>
    <br>
    <br>
    <br>
    <div>
        <h1>Tarefas</h1>
    </div>
    <div class="status-container">
        <?php foreach (['a fazer', 'fazendo', 'pronto'] as $status): ?>
            <div class="status-section">
                <h2><?php echo ucfirst($status); ?></h2>
                <?php foreach ($tarefas as $tarefa): ?>
                    <?php if ($tarefa['status'] == $status): ?>
                        <div class="task-card">
                            <p><strong>descricao:</strong> <?php echo $tarefa['descricao']; ?></p>
                            <p><strong>Setor:</strong> <?php echo $tarefa['nome_setor']; ?></p>
                            <p><strong>Prioridade:</strong> <?php echo ucfirst($tarefa['prioridade']); ?></p>
                            <p><strong>Vinculado a:</strong> <?php echo $tarefa['usuario_nome']; ?></p>
                            <button onclick="window.location.href='?edit=<?php echo $tarefa['id']; ?>'">Editar</button>
                            <button onclick="window.location.href='?delete=<?php echo $tarefa['id']; ?>'">Excluir</button>

                            <form action="" method="POST" class="status-select">
                                <input type="hidden" name="id_tarefa" value="<?php echo $tarefa['id']; ?>" />
                                <select name="new_status">
                                    <option value="a fazer" <?php echo $tarefa['status'] == 'a fazer' ? 'selected' : ''; ?>>A Fazer</option>
                                    <option value="fazendo" <?php echo $tarefa['status'] == 'fazendo' ? 'selected' : ''; ?>>Fazendo</option>
                                    <option value="pronto" <?php echo $tarefa['status'] == 'pronto' ? 'selected' : ''; ?>>Pronto</option>
                                </select>
                                <button type="submit" name="change_status">Alterar Status</button>
                            </form>
                        </div>
                    <?php endif; ?>
                <?php endforeach; ?>
            </div>
        <?php endforeach; ?>
    </div>

    <?php if (isset($tarefaEdit)): ?>
        <div class="edit-form" id="edit-form">
            <h2>Editar Tarefa</h2>
            <form action="" method="POST">
                <input type="hidden" name="id_tarefa" value="<?php echo $tarefaEdit['id']; ?>" />
           
                <label for="descricao">Descrição:</label>
                <textarea name="descricao" required><?php echo $tarefaEdit['descricao']; ?></textarea>

                <label for="nome_setor">Setor:</label>
                <textarea name="nome_setor" required><?php echo $tarefaEdit['nome_setor']; ?></textarea>

                <label for="prioridade">Prioridade:</label>
                <select name="prioridade" required>
                    <option value="alta" <?php echo $tarefaEdit['prioridade'] == 'alta' ? 'selected' : ''; ?>>Alta</option>
                    <option value="media" <?php echo $tarefaEdit['prioridade'] == 'media' ? 'selected' : ''; ?>>Média</option>
                    <option value="baixa" <?php echo $tarefaEdit['prioridade'] == 'baixa' ? 'selected' : ''; ?>>Baixa</option>
                </select>

                <label for="usuario">Vinculado a:</label>
                <select name="usuario" required>
                    <?php
                        $sqlUsuarios = "SELECT id, nome FROM usuarios";
                        $stmtUsuarios = $pdo->prepare($sqlUsuarios);
                        $stmtUsuarios->execute();
                        $usuarios = $stmtUsuarios->fetchAll();
                        foreach ($usuarios as $usuario):
                    ?>
                        <option value="<?php echo $usuario['id']; ?>" <?php echo $tarefaEdit['id_usuario'] == $usuario['id'] ? 'selected' : ''; ?>>
                            <?php echo $usuario['nome']; ?>
                        </option>
                    <?php endforeach; ?>
                </select>

                <button type="submit" name="update">Atualizar Tarefa</button>
            </form>
        </div>
    <?php endif; ?>

</body>
</html>

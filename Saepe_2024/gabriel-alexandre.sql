-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 03-Dez-2024 às 17:19
-- Versão do servidor: 10.4.25-MariaDB
-- versão do PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `gabriel-alexandre`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `tarefas`
--

CREATE TABLE `tarefas` (
  `id` int(8) NOT NULL,
  `id_usuario` int(8) DEFAULT NULL,
  `descricao` varchar(255) NOT NULL,
  `nome_setor` varchar(50) NOT NULL,
  `prioridade` enum('alta','media','baixa') NOT NULL,
  `data_cadastro` datetime DEFAULT current_timestamp(),
  `status` enum('a fazer','fazendo','pronto') DEFAULT 'a fazer'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tarefas`
--

INSERT INTO `tarefas` (`id`, `id_usuario`, `descricao`, `nome_setor`, `prioridade`, `data_cadastro`, `status`) VALUES
(6, 12345692, 'otima exelente', 'setor qualquer ooo', 'baixa', '2024-12-03 12:30:58', 'pronto'),
(7, 12345688, 'otima', 'um bom setor', 'media', '2024-12-03 13:00:35', 'a fazer'),
(8, 12345688, 'otima', 'setor qualquer', 'baixa', '2024-12-03 13:00:43', 'fazendo'),
(9, 12345693, 'atividade', 'setor qualquer', 'media', '2024-12-03 13:17:35', 'fazendo');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(8) NOT NULL COMMENT 'id do usuario',
  `nome` varchar(15) NOT NULL COMMENT 'nome do usuario',
  `e-mail` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='usuarios';

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `e-mail`) VALUES
(12345678, 'gabriel alexand', 'gabriel@kanban.com'),
(12345688, 'manuela vicente', 'manuela@kanban.com'),
(12345691, 'paulo melo', 'paulo@kanban.com'),
(12345692, 'paulina silva', 'paulina@kanban.com'),
(12345693, 'pessoa', 'pessoa@email.com');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `tarefas`
--
ALTER TABLE `tarefas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Índices para tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `tarefas`
--
ALTER TABLE `tarefas`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT COMMENT 'id do usuario', AUTO_INCREMENT=12345694;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `tarefas`
--
ALTER TABLE `tarefas`
  ADD CONSTRAINT `tarefas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

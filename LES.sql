-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 07, 2021 at 11:11 AM
-- Server version: 10.3.27-MariaDB-0+deb10u1
-- PHP Version: 7.3.27-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `LES`
--

-- --------------------------------------------------------

--
-- Table structure for table `Administrador`
--

CREATE TABLE `Administrador` (
  `UtilizadorID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add certificado de participação', 7, 'add_certificadodeparticipação'),
(26, 'Can change certificado de participação', 7, 'change_certificadodeparticipação'),
(27, 'Can delete certificado de participação', 7, 'delete_certificadodeparticipação'),
(28, 'Can view certificado de participação', 7, 'view_certificadodeparticipação'),
(29, 'Can add evento', 8, 'add_evento'),
(30, 'Can change evento', 8, 'change_evento'),
(31, 'Can delete evento', 8, 'delete_evento'),
(32, 'Can view evento', 8, 'view_evento'),
(33, 'Can add tipo de evento', 9, 'add_tipodeevento'),
(34, 'Can change tipo de evento', 9, 'change_tipodeevento'),
(35, 'Can delete tipo de evento', 9, 'delete_tipodeevento'),
(36, 'Can view tipo de evento', 9, 'view_tipodeevento'),
(37, 'Can add requisição', 10, 'add_requisição'),
(38, 'Can change requisição', 10, 'change_requisição'),
(39, 'Can delete requisição', 10, 'delete_requisição'),
(40, 'Can view requisição', 10, 'view_requisição'),
(41, 'Can add pedido de recurso', 11, 'add_pedidoderecurso'),
(42, 'Can change pedido de recurso', 11, 'change_pedidoderecurso'),
(43, 'Can delete pedido de recurso', 11, 'delete_pedidoderecurso'),
(44, 'Can view pedido de recurso', 11, 'view_pedidoderecurso'),
(45, 'Can add evento servicos', 12, 'add_eventoservicos'),
(46, 'Can change evento servicos', 12, 'change_eventoservicos'),
(47, 'Can delete evento servicos', 12, 'delete_eventoservicos'),
(48, 'Can view evento servicos', 12, 'view_eventoservicos'),
(49, 'Can add evento locais', 13, 'add_eventolocais'),
(50, 'Can change evento locais', 13, 'change_eventolocais'),
(51, 'Can delete evento locais', 13, 'delete_eventolocais'),
(52, 'Can view evento locais', 13, 'view_eventolocais'),
(53, 'Can add evento equipamentos', 14, 'add_eventoequipamentos'),
(54, 'Can change evento equipamentos', 14, 'change_eventoequipamentos'),
(55, 'Can delete evento equipamentos', 14, 'delete_eventoequipamentos'),
(56, 'Can view evento equipamentos', 14, 'view_eventoequipamentos'),
(57, 'Can add formulário', 15, 'add_formulário'),
(58, 'Can change formulário', 15, 'change_formulário'),
(59, 'Can delete formulário', 15, 'delete_formulário'),
(60, 'Can view formulário', 15, 'view_formulário'),
(61, 'Can add pergunta', 16, 'add_pergunta'),
(62, 'Can change pergunta', 16, 'change_pergunta'),
(63, 'Can delete pergunta', 16, 'delete_pergunta'),
(64, 'Can view pergunta', 16, 'view_pergunta'),
(65, 'Can add tipo de formulário', 17, 'add_tipodeformulário'),
(66, 'Can change tipo de formulário', 17, 'change_tipodeformulário'),
(67, 'Can delete tipo de formulário', 17, 'delete_tipodeformulário'),
(68, 'Can view tipo de formulário', 17, 'view_tipodeformulário'),
(69, 'Can add tipo de pergunta', 18, 'add_tipodepergunta'),
(70, 'Can change tipo de pergunta', 18, 'change_tipodepergunta'),
(71, 'Can delete tipo de pergunta', 18, 'delete_tipodepergunta'),
(72, 'Can view tipo de pergunta', 18, 'view_tipodepergunta'),
(73, 'Can add resposta', 19, 'add_resposta'),
(74, 'Can change resposta', 19, 'change_resposta'),
(75, 'Can delete resposta', 19, 'delete_resposta'),
(76, 'Can view resposta', 19, 'view_resposta'),
(77, 'Can add opção de resposta', 20, 'add_opçãoderesposta'),
(78, 'Can change opção de resposta', 20, 'change_opçãoderesposta'),
(79, 'Can delete opção de resposta', 20, 'delete_opçãoderesposta'),
(80, 'Can view opção de resposta', 20, 'view_opçãoderesposta'),
(81, 'Can add formulário pergunta', 21, 'add_formuláriopergunta'),
(82, 'Can change formulário pergunta', 21, 'change_formuláriopergunta'),
(83, 'Can delete formulário pergunta', 21, 'delete_formuláriopergunta'),
(84, 'Can view formulário pergunta', 21, 'view_formuláriopergunta'),
(85, 'Can add inscrição', 22, 'add_inscrição'),
(86, 'Can change inscrição', 22, 'change_inscrição'),
(87, 'Can delete inscrição', 22, 'delete_inscrição'),
(88, 'Can view inscrição', 22, 'view_inscrição'),
(89, 'Can add pagamento', 23, 'add_pagamento'),
(90, 'Can change pagamento', 23, 'change_pagamento'),
(91, 'Can delete pagamento', 23, 'delete_pagamento'),
(92, 'Can view pagamento', 23, 'view_pagamento'),
(93, 'Can add feedback', 24, 'add_feedback'),
(94, 'Can change feedback', 24, 'change_feedback'),
(95, 'Can delete feedback', 24, 'delete_feedback'),
(96, 'Can view feedback', 24, 'view_feedback'),
(97, 'Can add campus', 25, 'add_campus'),
(98, 'Can change campus', 25, 'change_campus'),
(99, 'Can delete campus', 25, 'delete_campus'),
(100, 'Can view campus', 25, 'view_campus'),
(101, 'Can add recurso', 26, 'add_recurso'),
(102, 'Can change recurso', 26, 'change_recurso'),
(103, 'Can delete recurso', 26, 'delete_recurso'),
(104, 'Can view recurso', 26, 'view_recurso'),
(105, 'Can add recurso_estado', 27, 'add_recurso_estado'),
(106, 'Can change recurso_estado', 27, 'change_recurso_estado'),
(107, 'Can delete recurso_estado', 27, 'delete_recurso_estado'),
(108, 'Can view recurso_estado', 27, 'view_recurso_estado'),
(109, 'Can add tipo de recurso', 28, 'add_tipoderecurso'),
(110, 'Can change tipo de recurso', 28, 'change_tipoderecurso'),
(111, 'Can delete tipo de recurso', 28, 'delete_tipoderecurso'),
(112, 'Can view tipo de recurso', 28, 'view_tipoderecurso'),
(113, 'Can add equipamento', 29, 'add_equipamento'),
(114, 'Can change equipamento', 29, 'change_equipamento'),
(115, 'Can delete equipamento', 29, 'delete_equipamento'),
(116, 'Can view equipamento', 29, 'view_equipamento'),
(117, 'Can add serviço', 30, 'add_serviço'),
(118, 'Can change serviço', 30, 'change_serviço'),
(119, 'Can delete serviço', 30, 'delete_serviço'),
(120, 'Can view serviço', 30, 'view_serviço'),
(121, 'Can add edificio', 31, 'add_edificio'),
(122, 'Can change edificio', 31, 'change_edificio'),
(123, 'Can delete edificio', 31, 'delete_edificio'),
(124, 'Can view edificio', 31, 'view_edificio'),
(125, 'Can add sala', 32, 'add_sala'),
(126, 'Can change sala', 32, 'change_sala'),
(127, 'Can delete sala', 32, 'delete_sala'),
(128, 'Can view sala', 32, 'view_sala'),
(129, 'Can add mensagem', 33, 'add_mensagem'),
(130, 'Can change mensagem', 33, 'change_mensagem'),
(131, 'Can delete mensagem', 33, 'delete_mensagem'),
(132, 'Can view mensagem', 33, 'view_mensagem'),
(133, 'Can add utilizador mensagem', 34, 'add_utilizadormensagem'),
(134, 'Can change utilizador mensagem', 34, 'change_utilizadormensagem'),
(135, 'Can delete utilizador mensagem', 34, 'delete_utilizadormensagem'),
(136, 'Can view utilizador mensagem', 34, 'view_utilizadormensagem'),
(137, 'Can add utilizador', 35, 'add_utilizador'),
(138, 'Can change utilizador', 35, 'change_utilizador'),
(139, 'Can delete utilizador', 35, 'delete_utilizador'),
(140, 'Can view utilizador', 35, 'view_utilizador'),
(141, 'Can add administrador', 36, 'add_administrador'),
(142, 'Can change administrador', 36, 'change_administrador'),
(143, 'Can delete administrador', 36, 'delete_administrador'),
(144, 'Can view administrador', 36, 'view_administrador'),
(145, 'Can add participante', 37, 'add_participante'),
(146, 'Can change participante', 37, 'change_participante'),
(147, 'Can delete participante', 37, 'delete_participante'),
(148, 'Can view participante', 37, 'view_participante'),
(149, 'Can add proponente', 38, 'add_proponente'),
(150, 'Can change proponente', 38, 'change_proponente'),
(151, 'Can delete proponente', 38, 'delete_proponente'),
(152, 'Can view proponente', 38, 'view_proponente');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Campus`
--

CREATE TABLE `Campus` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `Morada` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Campus`
--

INSERT INTO `Campus` (`ID`, `Nome`, `Morada`) VALUES
(1, 'Gambelas', 'Faro'),
(2, 'Penha', 'Faro');

-- --------------------------------------------------------

--
-- Table structure for table `Certificado de Participação`
--

CREATE TABLE `Certificado de Participação` (
  `ID` int(11) NOT NULL,
  `Nome evento` varchar(255) DEFAULT NULL,
  `Data emissão` date DEFAULT NULL,
  `Nome participante` varchar(255) DEFAULT NULL,
  `Publico` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(7, '2021-07-05 00:45:17.376940', '1', '10', 1, '[{\"added\": {}}]', 30, 10),
(8, '2021-07-05 00:47:37.591617', '1', '12', 2, '[{\"changed\": {\"fields\": [\"Nome\"]}}]', 26, 10),
(9, '2021-07-05 00:48:20.541743', '1', '12', 1, '[{\"added\": {}}]', 29, 10),
(10, '2021-07-05 15:51:12.031725', '13', 'Filipe', 3, '', 38, 10),
(11, '2021-07-06 01:35:22.635432', '46', 'FormulárioPergunta object (46)', 3, '', 21, 10),
(12, '2021-07-06 01:35:26.464155', '45', 'FormulárioPergunta object (45)', 3, '', 21, 10),
(13, '2021-07-06 16:01:49.938812', '1', 'Microfone', 3, '', 32, 10),
(14, '2021-07-06 16:03:57.134903', '7', 'CP - Gambelas', 1, '[{\"added\": {}}]', 31, 10),
(15, '2021-07-07 09:48:42.458216', '1', 'EventoLocais object (1)', 3, '', 13, 10),
(16, '2021-07-07 09:48:59.190074', '13', 'EventoA', 3, '', 8, 10),
(17, '2021-07-07 09:49:00.424644', '12', 'EventoA', 3, '', 8, 10),
(18, '2021-07-07 09:49:07.922090', '11', 'Vida mais facil depois do curso!', 3, '', 8, 10),
(19, '2021-07-07 09:49:08.218706', '13', 'EventoA', 3, '', 8, 10),
(20, '2021-07-07 09:49:15.325441', '12', 'EventoA', 3, '', 8, 10),
(21, '2021-07-07 09:49:15.328431', '8', 'Teste2', 3, '', 8, 10),
(22, '2021-07-07 09:49:19.581992', '11', 'Vida mais facil depois do curso!', 3, '', 8, 10),
(23, '2021-07-07 09:49:22.156808', '5', 'Unity for noobs', 3, '', 8, 10),
(24, '2021-07-07 09:49:28.764413', '8', 'Teste2', 3, '', 8, 10),
(25, '2021-07-07 09:49:33.755785', '3', 'Evento do Proponente', 3, '', 8, 10),
(26, '2021-07-07 09:49:33.756806', '5', 'Unity for noobs', 3, '', 8, 10),
(27, '2021-07-07 09:49:44.265594', '13', 'EventoA', 3, '', 8, 10),
(28, '2021-07-07 09:49:46.750715', '3', 'Evento do Proponente', 3, '', 8, 10),
(29, '2021-07-07 09:51:06.467807', '12', 'EventoA', 3, '', 8, 10),
(30, '2021-07-07 09:51:20.279946', '11', 'Vida mais facil depois do curso!', 3, '', 8, 10),
(31, '2021-07-07 09:51:40.984458', '8', 'Teste2', 3, '', 8, 10),
(32, '2021-07-07 09:51:52.506442', '5', 'Unity for noobs', 3, '', 8, 10),
(33, '2021-07-07 09:52:33.250769', '3', 'Evento do Proponente', 3, '', 8, 10),
(34, '2021-07-07 09:53:42.379715', '11', 'PedidoDeRecurso object (11)', 3, '', 11, 10),
(35, '2021-07-07 09:53:45.573542', '10', 'PedidoDeRecurso object (10)', 3, '', 11, 10),
(36, '2021-07-07 09:53:48.181423', '7', 'PedidoDeRecurso object (7)', 3, '', 11, 10),
(37, '2021-07-07 09:53:54.592450', '6', 'PedidoDeRecurso object (6)', 3, '', 11, 10),
(38, '2021-07-07 09:53:58.404932', '4', 'PedidoDeRecurso object (4)', 3, '', 11, 10),
(39, '2021-07-07 09:54:09.858178', '3', 'PedidoDeRecurso object (3)', 3, '', 11, 10),
(40, '2021-07-07 09:54:14.991284', '2', 'PedidoDeRecurso object (2)', 3, '', 11, 10),
(41, '2021-07-07 09:54:20.026250', '1', 'PedidoDeRecurso object (1)', 3, '', 11, 10),
(42, '2021-07-07 09:55:10.150833', '65', 'FormulárioPergunta object (65)', 3, '', 21, 10),
(43, '2021-07-07 09:55:10.169833', '64', 'FormulárioPergunta object (64)', 3, '', 21, 10),
(44, '2021-07-07 09:55:10.213340', '63', 'FormulárioPergunta object (63)', 3, '', 21, 10),
(45, '2021-07-07 09:55:10.237340', '62', 'FormulárioPergunta object (62)', 3, '', 21, 10),
(46, '2021-07-07 09:55:10.254339', '43', 'FormulárioPergunta object (43)', 3, '', 21, 10),
(47, '2021-07-07 09:55:10.410011', '42', 'FormulárioPergunta object (42)', 3, '', 21, 10),
(48, '2021-07-07 09:55:10.425011', '41', 'FormulárioPergunta object (41)', 3, '', 21, 10),
(49, '2021-07-07 09:55:10.441011', '40', 'FormulárioPergunta object (40)', 3, '', 21, 10),
(50, '2021-07-07 09:55:10.463369', '35', 'FormulárioPergunta object (35)', 3, '', 21, 10),
(51, '2021-07-07 09:55:10.482959', '34', 'FormulárioPergunta object (34)', 3, '', 21, 10),
(52, '2021-07-07 09:55:10.499978', '33', 'FormulárioPergunta object (33)', 3, '', 21, 10),
(53, '2021-07-07 09:55:10.518472', '32', 'FormulárioPergunta object (32)', 3, '', 21, 10),
(54, '2021-07-07 09:55:10.536491', '31', 'FormulárioPergunta object (31)', 3, '', 21, 10),
(55, '2021-07-07 09:55:10.693207', '30', 'FormulárioPergunta object (30)', 3, '', 21, 10),
(56, '2021-07-07 09:55:10.711184', '29', 'FormulárioPergunta object (29)', 3, '', 21, 10),
(57, '2021-07-07 09:55:10.729207', '28', 'FormulárioPergunta object (28)', 3, '', 21, 10),
(58, '2021-07-07 09:55:10.747200', '25', 'FormulárioPergunta object (25)', 3, '', 21, 10),
(59, '2021-07-07 09:55:10.775988', '24', 'FormulárioPergunta object (24)', 3, '', 21, 10),
(60, '2021-07-07 09:55:10.790217', '21', 'FormulárioPergunta object (21)', 3, '', 21, 10),
(61, '2021-07-07 09:55:10.808061', '20', 'FormulárioPergunta object (20)', 3, '', 21, 10),
(62, '2021-07-07 09:55:10.824274', '18', 'FormulárioPergunta object (18)', 3, '', 21, 10),
(63, '2021-07-07 09:55:10.980383', '17', 'FormulárioPergunta object (17)', 3, '', 21, 10),
(64, '2021-07-07 09:55:11.018460', '15', 'FormulárioPergunta object (15)', 3, '', 21, 10),
(65, '2021-07-07 09:55:11.035651', '14', 'FormulárioPergunta object (14)', 3, '', 21, 10),
(66, '2021-07-07 09:55:11.052617', '13', 'FormulárioPergunta object (13)', 3, '', 21, 10),
(67, '2021-07-07 09:55:30.656307', '30', 'Formulário object (30)', 3, '', 15, 10),
(68, '2021-07-07 09:55:31.845058', '29', 'Formulário object (29)', 3, '', 15, 10),
(69, '2021-07-07 09:55:31.861057', '27', 'Formulário object (27)', 3, '', 15, 10),
(70, '2021-07-07 09:55:31.878058', '26', 'Formulário object (26)', 3, '', 15, 10),
(71, '2021-07-07 09:55:31.895073', '10', 'Formulário object (10)', 3, '', 15, 10),
(72, '2021-07-07 09:55:32.052063', '9', 'Formulário object (9)', 3, '', 15, 10),
(73, '2021-07-07 09:55:32.074080', '6', 'Formulário object (6)', 3, '', 15, 10),
(74, '2021-07-07 09:55:32.093061', '4', 'Formulário object (4)', 3, '', 15, 10),
(75, '2021-07-07 09:55:32.109057', '3', 'Formulário object (3)', 3, '', 15, 10),
(76, '2021-07-07 09:55:33.372101', '2', 'Formulário object (2)', 3, '', 15, 10),
(77, '2021-07-07 09:55:37.174427', '1', 'Formulário object (1)', 3, '', 15, 10),
(78, '2021-07-07 09:56:30.713467', '20', 'vila1', 3, '', 20, 10),
(79, '2021-07-07 09:56:30.732115', '19', 'cidade', 3, '', 20, 10),
(80, '2021-07-07 09:56:30.753446', '18', 'Prefiro não dizer', 3, '', 20, 10),
(81, '2021-07-07 09:56:30.782269', '10', 'Mulher', 3, '', 20, 10),
(82, '2021-07-07 09:56:30.800797', '9', 'Homem', 3, '', 20, 10),
(83, '2021-07-07 09:56:30.819799', '8', 'Perfiro não dizer', 3, '', 20, 10),
(84, '2021-07-07 09:56:30.840010', '7', 'Mulher', 3, '', 20, 10),
(85, '2021-07-07 09:56:30.857592', '6', 'Homem', 3, '', 20, 10),
(86, '2021-07-07 09:56:30.877587', '1', 'bla', 3, '', 20, 10),
(87, '2021-07-07 09:56:53.455470', '18', 'Nome', 3, '', 16, 10),
(88, '2021-07-07 09:56:54.515326', '12', 'Genero', 3, '', 16, 10),
(89, '2021-07-07 09:57:03.238115', '11', 'Genero', 3, '', 16, 10),
(90, '2021-07-07 09:57:03.401170', '8', 'Nome', 3, '', 16, 10),
(91, '2021-07-07 09:57:04.762117', '7', 'Telefone', 3, '', 16, 10),
(92, '2021-07-07 09:57:06.332222', '18', 'Nome', 3, '', 16, 10),
(93, '2021-07-07 09:57:12.318289', '12', 'Genero', 3, '', 16, 10),
(94, '2021-07-07 09:57:12.319306', '5', 'Nome', 3, '', 16, 10),
(95, '2021-07-07 09:57:12.341291', '11', 'Genero', 3, '', 16, 10),
(96, '2021-07-07 09:57:12.361883', '4', 'Telefone', 3, '', 16, 10),
(97, '2021-07-07 09:57:12.374273', '8', 'Nome', 3, '', 16, 10),
(98, '2021-07-07 09:57:12.387943', '3', 'Email', 3, '', 16, 10),
(99, '2021-07-07 09:57:12.516264', '7', 'Telefone', 3, '', 16, 10),
(100, '2021-07-07 09:57:12.527271', '2', 'Idade', 3, '', 16, 10),
(101, '2021-07-07 09:57:12.562221', '5', 'Nome', 3, '', 16, 10),
(102, '2021-07-07 09:57:12.568229', '1', 'Nome', 3, '', 16, 10),
(103, '2021-07-07 09:57:12.588220', '4', 'Telefone', 3, '', 16, 10),
(104, '2021-07-07 09:57:12.613231', '3', 'Email', 3, '', 16, 10),
(105, '2021-07-07 09:57:12.633503', '2', 'Idade', 3, '', 16, 10),
(106, '2021-07-07 09:57:12.674246', '1', 'Nome', 3, '', 16, 10),
(107, '2021-07-07 09:57:29.199829', '112', 'Resposta object (112)', 3, '', 19, 10),
(108, '2021-07-07 09:57:33.083955', '111', 'Resposta object (111)', 3, '', 19, 10),
(109, '2021-07-07 09:57:35.977072', '112', 'Resposta object (112)', 3, '', 19, 10),
(110, '2021-07-07 09:57:38.501006', '111', 'Resposta object (111)', 3, '', 19, 10),
(111, '2021-07-07 09:57:38.502018', '110', 'Resposta object (110)', 3, '', 19, 10),
(112, '2021-07-07 09:57:48.554401', '109', 'Resposta object (109)', 3, '', 19, 10),
(113, '2021-07-07 09:57:48.555434', '110', 'Resposta object (110)', 3, '', 19, 10),
(114, '2021-07-07 09:57:49.901958', '108', 'Resposta object (108)', 3, '', 19, 10),
(115, '2021-07-07 09:57:49.905954', '109', 'Resposta object (109)', 3, '', 19, 10),
(116, '2021-07-07 09:57:56.265323', '108', 'Resposta object (108)', 3, '', 19, 10),
(117, '2021-07-07 09:58:42.737184', '23', '23', 3, '', 22, 10),
(118, '2021-07-07 09:58:53.077821', '3', '3', 3, '', 23, 10),
(119, '2021-07-07 09:58:53.097886', '2', '2', 3, '', 23, 10),
(120, '2021-07-07 09:58:53.124172', '1', '1', 3, '', 23, 10),
(121, '2021-07-07 09:59:08.322103', '9', 'Microfone2', 3, '', 29, 10),
(122, '2021-07-07 09:59:08.340771', '7', 'Colunas de som', 3, '', 29, 10),
(123, '2021-07-07 09:59:08.494981', '1', 'Microfone', 3, '', 29, 10),
(124, '2021-07-07 09:59:27.542539', '9', 'Microfone2', 3, '', 26, 10),
(125, '2021-07-07 09:59:28.788841', '8', 'Internet2', 3, '', 26, 10),
(126, '2021-07-07 09:59:37.644976', '7', 'Colunas de som', 3, '', 26, 10),
(127, '2021-07-07 09:59:41.446219', '6', 'Almoço', 3, '', 26, 10),
(128, '2021-07-07 09:59:42.805459', '5', 'CP 2.6', 3, '', 26, 10),
(129, '2021-07-07 09:59:42.960990', '4', 'CP 2.5', 3, '', 26, 10),
(130, '2021-07-07 09:59:42.976002', '3', 'Internet', 3, '', 26, 10),
(131, '2021-07-07 09:59:44.439759', '1', 'Microfone', 3, '', 26, 10),
(132, '2021-07-07 10:05:07.289829', '16', 'Catto', 3, '', 35, 10),
(133, '2021-07-07 10:05:07.307832', '13', 'Filipe', 3, '', 35, 10),
(134, '2021-07-07 10:05:07.327852', '3', 'test3', 3, '', 35, 10),
(135, '2021-07-07 10:05:07.485932', '5', 'test4', 3, '', 35, 10),
(136, '2021-07-07 10:05:07.507045', '6', 'test5', 3, '', 35, 10),
(137, '2021-07-07 10:05:07.526586', '7', 'test6', 3, '', 35, 10),
(138, '2021-07-07 10:05:07.544933', '8', 'test7', 3, '', 35, 10),
(139, '2021-07-07 10:05:07.564486', '9', 'test9', 3, '', 35, 10),
(140, '2021-07-07 10:05:07.585929', '14', 'teste', 3, '', 35, 10),
(141, '2021-07-07 10:05:07.742059', '11', 'XikoCat', 3, '', 35, 10),
(142, '2021-07-07 10:05:07.772653', '15', 'XikoCat2', 3, '', 35, 10);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'Evento', 'certificadodeparticipação'),
(8, 'Evento', 'evento'),
(14, 'Evento', 'eventoequipamentos'),
(13, 'Evento', 'eventolocais'),
(12, 'Evento', 'eventoservicos'),
(11, 'Evento', 'pedidoderecurso'),
(10, 'Evento', 'requisição'),
(9, 'Evento', 'tipodeevento'),
(15, 'Formulario', 'formulário'),
(21, 'Formulario', 'formuláriopergunta'),
(20, 'Formulario', 'opçãoderesposta'),
(16, 'Formulario', 'pergunta'),
(19, 'Formulario', 'resposta'),
(17, 'Formulario', 'tipodeformulário'),
(18, 'Formulario', 'tipodepergunta'),
(24, 'Inscriçao', 'feedback'),
(22, 'Inscriçao', 'inscrição'),
(23, 'Inscriçao', 'pagamento'),
(33, 'main', 'mensagem'),
(34, 'main', 'utilizadormensagem'),
(25, 'Recurso', 'campus'),
(31, 'Recurso', 'edificio'),
(29, 'Recurso', 'equipamento'),
(26, 'Recurso', 'recurso'),
(27, 'Recurso', 'recurso_estado'),
(32, 'Recurso', 'sala'),
(30, 'Recurso', 'serviço'),
(28, 'Recurso', 'tipoderecurso'),
(6, 'sessions', 'session'),
(36, 'Utilizadores', 'administrador'),
(37, 'Utilizadores', 'participante'),
(38, 'Utilizadores', 'proponente'),
(35, 'Utilizadores', 'utilizador');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Utilizadores', '0001_initial', '2021-07-03 22:59:03.864571'),
(2, 'Recurso', '0001_initial', '2021-07-03 23:06:06.430492'),
(3, 'Evento', '0001_initial', '2021-07-03 23:16:54.169120'),
(4, 'Inscriçao', '0001_initial', '2021-07-03 23:21:06.401538'),
(5, 'Formulario', '0001_initial', '2021-07-03 23:32:57.986779'),
(6, 'Evento', '0002_initial', '2021-07-03 23:37:04.801807'),
(7, 'contenttypes', '0001_initial', '2021-07-03 23:37:05.158126'),
(8, 'auth', '0001_initial', '2021-07-03 23:47:17.268026'),
(9, 'admin', '0001_initial', '2021-07-03 23:49:42.315223'),
(10, 'admin', '0002_logentry_remove_auto_add', '2021-07-03 23:49:43.666346'),
(11, 'admin', '0003_logentry_add_action_flag_choices', '2021-07-03 23:49:45.136397'),
(12, 'contenttypes', '0002_remove_content_type_name', '2021-07-03 23:50:50.182166'),
(13, 'auth', '0002_alter_permission_name_max_length', '2021-07-03 23:52:01.295668'),
(14, 'auth', '0003_alter_user_email_max_length', '2021-07-03 23:52:07.904976'),
(15, 'auth', '0004_alter_user_username_opts', '2021-07-03 23:52:10.490441'),
(16, 'auth', '0005_alter_user_last_login_null', '2021-07-03 23:52:52.854024'),
(17, 'auth', '0006_require_contenttypes_0002', '2021-07-03 23:52:59.170597'),
(18, 'auth', '0007_alter_validators_add_error_messages', '2021-07-03 23:53:00.427674'),
(19, 'auth', '0008_alter_user_username_max_length', '2021-07-03 23:53:54.150120'),
(20, 'auth', '0009_alter_user_last_name_max_length', '2021-07-03 23:55:09.357137'),
(21, 'auth', '0010_alter_group_name_max_length', '2021-07-03 23:55:14.322918'),
(22, 'auth', '0011_update_proxy_permissions', '2021-07-03 23:55:20.795134'),
(23, 'auth', '0012_alter_user_first_name_max_length', '2021-07-03 23:56:15.355770'),
(24, 'main', '0001_initial', '2021-07-03 23:59:50.708223'),
(25, 'sessions', '0001_initial', '2021-07-04 00:00:25.639288'),
(26, 'Formulario', '0002_auto_20210704_1312', '2021-07-04 13:15:00.574756'),
(27, 'Evento', '0003_auto_20210704_1514', '2021-07-04 15:15:10.807164'),
(28, 'Formulario', '0003_formulário_evento_id', '2021-07-04 15:16:21.198594'),
(29, 'Evento', '0004_auto_20210704_1700', '2021-07-04 17:02:17.716680'),
(30, 'Evento', '0005_alter_evento_evento_pagoid', '2021-07-04 17:08:27.076968'),
(31, 'Utilizadores', '0002_utilizador_tipoutilizador', '2021-07-04 23:27:12.225276'),
(32, 'Formulario', '0004_alter_formuláriopergunta_pos', '2021-07-05 16:40:48.104397');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('09k9vi77224ku6jors6gsdejadt6r2uq', '.eJxVjMsOwiAQRf-FtSHlMTxcuvcbCAODVA0kpV0Z_12bdKHbe865LxbittawDVrCnNmZCWCn3xFjelDbSb7Hdus89bYuM_Jd4Qcd_NozPS-H-3dQ46jfmgqQEwK089J6lKBwsspJFZHQ60yJkkFw0kphPKCeCIsuhpLLStnI3h_8DjgX:1m0tMd:buGq8WUi4FSFdiCAOK_fv5mp7ADHltWmkKHk_APGGkE', '2021-07-20 22:16:23.983881'),
('2h56vczplyi0aftewy8go1802kbzsaty', '.eJxVjMsOwiAQRf-FtSFAZwBduu83kBlgpGrapI-V8d-1SRe6veec-1KJtrWlbalzGoq6KAvq9Dsy5Ucdd1LuNN4mnadxnQfWu6IPuuh-KvV5Pdy_g0ZL-9YiBS25zGiAjA8sjB04hhCzYOy8eBDMBHg26CwWYRcEJEfoMHqv3h8S6Dfg:1m0sz5:o4Uq_sOYN7jQxKgyQBOuJ8EdpghiUK-KC6sGsHPphAY', '2021-07-20 21:52:03.979797'),
('57pyv6x1inn458znqtjqvqbou3avfmoh', '.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MykYKffMUF-UNsJ3qHdOs-9rcuc-K7wgw5-7UjPy-H-HVQY9VtbL53VOhVtghJmytYZTaTQyiyySo6cJ1TCB2P9BISUCHXxxakUBBB7fwDoDDgb:1m13s6:SdaaBgOfxWY72N75hjuXDfyeCy7ezcuMtojImhPVrTw', '2021-07-21 09:29:34.869093'),
('8tsfse345cmp2she21azvtrfsdke36n5', '.eJxVjMsOwiAQRf-FtSGU4TF16d5vIMAwUjUlKe3K-O_apAvd3nPOfYkQt7WGrZclTCTOYlDi9DummB9l3gnd43xrMrd5XaYkd0UetMtro_K8HO7fQY29fmuTRoMuY9JkM4-KAHyKo7YMyBqLAzAKbVI5WialkaEM3hB7jY4BxPsD_lg3tQ:1m0Ccj:09Mxvh2Ie3t4X6niD0SxwCy4qIBjsB6NKG_bif-VH2s', '2021-07-19 00:38:09.712285'),
('b2lpg1h1mbpnk8zi3veb5exbckng2sff', '.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MykYKffMUF-UNsJ3qHdOs-9rcuc-K7wgw5-7UjPy-H-HVQY9VtbL53VOhVtghJmytYZTaTQyiyySo6cJ1TCB2P9BISUCHXxxakUBBB7fwDoDDgb:1m13de:VNoPBWPVysfqfP02u-IAITegeVGVyA80avxwiB7cpe0', '2021-07-21 09:14:38.856523'),
('evy7ckwvqwmjq3mnw1jfj4zndluok30q', '.eJxVjDsOwjAQRO_iGlnexD8o6TmDtfaucQDZUpxUiLuTSCmgG817M28RcF1KWDvPYSJxEWDE6beMmJ5cd0IPrPcmU6vLPEW5K_KgXd4a8et6uH8HBXvZ1spkGPDsMJFD9pqZnMkYrQKAPPpsUA0jKbtlQqWJdcbRuagJiK0Xny8g7ji7:1m0YFg:Aa7k5PNSH63jyl6nB7S2plMVTpekNAQvqgSrwumP-dc', '2021-07-19 23:43:48.777661'),
('gi348hnymu5z8xcbi3c8rnlpxwaexj61', '.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MykYKffMUF-UNsJ3qHdOs-9rcuc-K7wgw5-7UjPy-H-HVQY9VtbL53VOhVtghJmytYZTaTQyiyySo6cJ1TCB2P9BISUCHXxxakUBBB7fwDoDDgb:1m14Ax:Rs0lV7lGve0va6mfVn1XJ0aT24UZXZH-XAoyOtOScqc', '2021-07-21 09:49:03.047643'),
('now56dmlhlflbe71utjsrxd3v1nmgmke', '.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MykYKffMUF-UNsJ3qHdOs-9rcuc-K7wgw5-7UjPy-H-HVQY9VtbL53VOhVtghJmytYZTaTQyiyySo6cJ1TCB2P9BISUCHXxxakUBBB7fwDoDDgb:1m0qwM:nI3wnAOV31f58PUFZoGjhU7rk33yorgG1tQCotCYjGQ', '2021-07-20 19:41:06.253679'),
('pyx4akgm5rjnhj2ud1rgeqtea2ghwamm', '.eJxVjMsOwiAQRf-FtSGU4TF16d5vIMAwUjUlKe3K-O_apAvd3nPOfYkQt7WGrZclTCTOYlDi9DummB9l3gnd43xrMrd5XaYkd0UetMtro_K8HO7fQY29fmuTRoMuY9JkM4-KAHyKo7YMyBqLAzAKbVI5WialkaEM3hB7jY4BxPsD_lg3tQ:1m0Cd0:CzVXwesc3G0kEUlV3PJ85EEpyP1TNOXQaBwaA7lqw1Y', '2021-07-19 00:38:26.638323'),
('un70w47pjz01pj7egflyd98b4laboyk4', 'e30:1m0AMh:CQAjMjVAPm94l8EaFslN1zBhwo4rtkAcdjxYQ8iiUWA', '2021-07-18 22:13:27.445695'),
('vl1kn5zg4ftmkc799si0uzw1fgyb797b', '.eJxVjMsOwiAQRf-FtSFAZwBduu83kBlgpGrapI-V8d-1SRe6veec-1KJtrWlbalzGoq6KAvq9Dsy5Ucdd1LuNN4mnadxnQfWu6IPuuh-KvV5Pdy_g0ZL-9YiBS25zGiAjA8sjB04hhCzYOy8eBDMBHg26CwWYRcEJEfoMHqv3h8S6Dfg:1m13h7:0cvbwI2ehZ9MHn42Bg9DYjTdXD6Vst4LU2tgBZNUXS0', '2021-07-21 09:18:13.302097'),
('vvlxzydai2sn0pumms6tmgvknlj52kcb', '.eJxVjMsOwiAQRf-FtSGU4TF16d5vIMAwUjUlKe3K-O_apAvd3nPOfYkQt7WGrZclTCTOYlDi9DummB9l3gnd43xrMrd5XaYkd0UetMtro_K8HO7fQY29fmuTRoMuY9JkM4-KAHyKo7YMyBqLAzAKbVI5WialkaEM3hB7jY4BxPsD_lg3tQ:1m0Brr:qeGpY1Zj-t3eYy8JtReXuRHHBhS635YqWnt4spROQm8', '2021-07-18 23:49:43.477570'),
('wwj8flt2tes4va1my1hxa0yspr2ad6th', 'e30:1m14CC:5ZYaNwIcmHpAsASrcbwrljGUEOqeRTDtWKXxSoRFTOw', '2021-07-21 09:50:20.619419');

-- --------------------------------------------------------

--
-- Table structure for table `Edificio`
--

CREATE TABLE `Edificio` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `CampusID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Edificio`
--

INSERT INTO `Edificio` (`ID`, `Nome`, `CampusID`) VALUES
(1, 'G1 - Gambelas', 1),
(2, 'G2 - Gambelas', 1),
(3, 'G3 - Gambelas', 1),
(4, 'P1 - Penha', 2),
(5, 'P2 - Penha', 2),
(6, 'P3 - Penha', 2),
(7, 'CP - Gambelas', 1);

-- --------------------------------------------------------

--
-- Table structure for table `Equipamento`
--

CREATE TABLE `Equipamento` (
  `RecursoID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Evento`
--

CREATE TABLE `Evento` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL,
  `Descrição` varchar(255) DEFAULT NULL,
  `Data` date DEFAULT NULL,
  `Hora` time(6) DEFAULT NULL,
  `Duração` double DEFAULT NULL,
  `Valor` double NOT NULL,
  `Evento pagoID` int(11) DEFAULT NULL,
  `ProponenteUtilizadorID` int(11) DEFAULT NULL,
  `Tipo de eventoID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Evento_eventoequipamentos`
--

CREATE TABLE `Evento_eventoequipamentos` (
  `ID` int(11) NOT NULL,
  `Equipamento` int(11) DEFAULT NULL,
  `Evento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Evento_eventolocais`
--

CREATE TABLE `Evento_eventolocais` (
  `ID` int(11) NOT NULL,
  `Evento` int(11) DEFAULT NULL,
  `Local` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Evento_eventoservicos`
--

CREATE TABLE `Evento_eventoservicos` (
  `ID` int(11) NOT NULL,
  `Evento` int(11) DEFAULT NULL,
  `Servico` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Feedback`
--

CREATE TABLE `Feedback` (
  `ID` int(11) NOT NULL,
  `InscriçãoID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Formulário`
--

CREATE TABLE `Formulário` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `Publico` tinyint(1) NOT NULL,
  `Tipo de eventoID` int(11) DEFAULT NULL,
  `Tipo de FormulárioID` int(11) DEFAULT NULL,
  `Evento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Formulário_Pergunta`
--

CREATE TABLE `Formulário_Pergunta` (
  `ID` int(11) NOT NULL,
  `Pos` int(11) DEFAULT NULL,
  `FormulárioID` int(11) NOT NULL,
  `PerguntaID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Inscrição`
--

CREATE TABLE `Inscrição` (
  `ID` int(11) NOT NULL,
  `CheckIn` tinyint(1) NOT NULL,
  `Valido` tinyint(1) NOT NULL,
  `EventoID` int(11) NOT NULL,
  `ParticipanteUtilizadorID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Mensagem`
--

CREATE TABLE `Mensagem` (
  `ID` int(11) NOT NULL,
  `Remetente` varchar(255) DEFAULT NULL,
  `Receptor` varchar(255) DEFAULT NULL,
  `Conteúdo` varchar(255) DEFAULT NULL,
  `Data` date DEFAULT NULL,
  `Assunto` varchar(255) DEFAULT NULL,
  `UtilizadorID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Opção de resposta`
--

CREATE TABLE `Opção de resposta` (
  `ID` int(11) NOT NULL,
  `Opção` varchar(255) DEFAULT NULL,
  `PerguntaID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Pagamento`
--

CREATE TABLE `Pagamento` (
  `ID` int(11) NOT NULL,
  `Divida` double NOT NULL,
  `Data` date DEFAULT NULL,
  `Hora` time(6) DEFAULT NULL,
  `InscriçãoID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Participante`
--

CREATE TABLE `Participante` (
  `UtilizadorID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Participante`
--

INSERT INTO `Participante` (`UtilizadorID`) VALUES
(11),
(13),
(14),
(15),
(16);

-- --------------------------------------------------------

--
-- Table structure for table `Pedido de recurso`
--

CREATE TABLE `Pedido de recurso` (
  `ID` int(11) NOT NULL,
  `Quantidade` int(11) NOT NULL,
  `Dia inicial` date DEFAULT NULL,
  `Hora inicial` time(6) DEFAULT NULL,
  `Dia final` date DEFAULT NULL,
  `Hora final` time(6) DEFAULT NULL,
  `Capacidade` int(11) DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL,
  `EventoID` int(11) DEFAULT NULL,
  `Tipo de recursoID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Pergunta`
--

CREATE TABLE `Pergunta` (
  `ID` int(11) NOT NULL,
  `Pergunta` varchar(255) DEFAULT NULL,
  `Obrigatório` tinyint(1) NOT NULL,
  `NumeroMaximoDeEscolhas` int(11) DEFAULT NULL,
  `temporario` tinyint(1) NOT NULL,
  `Tipo de perguntaID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Proponente`
--

CREATE TABLE `Proponente` (
  `UtilizadorID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Proponente`
--

INSERT INTO `Proponente` (`UtilizadorID`) VALUES
(11),
(13),
(14),
(15),
(16);

-- --------------------------------------------------------

--
-- Table structure for table `Recurso`
--

CREATE TABLE `Recurso` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `Estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Recurso_estado`
--

CREATE TABLE `Recurso_estado` (
  `ID` int(11) NOT NULL,
  `Estado` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Recurso_estado`
--

INSERT INTO `Recurso_estado` (`ID`, `Estado`) VALUES
(1, 'Disponivel'),
(2, 'Indisponivel');

-- --------------------------------------------------------

--
-- Table structure for table `Requisição`
--

CREATE TABLE `Requisição` (
  `ID` int(11) NOT NULL,
  `Dia inicial` date DEFAULT NULL,
  `Hora inicial` time(6) DEFAULT NULL,
  `Dia final` date DEFAULT NULL,
  `Hora final` time(6) DEFAULT NULL,
  `EventoID` int(11) DEFAULT NULL,
  `RecursoID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Resposta`
--

CREATE TABLE `Resposta` (
  `ID` int(11) NOT NULL,
  `Resposta` varchar(2048) DEFAULT NULL,
  `EventoID` int(11) DEFAULT NULL,
  `FeedbackID` int(11) DEFAULT NULL,
  `InscriçãoID` int(11) DEFAULT NULL,
  `PerguntaID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Sala`
--

CREATE TABLE `Sala` (
  `RecursoID` int(11) NOT NULL,
  `Lugares` int(11) DEFAULT NULL,
  `EdificioID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Serviço`
--

CREATE TABLE `Serviço` (
  `RecursoID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tipo de evento`
--

CREATE TABLE `Tipo de evento` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Tipo de evento`
--

INSERT INTO `Tipo de evento` (`ID`, `Nome`) VALUES
(1, 'Palestra'),
(2, 'Workshop'),
(3, 'Seminário');

-- --------------------------------------------------------

--
-- Table structure for table `Tipo de Formulário`
--

CREATE TABLE `Tipo de Formulário` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Tipo de Formulário`
--

INSERT INTO `Tipo de Formulário` (`ID`, `Nome`) VALUES
(1, 'Inscrição'),
(2, 'Proposta de evento'),
(3, 'Feedback');

-- --------------------------------------------------------

--
-- Table structure for table `Tipo de pergunta`
--

CREATE TABLE `Tipo de pergunta` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Tipo de pergunta`
--

INSERT INTO `Tipo de pergunta` (`ID`, `Nome`) VALUES
(1, 'Escolha Multipla'),
(2, 'Resposta Curta'),
(3, 'Resposta Média'),
(4, 'Resposta Longa');

-- --------------------------------------------------------

--
-- Table structure for table `Tipo de recurso`
--

CREATE TABLE `Tipo de recurso` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Tipo de recurso`
--

INSERT INTO `Tipo de recurso` (`ID`, `Nome`) VALUES
(1, 'Equipamento'),
(2, 'Sala'),
(3, 'Serviço');

-- --------------------------------------------------------

--
-- Table structure for table `utilizador`
--

CREATE TABLE `utilizador` (
  `id` int(11) NOT NULL,
  `nome` varchar(200) NOT NULL,
  `email` varchar(60) NOT NULL,
  `telefone` int(11) NOT NULL,
  `password` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `TipoUtilizador` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `utilizador`
--

INSERT INTO `utilizador` (`id`, `nome`, `email`, `telefone`, `password`, `username`, `date_joined`, `last_login`, `is_admin`, `is_active`, `is_staff`, `is_superuser`, `TipoUtilizador`) VALUES
(10, '', 'admin@ualg.pt', 0, 'pbkdf2_sha256$260000$dI7otMIxuq0SNQzAo04qPa$eIGKT5k+g4YZQ0rb3vXZIdbdGRukDEAZOxrfNqieQ9M=', 'admin', '2021-07-04 23:33:47.781477', '2021-07-07 09:49:00.528166', 1, 1, 1, 1, 'Administrador');

-- --------------------------------------------------------

--
-- Table structure for table `Utilizador_Mensagem`
--

CREATE TABLE `Utilizador_Mensagem` (
  `ID` int(11) NOT NULL,
  `MensagemID` int(11) DEFAULT NULL,
  `UtilizadorID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Administrador`
--
ALTER TABLE `Administrador`
  ADD PRIMARY KEY (`UtilizadorID`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `Campus`
--
ALTER TABLE `Campus`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Nome` (`Nome`);

--
-- Indexes for table `Certificado de Participação`
--
ALTER TABLE `Certificado de Participação`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `Edificio`
--
ALTER TABLE `Edificio`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Edificio_CampusID_f21d61a8_fk_Campus_ID` (`CampusID`);

--
-- Indexes for table `Equipamento`
--
ALTER TABLE `Equipamento`
  ADD PRIMARY KEY (`RecursoID`);

--
-- Indexes for table `Evento`
--
ALTER TABLE `Evento`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Evento_ProponenteUtilizador_0562bf95_fk_Proponent` (`ProponenteUtilizadorID`),
  ADD KEY `Evento_Tipo de eventoID_1e254a07_fk_Tipo de evento_ID` (`Tipo de eventoID`);

--
-- Indexes for table `Evento_eventoequipamentos`
--
ALTER TABLE `Evento_eventoequipamentos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Evento_eventoequipam_Equipamento_6ed9763c_fk_Equipamen` (`Equipamento`),
  ADD KEY `Evento_eventoequipamentos_Evento_f28e8d3f_fk_Evento_ID` (`Evento`);

--
-- Indexes for table `Evento_eventolocais`
--
ALTER TABLE `Evento_eventolocais`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Evento_eventolocais_Evento_1dc80c87_fk_Evento_ID` (`Evento`),
  ADD KEY `Evento_eventolocais_Local_aaf7338e_fk_Sala_RecursoID` (`Local`);

--
-- Indexes for table `Evento_eventoservicos`
--
ALTER TABLE `Evento_eventoservicos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Evento_eventoservicos_Evento_0658d393_fk_Evento_ID` (`Evento`),
  ADD KEY `Evento_eventoservicos_Servico_78269853_fk_Serviço_RecursoID` (`Servico`);

--
-- Indexes for table `Feedback`
--
ALTER TABLE `Feedback`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Feedback_InscriçãoID_5d6064a3_fk_Inscrição_ID` (`InscriçãoID`);

--
-- Indexes for table `Formulário`
--
ALTER TABLE `Formulário`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Formulário_Tipo de FormulárioID_a95ae2d6_fk_Tipo de F` (`Tipo de FormulárioID`),
  ADD KEY `Formulário_Tipo de eventoID_7da3b4e5_fk_Tipo de evento_ID` (`Tipo de eventoID`),
  ADD KEY `Formulário_Evento_64b0dda0_fk_Evento_ID` (`Evento`);

--
-- Indexes for table `Formulário_Pergunta`
--
ALTER TABLE `Formulário_Pergunta`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Formulário_Pergunta_FormulárioID_b2a4ca42` (`FormulárioID`),
  ADD KEY `Formulário_Pergunta_PerguntaID_3af1d6b9` (`PerguntaID`);

--
-- Indexes for table `Inscrição`
--
ALTER TABLE `Inscrição`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Inscrição_EventoID_40a8ce63_fk_Evento_ID` (`EventoID`),
  ADD KEY `Inscrição_ParticipanteUtilizad_eb728d76_fk_Participa` (`ParticipanteUtilizadorID`);

--
-- Indexes for table `Mensagem`
--
ALTER TABLE `Mensagem`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Mensagem_UtilizadorID_83df9f85_fk_utilizador_id` (`UtilizadorID`);

--
-- Indexes for table `Opção de resposta`
--
ALTER TABLE `Opção de resposta`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Opção de resposta_PerguntaID_3b57397b_fk_Pergunta_ID` (`PerguntaID`);

--
-- Indexes for table `Pagamento`
--
ALTER TABLE `Pagamento`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Pagamento_InscriçãoID_52c45601_fk_Inscrição_ID` (`InscriçãoID`);

--
-- Indexes for table `Participante`
--
ALTER TABLE `Participante`
  ADD PRIMARY KEY (`UtilizadorID`);

--
-- Indexes for table `Pedido de recurso`
--
ALTER TABLE `Pedido de recurso`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Pedido de recurso_EventoID_8b19122d_fk_Evento_ID` (`EventoID`),
  ADD KEY `Pedido de recurso_Tipo de recursoID_e8863947_fk_Tipo de r` (`Tipo de recursoID`);

--
-- Indexes for table `Pergunta`
--
ALTER TABLE `Pergunta`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Pergunta_Tipo de perguntaID_ac36cfca_fk_Tipo de pergunta_ID` (`Tipo de perguntaID`);

--
-- Indexes for table `Proponente`
--
ALTER TABLE `Proponente`
  ADD PRIMARY KEY (`UtilizadorID`);

--
-- Indexes for table `Recurso`
--
ALTER TABLE `Recurso`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Recurso_Estado_e7c0f028_fk_Recurso_estado_ID` (`Estado`);

--
-- Indexes for table `Recurso_estado`
--
ALTER TABLE `Recurso_estado`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Requisição`
--
ALTER TABLE `Requisição`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `EventoID` (`EventoID`),
  ADD UNIQUE KEY `RecursoID` (`RecursoID`);

--
-- Indexes for table `Resposta`
--
ALTER TABLE `Resposta`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Resposta_EventoID_c8f2b98e_fk_Evento_ID` (`EventoID`),
  ADD KEY `Resposta_FeedbackID_661c6c54_fk_Feedback_ID` (`FeedbackID`),
  ADD KEY `Resposta_InscriçãoID_90f47532_fk_Inscrição_ID` (`InscriçãoID`),
  ADD KEY `Resposta_PerguntaID_1c45255a_fk_Pergunta_ID` (`PerguntaID`);

--
-- Indexes for table `Sala`
--
ALTER TABLE `Sala`
  ADD PRIMARY KEY (`RecursoID`),
  ADD KEY `Sala_EdificioID_fa3c289d_fk_Edificio_ID` (`EdificioID`);

--
-- Indexes for table `Serviço`
--
ALTER TABLE `Serviço`
  ADD PRIMARY KEY (`RecursoID`);

--
-- Indexes for table `Tipo de evento`
--
ALTER TABLE `Tipo de evento`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Tipo de Formulário`
--
ALTER TABLE `Tipo de Formulário`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Tipo de pergunta`
--
ALTER TABLE `Tipo de pergunta`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Tipo de recurso`
--
ALTER TABLE `Tipo de recurso`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Nome` (`Nome`);

--
-- Indexes for table `utilizador`
--
ALTER TABLE `utilizador`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `Utilizador_Mensagem`
--
ALTER TABLE `Utilizador_Mensagem`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Utilizador_Mensagem_MensagemID_a583205d_fk_Mensagem_ID` (`MensagemID`),
  ADD KEY `Utilizador_Mensagem_UtilizadorID_66c06b77_fk_utilizador_id` (`UtilizadorID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=153;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Campus`
--
ALTER TABLE `Campus`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `Certificado de Participação`
--
ALTER TABLE `Certificado de Participação`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
--
-- AUTO_INCREMENT for table `Edificio`
--
ALTER TABLE `Edificio`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `Evento`
--
ALTER TABLE `Evento`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `Evento_eventoequipamentos`
--
ALTER TABLE `Evento_eventoequipamentos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `Evento_eventolocais`
--
ALTER TABLE `Evento_eventolocais`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `Evento_eventoservicos`
--
ALTER TABLE `Evento_eventoservicos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `Feedback`
--
ALTER TABLE `Feedback`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Formulário`
--
ALTER TABLE `Formulário`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `Formulário_Pergunta`
--
ALTER TABLE `Formulário_Pergunta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;
--
-- AUTO_INCREMENT for table `Inscrição`
--
ALTER TABLE `Inscrição`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
--
-- AUTO_INCREMENT for table `Mensagem`
--
ALTER TABLE `Mensagem`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Opção de resposta`
--
ALTER TABLE `Opção de resposta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `Pagamento`
--
ALTER TABLE `Pagamento`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `Pedido de recurso`
--
ALTER TABLE `Pedido de recurso`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `Pergunta`
--
ALTER TABLE `Pergunta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `Recurso`
--
ALTER TABLE `Recurso`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `Recurso_estado`
--
ALTER TABLE `Recurso_estado`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `Requisição`
--
ALTER TABLE `Requisição`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Resposta`
--
ALTER TABLE `Resposta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=147;
--
-- AUTO_INCREMENT for table `Tipo de evento`
--
ALTER TABLE `Tipo de evento`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `Tipo de Formulário`
--
ALTER TABLE `Tipo de Formulário`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `Tipo de pergunta`
--
ALTER TABLE `Tipo de pergunta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `Tipo de recurso`
--
ALTER TABLE `Tipo de recurso`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `utilizador`
--
ALTER TABLE `utilizador`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `Utilizador_Mensagem`
--
ALTER TABLE `Utilizador_Mensagem`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Administrador`
--
ALTER TABLE `Administrador`
  ADD CONSTRAINT `Administrador_UtilizadorID_40027ecf_fk_utilizador_id` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `Edificio`
--
ALTER TABLE `Edificio`
  ADD CONSTRAINT `Edificio_CampusID_f21d61a8_fk_Campus_ID` FOREIGN KEY (`CampusID`) REFERENCES `Campus` (`ID`);

--
-- Constraints for table `Equipamento`
--
ALTER TABLE `Equipamento`
  ADD CONSTRAINT `Equipamento_RecursoID_6d08a178_fk_Recurso_ID` FOREIGN KEY (`RecursoID`) REFERENCES `Recurso` (`ID`);

--
-- Constraints for table `Evento`
--
ALTER TABLE `Evento`
  ADD CONSTRAINT `Evento_ProponenteUtilizador_0562bf95_fk_Proponent` FOREIGN KEY (`ProponenteUtilizadorID`) REFERENCES `Proponente` (`UtilizadorID`),
  ADD CONSTRAINT `Evento_Tipo de eventoID_1e254a07_fk_Tipo de evento_ID` FOREIGN KEY (`Tipo de eventoID`) REFERENCES `Tipo de evento` (`ID`);

--
-- Constraints for table `Evento_eventoequipamentos`
--
ALTER TABLE `Evento_eventoequipamentos`
  ADD CONSTRAINT `Evento_eventoequipam_Equipamento_6ed9763c_fk_Equipamen` FOREIGN KEY (`Equipamento`) REFERENCES `Equipamento` (`RecursoID`),
  ADD CONSTRAINT `Evento_eventoequipamentos_Evento_f28e8d3f_fk_Evento_ID` FOREIGN KEY (`Evento`) REFERENCES `Evento` (`ID`);

--
-- Constraints for table `Evento_eventolocais`
--
ALTER TABLE `Evento_eventolocais`
  ADD CONSTRAINT `Evento_eventolocais_Evento_1dc80c87_fk_Evento_ID` FOREIGN KEY (`Evento`) REFERENCES `Evento` (`ID`),
  ADD CONSTRAINT `Evento_eventolocais_Local_aaf7338e_fk_Sala_RecursoID` FOREIGN KEY (`Local`) REFERENCES `Sala` (`RecursoID`);

--
-- Constraints for table `Evento_eventoservicos`
--
ALTER TABLE `Evento_eventoservicos`
  ADD CONSTRAINT `Evento_eventoservicos_Evento_0658d393_fk_Evento_ID` FOREIGN KEY (`Evento`) REFERENCES `Evento` (`ID`),
  ADD CONSTRAINT `Evento_eventoservicos_Servico_78269853_fk_Serviço_RecursoID` FOREIGN KEY (`Servico`) REFERENCES `Serviço` (`RecursoID`);

--
-- Constraints for table `Feedback`
--
ALTER TABLE `Feedback`
  ADD CONSTRAINT `Feedback_InscriçãoID_5d6064a3_fk_Inscrição_ID` FOREIGN KEY (`InscriçãoID`) REFERENCES `Inscrição` (`ID`);

--
-- Constraints for table `Formulário`
--
ALTER TABLE `Formulário`
  ADD CONSTRAINT `Formulário_Evento_64b0dda0_fk_Evento_ID` FOREIGN KEY (`Evento`) REFERENCES `Evento` (`ID`),
  ADD CONSTRAINT `Formulário_Tipo de FormulárioID_a95ae2d6_fk_Tipo de F` FOREIGN KEY (`Tipo de FormulárioID`) REFERENCES `Tipo de Formulário` (`ID`),
  ADD CONSTRAINT `Formulário_Tipo de eventoID_7da3b4e5_fk_Tipo de evento_ID` FOREIGN KEY (`Tipo de eventoID`) REFERENCES `Tipo de evento` (`ID`);

--
-- Constraints for table `Formulário_Pergunta`
--
ALTER TABLE `Formulário_Pergunta`
  ADD CONSTRAINT `Formulário_Pergunta_FormulárioID_b2a4ca42_fk_Formulário_ID` FOREIGN KEY (`FormulárioID`) REFERENCES `Formulário` (`ID`),
  ADD CONSTRAINT `Formulário_Pergunta_PerguntaID_3af1d6b9_fk_Pergunta_ID` FOREIGN KEY (`PerguntaID`) REFERENCES `Pergunta` (`ID`);

--
-- Constraints for table `Inscrição`
--
ALTER TABLE `Inscrição`
  ADD CONSTRAINT `Inscrição_EventoID_40a8ce63_fk_Evento_ID` FOREIGN KEY (`EventoID`) REFERENCES `Evento` (`ID`),
  ADD CONSTRAINT `Inscrição_ParticipanteUtilizad_eb728d76_fk_Participa` FOREIGN KEY (`ParticipanteUtilizadorID`) REFERENCES `Participante` (`UtilizadorID`);

--
-- Constraints for table `Mensagem`
--
ALTER TABLE `Mensagem`
  ADD CONSTRAINT `Mensagem_UtilizadorID_83df9f85_fk_utilizador_id` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`id`);

--
-- Constraints for table `Opção de resposta`
--
ALTER TABLE `Opção de resposta`
  ADD CONSTRAINT `Opção de resposta_PerguntaID_3b57397b_fk_Pergunta_ID` FOREIGN KEY (`PerguntaID`) REFERENCES `Pergunta` (`ID`);

--
-- Constraints for table `Pagamento`
--
ALTER TABLE `Pagamento`
  ADD CONSTRAINT `Pagamento_InscriçãoID_52c45601_fk_Inscrição_ID` FOREIGN KEY (`InscriçãoID`) REFERENCES `Inscrição` (`ID`);

--
-- Constraints for table `Participante`
--
ALTER TABLE `Participante`
  ADD CONSTRAINT `Participante_UtilizadorID_57dc5845_fk_utilizador_id` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`id`);

--
-- Constraints for table `Pedido de recurso`
--
ALTER TABLE `Pedido de recurso`
  ADD CONSTRAINT `Pedido de recurso_EventoID_8b19122d_fk_Evento_ID` FOREIGN KEY (`EventoID`) REFERENCES `Evento` (`ID`),
  ADD CONSTRAINT `Pedido de recurso_Tipo de recursoID_e8863947_fk_Tipo de r` FOREIGN KEY (`Tipo de recursoID`) REFERENCES `Tipo de recurso` (`ID`);

--
-- Constraints for table `Pergunta`
--
ALTER TABLE `Pergunta`
  ADD CONSTRAINT `Pergunta_Tipo de perguntaID_ac36cfca_fk_Tipo de pergunta_ID` FOREIGN KEY (`Tipo de perguntaID`) REFERENCES `Tipo de pergunta` (`ID`);

--
-- Constraints for table `Proponente`
--
ALTER TABLE `Proponente`
  ADD CONSTRAINT `Proponente_UtilizadorID_8d10e88a_fk_utilizador_id` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`id`);

--
-- Constraints for table `Recurso`
--
ALTER TABLE `Recurso`
  ADD CONSTRAINT `Recurso_Estado_e7c0f028_fk_Recurso_estado_ID` FOREIGN KEY (`Estado`) REFERENCES `Recurso_estado` (`ID`);

--
-- Constraints for table `Requisição`
--
ALTER TABLE `Requisição`
  ADD CONSTRAINT `Requisição_EventoID_202ac0c6_fk_Evento_ID` FOREIGN KEY (`EventoID`) REFERENCES `Evento` (`ID`),
  ADD CONSTRAINT `Requisição_RecursoID_68ed300a_fk_Recurso_ID` FOREIGN KEY (`RecursoID`) REFERENCES `Recurso` (`ID`);

--
-- Constraints for table `Resposta`
--
ALTER TABLE `Resposta`
  ADD CONSTRAINT `Resposta_EventoID_c8f2b98e_fk_Evento_ID` FOREIGN KEY (`EventoID`) REFERENCES `Evento` (`ID`),
  ADD CONSTRAINT `Resposta_FeedbackID_661c6c54_fk_Feedback_ID` FOREIGN KEY (`FeedbackID`) REFERENCES `Feedback` (`ID`),
  ADD CONSTRAINT `Resposta_InscriçãoID_90f47532_fk_Inscrição_ID` FOREIGN KEY (`InscriçãoID`) REFERENCES `Inscrição` (`ID`),
  ADD CONSTRAINT `Resposta_PerguntaID_1c45255a_fk_Pergunta_ID` FOREIGN KEY (`PerguntaID`) REFERENCES `Pergunta` (`ID`);

--
-- Constraints for table `Sala`
--
ALTER TABLE `Sala`
  ADD CONSTRAINT `Sala_EdificioID_fa3c289d_fk_Edificio_ID` FOREIGN KEY (`EdificioID`) REFERENCES `Edificio` (`ID`),
  ADD CONSTRAINT `Sala_RecursoID_f6bac90c_fk_Recurso_ID` FOREIGN KEY (`RecursoID`) REFERENCES `Recurso` (`ID`);

--
-- Constraints for table `Serviço`
--
ALTER TABLE `Serviço`
  ADD CONSTRAINT `Serviço_RecursoID_8884d46d_fk_Recurso_ID` FOREIGN KEY (`RecursoID`) REFERENCES `Recurso` (`ID`);

--
-- Constraints for table `Utilizador_Mensagem`
--
ALTER TABLE `Utilizador_Mensagem`
  ADD CONSTRAINT `Utilizador_Mensagem_MensagemID_a583205d_fk_Mensagem_ID` FOREIGN KEY (`MensagemID`) REFERENCES `Mensagem` (`ID`),
  ADD CONSTRAINT `Utilizador_Mensagem_UtilizadorID_66c06b77_fk_utilizador_id` FOREIGN KEY (`UtilizadorID`) REFERENCES `utilizador` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

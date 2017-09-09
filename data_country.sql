-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 07, 2017 at 02:11 AM
-- Server version: 10.1.22-MariaDB
-- PHP Version: 7.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ojmjqgeaosnbxecj`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_country`
--

CREATE TABLE `ojmjqgeaosnbxecj`.`data_country` (
  `id` bigint(20) DEFAULT NULL,
  `country_name` text,
  `country_flag` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `data_country`
--

INSERT INTO `ojmjqgeaosnbxecj`.`data_country` (`id`, `country_name`, `country_flag`) VALUES
(0, 'Austria', NULL),
(1, 'Belgium', NULL),
(2, 'Bulgaria', NULL),
(3, 'Czech Republic', NULL),
(4, 'Denmark', NULL),
(5, 'Estonia', NULL),
(6, 'Finland', NULL),
(7, 'France', NULL),
(8, 'Germany', NULL),
(9, 'Greece', NULL),
(10, 'Ireland', NULL),
(11, 'Italy', NULL),
(12, 'Netherlands', NULL),
(13, 'Poland', NULL),
(14, 'Portugal', NULL),
(15, 'Romania', NULL),
(16, 'Slovenia', NULL),
(17, 'Spain', NULL),
(18, 'Sweden', NULL),
(19, 'United Kingdom', NULL),
(20, 'Slovakia', NULL),
(21, 'Croatia', NULL),
(22, 'Hungary', NULL),
(23, 'Lithuania', NULL),
(24, 'Malta', NULL),
(25, 'Cyprus', NULL),
(26, 'Latvia', NULL),
(27, 'Luxembourg', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_country`
--
ALTER TABLE `data_country`
  ADD KEY `ix_data_country_index` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

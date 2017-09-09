-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 21, 2017 at 06:42 PM
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
-- Database: `recommend_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `engine_rating`
--

CREATE TABLE `opo0gt46iooa286a`.`engine_rating` (
  `id` int(11) NOT NULL,
  `rating` decimal(10,6) NOT NULL,
  `movieId_id` int(11) NOT NULL,
  `userId_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `engine_rating`
--
ALTER TABLE `opo0gt46iooa286a`.`engine_rating`
  ADD PRIMARY KEY (`id`),
  ADD KEY `engine_rating_movieId_id_3e7dfebd_fk_engine_movie_movieId` (`movieId_id`),
  ADD KEY `engine_rating_userId_id_18941690_fk_auth_user_id` (`userId_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `engine_rating`
--
ALTER TABLE `engine_rating`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `engine_rating`
--
ALTER TABLE `engine_rating`
  ADD CONSTRAINT `engine_rating_movieId_id_3e7dfebd_fk_engine_movie_movieId` FOREIGN KEY (`movieId_id`) REFERENCES `engine_movie` (`movieId`),
  ADD CONSTRAINT `engine_rating_userId_id_18941690_fk_auth_user_id` FOREIGN KEY (`userId_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

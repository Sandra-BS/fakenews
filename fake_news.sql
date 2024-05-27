-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2023 at 08:40 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fake_news`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_revw`
--

CREATE TABLE `user_revw` (
  `id` int(11) NOT NULL,
  `nme` varchar(50) NOT NULL,
  `cmnt` text NOT NULL,
  `rat` int(11) NOT NULL,
  `dt` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_revw`
--

INSERT INTO `user_revw` (`id`, `nme`, `cmnt`, `rat`, `dt`) VALUES
(1, 'Vineeth A V', 'Very Nice Experience.. User Friendly UI', 5, '2023-04-19'),
(2, 'Midhun', 'Good ', 2, '2023-04-19'),
(3, 'Sandra', 'Nice teamwork.....', 5, '2023-04-19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_revw`
--
ALTER TABLE `user_revw`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_revw`
--
ALTER TABLE `user_revw`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

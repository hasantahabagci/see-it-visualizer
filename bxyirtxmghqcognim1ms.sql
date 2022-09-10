-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: bxyirtxmghqcognim1ms-mysql.services.clever-cloud.com:3306
-- Generation Time: Jun 02, 2022 at 09:47 AM
-- Server version: 8.0.22-13
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bxyirtxmghqcognim1ms`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Name` varchar(20) DEFAULT NULL,
  `Surname` varchar(20) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Password` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Name`, `Surname`, `Email`, `Password`) VALUES
('Ali', 'Dursun', 'alidursun@gmail.com', '12345\0\0\0\0\0\0\0\0\0\0\0'),
('Hasan Taha', 'Bağcı', 'hasantahabagci@gmail.com', 'asd123'),
('Yusuf Faruk', 'Güldemir', 'yusufarukguldemir@gmail.com', '123asd'),
('Asım', 'Duman', 'asimdmn@gmail.com', 'asim123');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

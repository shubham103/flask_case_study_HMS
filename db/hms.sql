-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 18, 2020 at 05:42 PM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hms`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `ws_ssn` int(9) NOT NULL,
  `ws_pat_id` int(9) NOT NULL,
  `ws_pat_name` varchar(20) NOT NULL,
  `ws_age` int(3) DEFAULT NULL,
  `ws_doj` varchar(9) DEFAULT NULL,
  `ws_rtype` varchar(1) NOT NULL,
  `ws_adrs` varchar(20) NOT NULL,
  `ws_city` varchar(20) NOT NULL,
  `ws_state` varchar(20) NOT NULL,
  `status` text NOT NULL,
  `fee` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




-- --------------------------------------------------------


--
-- Table structure for table `medicineissued`
--

CREATE TABLE `medicineissued` (
  `ws_pat_id` int(9) NOT NULL,
  `ws_med_name` varchar(20) NOT NULL,
  `ws_qty` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



-- --------------------------------------------------------
--
-- Table structure for table `medicinemaster`
--

CREATE TABLE `medicinemaster` (
  `ws_med_id` int(9) NOT NULL,
  `ws_med_name` varchar(20) NOT NULL,
  `ws_qty` int(5) NOT NULL,
  `ws_amount` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --------------------------------------------------------
--
-- Table structure for table `diagnostics`
--

CREATE TABLE `diagnostics` (
  `ws_pat_id` int(9) NOT NULL,
  `ws_test_id` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



-- --------------------------------------------------------
--
-- Table structure for table `diagnosticsmaster`
--

CREATE TABLE `diagnosticsmaster` (
  `ws_test_id` int(9) NOT NULL,
  `ws_test_name` text NOT NULL,
  `ws_test_amount` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



-- --------------------------------------------------------

--
-- Table structure for table `userstore`
--

CREATE TABLE `userstore` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



--
-- Indexes for dumped tables
--



--
-- Indexes for table `medicineissued`
--
ALTER TABLE `medicineissued`
  ADD PRIMARY KEY (`ws_pat_id`);

--
-- Indexes for table `medicinemaster`
--
ALTER TABLE `medicinemaster`
  ADD UNIQUE KEY `ws_med_id` (`ws_med_id`);
  
  
--
-- Indexes for table `diagnostics`
--
ALTER TABLE `diagnostics`
  ADD PRIMARY KEY (`ws_pat_id`);
  

--
-- Indexes for table `diagnosticsmaster`
--
ALTER TABLE `diagnosticsmaster`
  ADD PRIMARY KEY (`ws_test_id`);
  
  
  
  
  

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `ws_pat_id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `medicinemaster`
--
ALTER TABLE `medicinemaster`
  MODIFY `ws_med_id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
  
--
-- AUTO_INCREMENT for table `diagnosticsmaster`
--
ALTER TABLE `diagnosticsmaster`
  MODIFY `ws_test_id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;  
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

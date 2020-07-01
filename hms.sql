-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 01, 2020 at 04:23 PM
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
-- Table structure for table `diagnostics`
--

CREATE TABLE `diagnostics` (
  `ssnid` int(9) NOT NULL,
  `dname` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `diagnostics`
--

INSERT INTO `diagnostics` (`ssnid`, `dname`, `amount`) VALUES
(2, 'Covaxin', 2000),
(3, 'Coronil', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `diagnosticsmaster`
--

CREATE TABLE `diagnosticsmaster` (
  `dname` varchar(20) NOT NULL,
  `amount` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `diagnosticsmaster`
--

INSERT INTO `diagnosticsmaster` (`dname`, `amount`) VALUES
('Covaxin', 2000),
('Coronil', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `medicineissued`
--

CREATE TABLE `medicineissued` (
  `ssnid` int(9) NOT NULL,
  `mname` varchar(20) NOT NULL,
  `quantity` int(5) NOT NULL,
  `rate` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medicineissued`
--

INSERT INTO `medicineissued` (`ssnid`, `mname`, `quantity`, `rate`) VALUES
(2, 'Covaxin', 1, 2000),
(3, 'Covaxin', 1, 2000);

-- --------------------------------------------------------

--
-- Table structure for table `medicinemaster`
--

CREATE TABLE `medicinemaster` (
  `mname` text NOT NULL,
  `quantity` int(5) NOT NULL,
  `rate` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medicinemaster`
--

INSERT INTO `medicinemaster` (`mname`, `quantity`, `rate`) VALUES
('Covaxin', 1, 2000),
('Coronil', 20, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `ssnid` int(9) NOT NULL,
  `name` varchar(20) NOT NULL,
  `age` int(3) DEFAULT NULL,
  `admission_date` varchar(15) DEFAULT NULL,
  `bed` varchar(20) NOT NULL,
  `address` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `status` text NOT NULL,
  `fee` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`ssnid`, `name`, `age`, `admission_date`, `bed`, `address`, `city`, `state`, `status`, `fee`) VALUES
(4, 'Arsalan', 23, '01-07-2020', 'Single', 'Phulwari Sharif', 'Bihar', 'Patna', 'Discharged', 0);

-- --------------------------------------------------------

--
-- Table structure for table `userstore`
--

CREATE TABLE `userstore` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userstore`
--

INSERT INTO `userstore` (`username`, `password`) VALUES
('shubham', 'shubham@123');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

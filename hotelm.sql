-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 05, 2019 at 08:16 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.1.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelm`
--

-- --------------------------------------------------------

--
-- Table structure for table `billing_sy`
--

CREATE TABLE `billing_sy` (
  `order_no` int(11) NOT NULL,
  `qty_ff` int(11) NOT NULL,
  `amount_ff` int(11) NOT NULL,
  `qnty_burg` int(11) NOT NULL,
  `burg_amount` int(11) NOT NULL,
  `qnty_san` int(11) NOT NULL,
  `san_amount` int(11) NOT NULL,
  `qty_pasta` int(11) NOT NULL,
  `pasta_amount` int(11) NOT NULL,
  `qnty_thali` int(11) NOT NULL,
  `thali_amount` int(11) NOT NULL,
  `qnty_coffe` int(11) NOT NULL,
  `coffe_amount` int(11) NOT NULL,
  `total_qty` int(11) NOT NULL,
  `net_amount` int(11) NOT NULL,
  `gst` int(11) NOT NULL,
  `total_amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `billing_sy`
--

INSERT INTO `billing_sy` (`order_no`, `qty_ff`, `amount_ff`, `qnty_burg`, `burg_amount`, `qnty_san`, `san_amount`, `qty_pasta`, `pasta_amount`, `qnty_thali`, `thali_amount`, `qnty_coffe`, `coffe_amount`, `total_qty`, `net_amount`, `gst`, `total_amount`) VALUES
(123, 10, 400, 10, 350, 10, 400, 10, 800, 10, 1900, 10, 300, 60, 4150, 104, 4254),
(125, 12, 480, 14, 490, 1, 40, 12, 960, 5, 950, 7, 210, 51, 3130, 78, 3208),
(126, 5, 200, 4, 140, 5, 200, 5, 400, 6, 1140, 3, 90, 28, 2170, 54, 2224),
(127, 7, 280, 5, 175, 8, 320, 2, 160, 7, 1330, 4, 120, 33, 2385, 60, 2445),
(128, 8, 320, 5, 175, 2, 80, 7, 560, 8, 1520, 6, 180, 36, 2835, 71, 2906),
(129, 7, 280, 27, 945, 5, 200, 65, 5200, 22, 4180, 16, 480, 142, 11285, 282, 11567),
(130, 8, 320, 12, 420, 6, 240, 5, 400, 8, 1520, 7, 210, 46, 3110, 78, 3188),
(131, 15, 600, 7, 245, 6, 240, 7, 560, 3, 570, 7, 210, 45, 2425, 61, 2486),
(132, 8, 320, 2, 70, 6, 240, 7, 560, 9, 1710, 2, 60, 34, 2960, 74, 3034),
(133, 8, 320, 5, 175, 6, 240, 2, 160, 3, 570, 1, 30, 25, 1495, 37, 1532);

-- --------------------------------------------------------

--
-- Table structure for table `customer_points`
--

CREATE TABLE `customer_points` (
  `order_no` int(11) NOT NULL,
  `customer_name` varchar(30) NOT NULL,
  `phone_no` bigint(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `customer_points` int(11) NOT NULL,
  `total_points` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_points`
--

INSERT INTO `customer_points` (`order_no`, `customer_name`, `phone_no`, `email`, `customer_points`, `total_points`) VALUES
(56, 'bhavna', 965842856, 'choti@gmail.com', 56, 456),
(132, 'rama', 9664665842, 'rama123@gmail.com', 607, 607),
(126, 'shayama', 9664636842, 'shayama123@gmail.com', 445, 445),
(127, 'raman', 9665636842, 'raman123@gmail.com', 489, 489),
(128, 'gautam', 9666636842, 'gautam123@gmail.com', 581, 581),
(130, 'rajan', 9662636842, 'rajan123@gmail.com', 642, 642),
(131, 'shubham', 9656636842, 'shubham123@gmail.com', 637, 637),
(132, 'arjun', 9659636842, 'arjun563@gmail.com', 637, 637);

-- --------------------------------------------------------

--
-- Table structure for table `reset_pass`
--

CREATE TABLE `reset_pass` (
  `user_name` varchar(30) NOT NULL,
  `phone_no` bigint(20) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reset_pass`
--

INSERT INTO `reset_pass` (`user_name`, `phone_no`, `password`) VALUES
('virender', 9654665485, 'viru'),
('virnay rawat', 8956825462, 'vinay124'),
('sagar aggarwal', 8956568920, 'sag345'),
('bhavna rati', 8956568928, 'bahv12'),
('sumit singh', 8956568528, 'sumit11'),
('sumit sharma', 8956568585, 'sumit124'),
('sumit sharma', 8956568585, 'sumit124'),
('rahul dagar', 8665568520, 'rahul123'),
('sumit sharma', 866556520, 'sumit125'),
('pramod kumar', 8956856820, 'pramo13'),
('sohan', 8956886820, 'soh34');

-- --------------------------------------------------------

--
-- Table structure for table `staff_details`
--

CREATE TABLE `staff_details` (
  `emp_id` int(11) NOT NULL,
  `emp_name` varchar(30) NOT NULL,
  `emp_password` varchar(30) NOT NULL,
  `shift` varchar(30) NOT NULL,
  `contact_no` bigint(20) NOT NULL,
  `emp_address` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff_details`
--

INSERT INTO `staff_details` (`emp_id`, `emp_name`, `emp_password`, `shift`, `contact_no`, `emp_address`) VALUES
(25, 'virender', 'viru', 'morning', 9654665485, 'saket'),
(101, 'virnay rawat', 'vinay124', 'evening', 8956825462, 'maidan giri'),
(102, 'sagar aggarwal', 'sag345', 'night', 8956568920, 'chattar pur'),
(103, 'bhavna rati', 'bahv12', 'morning', 8956568928, 'chattar pur'),
(104, 'sumit singh', 'sumit11', 'morning', 8956568528, 'chirag delhi'),
(105, 'sumit sharma', 'sumit124', 'evening ', 8956568585, 'malvi nagar'),
(105, 'sumit sharma', 'sumit124', 'evening ', 8956568585, 'malvi nagar'),
(107, 'rahul dagar', 'rahul123', 'evening', 8665568520, 'asian park'),
(105, 'sumit sharma', 'sumit125', 'evening', 866556520, 'asian park'),
(106, 'pramod kumar', 'pramo13', 'night', 8956856820, 'khanpur'),
(108, 'sohan', 'soh34', 'night', 8956886820, 'bangla saheb');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

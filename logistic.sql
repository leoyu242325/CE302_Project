-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 12, 2021 at 11:14 PM
-- Server version: 5.7.33-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `logistic`
--

-- --------------------------------------------------------

--
-- Table structure for table `delivery`
--

CREATE TABLE `delivery` (
  `order_item_no` int(255) NOT NULL,
  `order_no` varchar(1000) NOT NULL,
  `order_item_id` int(255) NOT NULL,
  `quantity` int(255) NOT NULL,
  `tracking_no` varchar(1000) DEFAULT NULL,
  `weight` int(255) DEFAULT NULL,
  `delivery_price` int(255) DEFAULT NULL,
  `estimated_delivery_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `delivery`
--

INSERT INTO `delivery` (`order_item_no`, `order_no`, `order_item_id`, `quantity`, `tracking_no`, `weight`, `delivery_price`, `estimated_delivery_date`) VALUES
(100001, 'T0000001', 5, 4, 'QS8291083', 2, 50, '2020-04-24'),
(100002, 'T0000002', 3, 3, 'QS8291085', 8, 200, '2020-04-25'),
(100003, 'T0000002', 2, 1, 'QS8291085', 1, 13, '2020-04-25'),
(100004, 'T0000003', 4, 10, 'QT3846673', 3, 75, '2020-04-30'),
(100005, 'T0000004', 1, 1, 'Q8291083', 2, 50, '2020-06-30');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_item_no` int(255) NOT NULL,
  `Order_No` varchar(100) NOT NULL,
  `Phone_Number` int(20) NOT NULL,
  `Email_Address` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Item_Name` varchar(255) NOT NULL,
  `Quantity` int(255) NOT NULL,
  `Weight` int(255) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_item_no`, `Order_No`, `Phone_Number`, `Email_Address`, `Address`, `Item_Name`, `Quantity`, `Weight`, `Name`) VALUES
(100001, 'T0000001', 98765432, 'ashleylam@gmail.com', 'Rooms 1318-20 13 / F Hollywood Plaza 610 Nathan Road Mongkok', 'Japan apple, 5pcs/pack', 4, 2, 'Ashley Lam'),
(100002, 'T0000002', 64859637, 'jerryliu@gmail.com', 'Flat 301 3 / F. The Sun Lippo Plaza 28 Canton Road Tsim sha tsui Kowloon', 'Chair', 3, 8, 'Jerry Liu'),
(100003, 'T0000002', 64859637, 'jerryliu@gmail.com', 'Flat 301 3 / F. The Sun Lippo Plaza 28 Canton Road Tsim sha tsui Kowloon', 'Animal Watch', 1, 1, 'Jerry Liu'),
(100004, 'T0000003', 63015374, 'bonnieyiu@gmail.com', '803 South China Ind. Building 1 Chun Pin Street Kwai Chung', 'Coca cola, 12pcs/pack', 10, 3, 'Bonnie Yiu'),
(100005, 'T0000004', 90899988, 'queeniewong@gmail.com', '202-5 International Trade Center11-19 Sha Tsui Rd Nt', 'Wooden Table', 1, 8, 'Queenie Wong');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'Admin', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `delivery`
--
ALTER TABLE `delivery`
  ADD PRIMARY KEY (`order_item_no`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_item_no`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `delivery`
--
ALTER TABLE `delivery`
  MODIFY `order_item_no` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100006;
--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_item_no` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100006;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

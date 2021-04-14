-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 12, 2021 at 11:56 PM
-- Server version: 5.7.33-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `retailer`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(255) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `phone_number` varchar(1000) NOT NULL,
  `email_address` varchar(1000) NOT NULL,
  `address` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `name`, `phone_number`, `email_address`, `address`) VALUES
(112392, 'Queenie Wong', '90899988', 'queeniewong@gmail.com', '202-5 International Trade Center11-19 Sha Tsui Rd Nt'),
(152938, 'Ashley Lam', '98765432', 'ashleylam@gmail.com', 'Rooms 1318-20 13 / F Hollywood Plaza 610 Nathan Road Mongkok'),
(154321, 'Jerry Liu', '64859637', 'jerryliu@gmail.com', 'Flat 301 3 / F. The Sun Lippo Plaza 28 Canton Road Tsim sha tsui Kowloon'),
(169003, 'Bonnie Yiu', '63015374', 'bonnieyiu@gmail.com', '803 South China Ind. Building 1 Chun Pin Street Kwai Chung');

-- --------------------------------------------------------

--
-- Table structure for table `delivery_form`
--

CREATE TABLE `delivery_form` (
  `order_item_no` int(255) NOT NULL,
  `tracking_no` varchar(255) NOT NULL,
  `delivery_price` int(255) NOT NULL,
  `estimated_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `delivery_form`
--

INSERT INTO `delivery_form` (`order_item_no`, `tracking_no`, `delivery_price`, `estimated_date`) VALUES
(100001, 'QS8291083', 50, '2020-04-24'),
(100002, 'QS8291085', 200, '2020-04-25'),
(100003, 'QS8291085', 13, '2020-04-25'),
(100004, 'QT3846673', 75, '2020-04-30'),
(100005, 'Q8291083', 50, '2020-06-30');

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE `item` (
  `order_item_id` int(255) NOT NULL,
  `item_type` varchar(1000) NOT NULL,
  `item_name` varchar(1000) NOT NULL,
  `unit_price` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`order_item_id`, `item_type`, `item_name`, `unit_price`) VALUES
(1, 'Furniture', 'Wooden Table', 850),
(2, 'Luxury', 'Animal Watch', 1100),
(3, 'Furniture', 'Chair', 600),
(4, 'Drink', 'Cocoa cola, 12pcs/pack', 50),
(5, 'Fresh_fruit', 'Japan Apple, 5pcs/pack', 15),
(6, 'Book', 'Three little pigs', 150);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_item_no` int(255) NOT NULL,
  `order_no` longtext NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `order_item_id` int(255) NOT NULL,
  `quantity` int(255) NOT NULL,
  `price` int(255) NOT NULL,
  `tracking_no` longtext,
  `weight` int(255) DEFAULT NULL,
  `delivery_price` int(255) DEFAULT NULL,
  `estimated_delivery_date` date DEFAULT NULL,
  `customer_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_item_no`, `order_no`, `date`, `order_item_id`, `quantity`, `price`, `tracking_no`, `weight`, `delivery_price`, `estimated_delivery_date`, `customer_id`) VALUES
(100001, 'T0000001', '2020-04-20 15:36:00', 5, 4, 60, 'QS8291083', 2, 30, '2021-02-15', 152938),
(100002, 'T0000002', '2020-04-21 23:46:23', 3, 3, 1800, 'QS8291085', 8, 200, '2020-04-25', 154321),
(100003, 'T0000002', '2020-04-21 23:46:23', 2, 1, 1100, 'QS8291085', 1, 13, '2020-04-25', 154321),
(100004, 'T0000003', '2020-04-25 13:46:11', 4, 10, 500, 'QT3846673', 3, 75, '2020-04-30', 169003),
(100005, 'T0000004', '2020-05-01 16:46:32', 1, 1, 850, 'Q8291083', 2, 50, '2020-06-30', 120938);

-- --------------------------------------------------------

--
-- Table structure for table `order_form`
--

CREATE TABLE `order_form` (
  `order_item_no` int(255) NOT NULL,
  `Order_No` varchar(255) NOT NULL,
  `Date` date NOT NULL,
  `Customer_ID` int(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Type` varchar(255) NOT NULL,
  `Item_Name` varchar(255) NOT NULL,
  `Price` int(255) NOT NULL,
  `Quantity` int(255) NOT NULL,
  `Weight` int(255) NOT NULL,
  `Phone_Number` int(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_form`
--

INSERT INTO `order_form` (`order_item_no`, `Order_No`, `Date`, `Customer_ID`, `Name`, `Type`, `Item_Name`, `Price`, `Quantity`, `Weight`, `Phone_Number`, `Email`, `Address`) VALUES
(100001, 'T0000001', '2020-04-20', 152938, 'Ashley Lam', 'Fresh_fruit', 'Japan Apple, 5pcs/pack', 60, 4, 2, 98765432, 'ashleylam@gmail.com', 'Rooms 1318-20 13 / F Hollywood Plaza 610 Nathan Road Mongkok'),
(100002, 'T0000002', '2020-04-21', 154321, 'Jerry Liu', 'Furniture', 'Chair', 1800, 3, 8, 64859637, 'jerryliu@gmail.com', 'Flat 301 3 / F. The Sun Lippo Plaza 28 Canton Road Tsim sha tsui Kowloon'),
(100003, 'T0000002', '2020-04-21', 154321, 'Jerry Liu', 'luxury', 'animal Watch', 1100, 1, 1, 64859637, 'jerryliu@gmail.com', 'Flat 301 3 / F. The Sun Lippo Plaza 28 Canton Road Tsim sha tsui Kowloon'),
(100004, 'T0000003', '2020-04-25', 169003, 'Bonnie Yiu', 'Drink', 'Cocoa cola, 12pcs/pack', 500, 10, 3, 63015374, 'bonnieyiu@gmail.com', '803 South China Ind. Building 1 Chun Pin Street Kwai Chung'),
(100005, 'T0000004', '2020-05-01', 112392, 'Queenie Wong', 'Furniture', 'Wooden Table', 850, 1, 8, 90899988, 'queeniewong@gmail.com', '202-5 International Trade Center11-19 Sha Tsui Rd Nt');

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
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `delivery_form`
--
ALTER TABLE `delivery_form`
  ADD PRIMARY KEY (`order_item_no`);

--
-- Indexes for table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`order_item_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_item_no`);

--
-- Indexes for table `order_form`
--
ALTER TABLE `order_form`
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
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customer_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=169004;
--
-- AUTO_INCREMENT for table `delivery_form`
--
ALTER TABLE `delivery_form`
  MODIFY `order_item_no` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100006;
--
-- AUTO_INCREMENT for table `item`
--
ALTER TABLE `item`
  MODIFY `order_item_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_item_no` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100006;
--
-- AUTO_INCREMENT for table `order_form`
--
ALTER TABLE `order_form`
  MODIFY `order_item_no` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100006;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

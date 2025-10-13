-- schema.sql
-- Shopping Assistant Database Schema
CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

-- Products table for storing e-commerce items
CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  category VARCHAR(100) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  stock INT DEFAULT 0,
  description TEXT,
  brand VARCHAR(100),
  rating DECIMAL(2,1) DEFAULT 0.0,
  image_url VARCHAR(500),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

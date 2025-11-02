-- =========================================
-- Shopping Assistant + Vendor Database Schema
-- =========================================

CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

-- =====================
-- PRODUCTS TABLE
-- =====================
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

-- =====================
-- VENDORS TABLE
-- (used for event services and 3NF demonstration)
-- =====================
CREATE TABLE IF NOT EXISTS vendors (
  vendor_id INT AUTO_INCREMENT PRIMARY KEY,
  vendor_name VARCHAR(100) NOT NULL,
  service_type VARCHAR(100) NOT NULL,   -- e.g., catering, photography, DJ
  service_price DECIMAL(10,2),
  vendor_pincode VARCHAR(10),
  contact_number VARCHAR(15),
  email VARCHAR(100),
  rating DECIMAL(2,1) DEFAULT 0.0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================
-- LOCATION TABLE
-- (separate to remove transitive dependency for 3NF proof)
-- =====================
CREATE TABLE IF NOT EXISTS location (
  vendor_pincode VARCHAR(10) PRIMARY KEY,
  vendor_city VARCHAR(100) NOT NULL
);

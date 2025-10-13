-- seed.sql
-- Sample data for Shopping Assistant
USE student_db;

-- Insert sample products with enhanced information
INSERT INTO products (name, category, price, stock, description, brand, rating) VALUES
-- Mobile Phones
('Redmi Note 12', 'Mobile', 12999.00, 10, '6.67 inch AMOLED display, 128GB storage, 48MP camera', 'Redmi', 4.2),
('Samsung Galaxy A14', 'Mobile', 15999.00, 7, '48MP triple camera, 64GB storage, 5000mAh battery', 'Samsung', 4.0),
('Realme Narzo 50', 'Mobile', 11999.00, 5, 'MediaTek Helio G96, 6GB RAM, good battery life', 'Realme', 4.1),
('iPhone 13', 'Mobile', 59999.00, 3, 'A15 Bionic chip, 128GB, dual camera system', 'Apple', 4.6),
('OnePlus Nord CE 3', 'Mobile', 26999.00, 8, '6.7 inch display, Snapdragon 782G, 8GB RAM', 'OnePlus', 4.3),

-- Laptops
('HP 15 Laptop', 'Laptop', 34999.00, 5, 'Intel i3-1215U, 8GB RAM, 512GB SSD, Windows 11', 'HP', 4.0),
('Lenovo Ideapad 3', 'Laptop', 37999.00, 3, 'AMD Ryzen 5, 8GB RAM, 512GB SSD', 'Lenovo', 4.2),
('Dell Inspiron 15', 'Laptop', 42999.00, 4, 'Intel i5, 8GB RAM, 1TB HDD, dedicated graphics', 'Dell', 4.1),
('MacBook Air M1', 'Laptop', 89999.00, 2, 'Apple M1 chip, 8GB RAM, 256GB SSD, 13.3 inch', 'Apple', 4.7),

-- Audio Devices
('Boat Rockerz 450', 'Headphones', 1999.00, 20, 'Wireless over-ear headphones, 40mm drivers, 15hr battery', 'Boat', 4.1),
('Noise Buds VS102', 'Headphones', 1499.00, 35, 'In-ear TWS earbuds, 24hr playtime, IPX4', 'Noise', 3.9),
('Sony WH-CH720N', 'Headphones', 8999.00, 8, 'Noise cancelling, 35hr battery, V1 processor', 'Sony', 4.4),
('JBL Tune 510BT', 'Headphones', 2999.00, 15, 'Wireless on-ear headphones, JBL Pure Bass', 'JBL', 4.2),

-- Electronics
('Sony Bravia 32 inch', 'TV', 24999.00, 3, '32 inch HD Ready Smart Android TV, X-Reality PRO', 'Sony', 4.3),
('Samsung 43 inch 4K', 'TV', 34999.00, 2, '43 inch Ultra HD Smart LED TV, HDR10+', 'Samsung', 4.2),
('Mi Smart Band 7', 'Wearable', 1999.00, 25, 'Fitness tracker, 1.62 inch display, 14 days battery', 'Xiaomi', 4.1),
('Apple Watch Series 8', 'Wearable', 41999.00, 5, 'GPS, 45mm, fitness tracking, ECG app', 'Apple', 4.5),

-- Footwear
('Puma Running Shoes', 'Shoes', 2999.00, 12, 'Men sports shoes, comfortable cushioning', 'Puma', 4.0),
('Nike Air Max', 'Shoes', 7999.00, 8, 'Premium running shoes, Air Max technology', 'Nike', 4.4),
('Adidas Ultraboost', 'Shoes', 12999.00, 6, 'Energy return running shoes, Boost midsole', 'Adidas', 4.5);

-- seed.sql
USE shopping_db;

INSERT INTO products (name, category, price, stock, description) VALUES
('Redmi Note 12', 'Mobile', 12999.00, 10, '6.67 inch AMOLED, 128GB storage'),
('Samsung Galaxy A14', 'Mobile', 15999.00, 7, '48MP camera, 64GB'),
('Realme Narzo 50', 'Mobile', 11999.00, 5, 'Good battery life'),
('HP 15 Laptop', 'Laptop', 34999.00, 5, 'Intel i3, 8GB RAM, 512GB SSD'),
('Lenovo Ideapad 3', 'Laptop', 37999.00, 3, 'AMD Ryzen 5, 8GB RAM'),
('Boat Rockerz Headphones', 'Headphones', 1999.00, 20, 'Wireless over-ear, bassy'),
('Noise Earbuds', 'Headphones', 1499.00, 35, 'In-ear Bluetooth earbuds'),
('Sony Bravia 32"', 'TV', 24999.00, 3, '32 inch HD TV'),
('Mi Smart Band', 'Wearable', 1999.00, 25, 'Fitness tracker'),
('Puma Running Shoes', 'Shoes', 2999.00, 12, 'Men sports shoes');

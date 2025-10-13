# setup_enhanced_database.py
# Enhanced database setup with comprehensive product catalog

import mysql.connector
from mysql.connector import Error
import getpass

def setup_enhanced_database():
    print("🚀 Shopping Assistant - Enhanced Database Setup")
    print("=" * 60)
    
    # Get credentials
    host = input("MySQL Host (default: localhost): ") or "localhost"
    port = input("MySQL Port (default: 3306): ") or "3306"
    user = input("MySQL Username (default: root): ") or "root"
    password = getpass.getpass("MySQL Password: ")
    
    try:
        port = int(port)
    except ValueError:
        print("❌ Invalid port number")
        return
    
    print(f"\n🔄 Connecting to MySQL server as {user}@{host}:{port}...")
    
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print("✅ Connected to MySQL server!")
            
            # Create/use database
            cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
            cursor.execute("USE student_db")
            print("✅ Using student_db database")
            
            # Drop existing table to recreate with new data
            print("🔄 Recreating products table...")
            cursor.execute("DROP TABLE IF EXISTS products")
            
            # Create enhanced products table
            create_table_sql = """
            CREATE TABLE products (
              id INT AUTO_INCREMENT PRIMARY KEY,
              name VARCHAR(255) NOT NULL,
              category VARCHAR(100) NOT NULL,
              price DECIMAL(10,2) NOT NULL,
              stock INT DEFAULT 0,
              description TEXT,
              brand VARCHAR(100),
              rating DECIMAL(2,1) DEFAULT 0.0,
              image_url VARCHAR(500),
              specifications JSON,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
              INDEX idx_category (category),
              INDEX idx_price (price),
              INDEX idx_brand (brand)
            )
            """
            cursor.execute(create_table_sql)
            print("✅ Products table created successfully!")
            
            # Insert comprehensive product data
            print("🔄 Inserting comprehensive product catalog...")
            
            # Mobile phones (25 products)
            mobile_products = [
                ('iPhone 15 Pro', 'Mobile', 134999.00, 8, 'A17 Pro chip, 128GB, titanium design, 48MP camera', 'Apple', 4.8, 'https://via.placeholder.com/300x200?text=iPhone+15+Pro'),
                ('iPhone 15', 'Mobile', 79999.00, 12, 'A16 Bionic chip, 128GB, dual camera system', 'Apple', 4.6, 'https://via.placeholder.com/300x200?text=iPhone+15'),
                ('iPhone 14', 'Mobile', 69999.00, 15, 'A15 Bionic chip, 128GB storage, 12MP camera', 'Apple', 4.5, 'https://via.placeholder.com/300x200?text=iPhone+14'),
                ('Samsung Galaxy S24 Ultra', 'Mobile', 129999.00, 6, 'Snapdragon 8 Gen 3, 256GB, S Pen, 200MP camera', 'Samsung', 4.7, 'https://via.placeholder.com/300x200?text=Galaxy+S24+Ultra'),
                ('Samsung Galaxy S24', 'Mobile', 79999.00, 10, 'Exynos 2400, 128GB, AI camera, 6.2 inch display', 'Samsung', 4.4, 'https://via.placeholder.com/300x200?text=Galaxy+S24'),
                ('Samsung Galaxy A54', 'Mobile', 38999.00, 20, '50MP triple camera, 128GB storage, 5000mAh battery', 'Samsung', 4.2, 'https://via.placeholder.com/300x200?text=Galaxy+A54'),
                ('Samsung Galaxy A34', 'Mobile', 30999.00, 25, '48MP camera, 128GB storage, Super AMOLED display', 'Samsung', 4.1, 'https://via.placeholder.com/300x200?text=Galaxy+A34'),
                ('Samsung Galaxy M14', 'Mobile', 14999.00, 30, '50MP triple camera, 4GB RAM, 6000mAh battery', 'Samsung', 3.9, 'https://via.placeholder.com/300x200?text=Galaxy+M14'),
                ('OnePlus 12', 'Mobile', 64999.00, 8, 'Snapdragon 8 Gen 3, 256GB, 50MP Hasselblad camera', 'OnePlus', 4.6, 'https://via.placeholder.com/300x200?text=OnePlus+12'),
                ('OnePlus 11R', 'Mobile', 39999.00, 15, 'Snapdragon 8+ Gen 1, 128GB, 50MP camera', 'OnePlus', 4.3, 'https://via.placeholder.com/300x200?text=OnePlus+11R'),
                ('OnePlus Nord CE 3', 'Mobile', 26999.00, 18, 'Snapdragon 782G, 128GB, 50MP camera', 'OnePlus', 4.2, 'https://via.placeholder.com/300x200?text=OnePlus+Nord+CE3'),
                ('Xiaomi 14', 'Mobile', 69999.00, 12, 'Snapdragon 8 Gen 3, 256GB, Leica camera', 'Xiaomi', 4.5, 'https://via.placeholder.com/300x200?text=Xiaomi+14'),
                ('Redmi Note 13 Pro+', 'Mobile', 31999.00, 22, '200MP camera, 256GB, 120W fast charging', 'Redmi', 4.4, 'https://via.placeholder.com/300x200?text=Redmi+Note+13+Pro'),
                ('Redmi Note 13', 'Mobile', 17999.00, 35, '108MP camera, 128GB, AMOLED display', 'Redmi', 4.1, 'https://via.placeholder.com/300x200?text=Redmi+Note+13'),
                ('Redmi 12', 'Mobile', 10999.00, 40, '50MP AI camera, 128GB, 5000mAh battery', 'Redmi', 3.8, 'https://via.placeholder.com/300x200?text=Redmi+12'),
                ('Realme GT 3', 'Mobile', 42999.00, 12, 'Snapdragon 8+ Gen 1, 128GB, 150W charging', 'Realme', 4.3, 'https://via.placeholder.com/300x200?text=Realme+GT3'),
                ('Realme 11 Pro+', 'Mobile', 27999.00, 18, '200MP OIS camera, 256GB, curved display', 'Realme', 4.2, 'https://via.placeholder.com/300x200?text=Realme+11+Pro'),
                ('Realme Narzo 60', 'Mobile', 17999.00, 25, '64MP OIS camera, 128GB, 5000mAh battery', 'Realme', 4.0, 'https://via.placeholder.com/300x200?text=Realme+Narzo+60'),
                ('Vivo V29', 'Mobile', 32999.00, 15, '50MP selfie camera, 256GB, color changing back', 'Vivo', 4.2, 'https://via.placeholder.com/300x200?text=Vivo+V29'),
                ('Vivo Y36', 'Mobile', 19999.00, 28, '50MP camera, 128GB, 5000mAh battery', 'Vivo', 3.9, 'https://via.placeholder.com/300x200?text=Vivo+Y36'),
                ('Oppo Reno 10', 'Mobile', 32999.00, 14, '64MP periscope camera, 256GB, 67W charging', 'Oppo', 4.1, 'https://via.placeholder.com/300x200?text=Oppo+Reno+10'),
                ('Oppo A58', 'Mobile', 15999.00, 32, '50MP AI camera, 128GB, 5000mAh battery', 'Oppo', 3.8, 'https://via.placeholder.com/300x200?text=Oppo+A58'),
                ('Nothing Phone 2', 'Mobile', 44999.00, 10, 'Snapdragon 8+ Gen 1, 256GB, Glyph interface', 'Nothing', 4.4, 'https://via.placeholder.com/300x200?text=Nothing+Phone+2'),
                ('Motorola Edge 40', 'Mobile', 25999.00, 16, 'MediaTek 8020, 128GB, 68W charging', 'Motorola', 4.0, 'https://via.placeholder.com/300x200?text=Motorola+Edge+40'),
                ('Google Pixel 8', 'Mobile', 75999.00, 8, 'Google Tensor G3, 128GB, AI photography', 'Google', 4.5, 'https://via.placeholder.com/300x200?text=Google+Pixel+8')
            ]
            
            # Laptops (25 products)
            laptop_products = [
                ('MacBook Pro 16" M3', 'Laptop', 249999.00, 3, 'Apple M3 Pro chip, 18GB RAM, 512GB SSD, 16.2" display', 'Apple', 4.8, 'https://via.placeholder.com/300x200?text=MacBook+Pro+16'),
                ('MacBook Air 15" M2', 'Laptop', 134999.00, 5, 'Apple M2 chip, 8GB RAM, 256GB SSD, 15.3" display', 'Apple', 4.7, 'https://via.placeholder.com/300x200?text=MacBook+Air+15'),
                ('MacBook Air 13" M2', 'Laptop', 114999.00, 8, 'Apple M2 chip, 8GB RAM, 256GB SSD, 13.6" display', 'Apple', 4.6, 'https://via.placeholder.com/300x200?text=MacBook+Air+13'),
                ('Dell XPS 13', 'Laptop', 89999.00, 6, 'Intel i7-1360P, 16GB RAM, 512GB SSD, 13.4" OLED', 'Dell', 4.5, 'https://via.placeholder.com/300x200?text=Dell+XPS+13'),
                ('Dell XPS 15', 'Laptop', 159999.00, 4, 'Intel i7-13700H, 32GB RAM, 1TB SSD, RTX 4060', 'Dell', 4.6, 'https://via.placeholder.com/300x200?text=Dell+XPS+15'),
                ('Dell Inspiron 15 3000', 'Laptop', 42999.00, 12, 'Intel i5-1235U, 8GB RAM, 512GB SSD, 15.6" FHD', 'Dell', 4.0, 'https://via.placeholder.com/300x200?text=Dell+Inspiron+15'),
                ('Dell Inspiron 14', 'Laptop', 54999.00, 10, 'Intel i7-1255U, 16GB RAM, 512GB SSD, 14" FHD+', 'Dell', 4.2, 'https://via.placeholder.com/300x200?text=Dell+Inspiron+14'),
                ('HP Spectre x360', 'Laptop', 124999.00, 5, 'Intel i7-1355U, 16GB RAM, 1TB SSD, 2-in-1 design', 'HP', 4.4, 'https://via.placeholder.com/300x200?text=HP+Spectre+x360'),
                ('HP Pavilion 15', 'Laptop', 54999.00, 15, 'Intel i5-1235U, 8GB RAM, 512GB SSD, 15.6" FHD', 'HP', 4.1, 'https://via.placeholder.com/300x200?text=HP+Pavilion+15'),
                ('HP Envy x360', 'Laptop', 74999.00, 8, 'AMD Ryzen 5 7530U, 16GB RAM, 512GB SSD, 2-in-1', 'HP', 4.3, 'https://via.placeholder.com/300x200?text=HP+Envy+x360'),
                ('HP 14s', 'Laptop', 39999.00, 20, 'Intel i3-1215U, 8GB RAM, 512GB SSD, 14" FHD', 'HP', 3.9, 'https://via.placeholder.com/300x200?text=HP+14s'),
                ('Lenovo ThinkPad X1 Carbon', 'Laptop', 149999.00, 4, 'Intel i7-1365U, 32GB RAM, 1TB SSD, 14" 2.8K', 'Lenovo', 4.7, 'https://via.placeholder.com/300x200?text=ThinkPad+X1+Carbon'),
                ('Lenovo IdeaPad Slim 5', 'Laptop', 59999.00, 12, 'AMD Ryzen 5 7530U, 16GB RAM, 512GB SSD, 14" FHD', 'Lenovo', 4.2, 'https://via.placeholder.com/300x200?text=IdeaPad+Slim+5'),
                ('Lenovo IdeaPad 3', 'Laptop', 42999.00, 18, 'Intel i5-12450H, 8GB RAM, 512GB SSD, 15.6" FHD', 'Lenovo', 4.0, 'https://via.placeholder.com/300x200?text=IdeaPad+3'),
                ('Lenovo LOQ 15', 'Laptop', 69999.00, 8, 'Intel i5-12450HX, 16GB RAM, 512GB SSD, RTX 4050', 'Lenovo', 4.3, 'https://via.placeholder.com/300x200?text=Lenovo+LOQ+15'),
                ('ASUS ZenBook 14', 'Laptop', 84999.00, 7, 'Intel i7-1355U, 16GB RAM, 512GB SSD, 14" OLED', 'ASUS', 4.4, 'https://via.placeholder.com/300x200?text=ZenBook+14'),
                ('ASUS VivoBook 15', 'Laptop', 49999.00, 15, 'Intel i5-1235U, 8GB RAM, 512GB SSD, 15.6" FHD', 'ASUS', 4.1, 'https://via.placeholder.com/300x200?text=VivoBook+15'),
                ('ASUS ROG Strix G15', 'Laptop', 89999.00, 6, 'AMD Ryzen 7 6800H, 16GB RAM, 512GB SSD, RTX 4060', 'ASUS', 4.5, 'https://via.placeholder.com/300x200?text=ROG+Strix+G15'),
                ('Acer Swift 3', 'Laptop', 54999.00, 12, 'Intel i5-1235U, 8GB RAM, 512GB SSD, 14" FHD', 'Acer', 4.0, 'https://via.placeholder.com/300x200?text=Acer+Swift+3'),
                ('Acer Aspire 5', 'Laptop', 44999.00, 16, 'Intel i3-1215U, 8GB RAM, 512GB SSD, 15.6" FHD', 'Acer', 3.8, 'https://via.placeholder.com/300x200?text=Acer+Aspire+5'),
                ('Acer Nitro 5', 'Laptop', 64999.00, 9, 'Intel i5-12500H, 16GB RAM, 512GB SSD, RTX 4050', 'Acer', 4.2, 'https://via.placeholder.com/300x200?text=Acer+Nitro+5'),
                ('Microsoft Surface Laptop 5', 'Laptop', 109999.00, 5, 'Intel i7-1255U, 16GB RAM, 512GB SSD, 13.5" touch', 'Microsoft', 4.4, 'https://via.placeholder.com/300x200?text=Surface+Laptop+5'),
                ('MSI Modern 15', 'Laptop', 52999.00, 10, 'Intel i5-1235U, 8GB RAM, 512GB SSD, 15.6" FHD', 'MSI', 4.1, 'https://via.placeholder.com/300x200?text=MSI+Modern+15'),
                ('Xiaomi RedmiBook 15', 'Laptop', 39999.00, 14, 'Intel i3-1115G4, 8GB RAM, 256GB SSD, 15.6" FHD', 'Xiaomi', 3.9, 'https://via.placeholder.com/300x200?text=RedmiBook+15'),
                ('Honor MagicBook X14', 'Laptop', 36999.00, 18, 'Intel i3-10110U, 8GB RAM, 256GB SSD, 14" FHD', 'Honor', 3.8, 'https://via.placeholder.com/300x200?text=MagicBook+X14')
            ]
            
            # Headphones (25 products)
            headphone_products = [
                ('Apple AirPods Pro 2', 'Headphones', 24999.00, 25, 'Active noise cancellation, spatial audio, USB-C', 'Apple', 4.7, 'https://via.placeholder.com/300x200?text=AirPods+Pro+2'),
                ('Apple AirPods 3', 'Headphones', 18999.00, 30, 'Spatial audio, 6hr battery, sweat resistant', 'Apple', 4.5, 'https://via.placeholder.com/300x200?text=AirPods+3'),
                ('Apple AirPods Max', 'Headphones', 59999.00, 8, 'Over-ear, active noise cancellation, premium build', 'Apple', 4.6, 'https://via.placeholder.com/300x200?text=AirPods+Max'),
                ('Sony WH-1000XM5', 'Headphones', 29999.00, 15, 'Industry-leading noise cancellation, 30hr battery', 'Sony', 4.8, 'https://via.placeholder.com/300x200?text=Sony+WH-1000XM5'),
                ('Sony WH-CH720N', 'Headphones', 8999.00, 20, 'Noise cancellation, 35hr battery, V1 processor', 'Sony', 4.4, 'https://via.placeholder.com/300x200?text=Sony+WH-CH720N'),
                ('Sony WF-1000XM4', 'Headphones', 19999.00, 18, 'True wireless, LDAC, 8hr battery + case', 'Sony', 4.6, 'https://via.placeholder.com/300x200?text=Sony+WF-1000XM4'),
                ('Bose QuietComfort 45', 'Headphones', 32999.00, 12, 'World-class noise cancellation, 24hr battery', 'Bose', 4.7, 'https://via.placeholder.com/300x200?text=Bose+QC45'),
                ('Bose QuietComfort Earbuds', 'Headphones', 26999.00, 14, 'True wireless, 11 levels noise cancellation', 'Bose', 4.5, 'https://via.placeholder.com/300x200?text=Bose+QC+Earbuds'),
                ('JBL Tune 760NC', 'Headphones', 7999.00, 25, 'Active noise cancelling, 50hr battery, JBL Pure Bass', 'JBL', 4.2, 'https://via.placeholder.com/300x200?text=JBL+Tune+760NC'),
                ('JBL Live 660NC', 'Headphones', 9999.00, 22, 'Adaptive noise cancelling, 50hr battery, multi-point', 'JBL', 4.3, 'https://via.placeholder.com/300x200?text=JBL+Live+660NC'),
                ('JBL Quantum 400', 'Headphones', 6999.00, 28, 'Gaming headset, QuantumSOUND signature, Discord certified', 'JBL', 4.1, 'https://via.placeholder.com/300x200?text=JBL+Quantum+400'),
                ('Sennheiser HD 450BT', 'Headphones', 12999.00, 16, 'Active noise cancellation, 30hr battery, aptX', 'Sennheiser', 4.4, 'https://via.placeholder.com/300x200?text=Sennheiser+HD450BT'),
                ('Audio-Technica ATH-M50xBT2', 'Headphones', 19999.00, 12, 'Professional monitor, 50hr battery, multipoint', 'Audio-Technica', 4.6, 'https://via.placeholder.com/300x200?text=ATH-M50xBT2'),
                ('Boat Rockerz 550', 'Headphones', 2999.00, 35, '20hr battery, 50mm drivers, physical noise isolation', 'Boat', 4.0, 'https://via.placeholder.com/300x200?text=Boat+Rockerz+550'),
                ('Boat Airdopes 800', 'Headphones', 4999.00, 40, 'True wireless, ANC, 40hr battery with case', 'Boat', 4.1, 'https://via.placeholder.com/300x200?text=Boat+Airdopes+800'),
                ('Boat Immortal 400', 'Headphones', 2499.00, 45, 'Gaming earbuds, low latency, RGB lights', 'Boat', 3.9, 'https://via.placeholder.com/300x200?text=Boat+Immortal+400'),
                ('Noise Air Buds Pro', 'Headphones', 4999.00, 30, 'Hybrid ANC, 45hr playtime, quad mics', 'Noise', 4.0, 'https://via.placeholder.com/300x200?text=Noise+Air+Buds+Pro'),
                ('Noise Two', 'Headphones', 2999.00, 35, 'True wireless, 50hr playtime, 11mm drivers', 'Noise', 3.8, 'https://via.placeholder.com/300x200?text=Noise+Two'),
                ('OnePlus Buds Pro 2', 'Headphones', 11999.00, 18, 'Adaptive ANC, spatial audio, 39hr battery', 'OnePlus', 4.3, 'https://via.placeholder.com/300x200?text=OnePlus+Buds+Pro+2'),
                ('Realme Buds Air 5', 'Headphones', 3999.00, 32, 'Active noise cancellation, 28hr battery', 'Realme', 4.0, 'https://via.placeholder.com/300x200?text=Realme+Buds+Air+5'),
                ('Xiaomi Buds 4', 'Headphones', 8999.00, 22, 'Adaptive ANC, Hi-Res audio, 36hr battery', 'Xiaomi', 4.2, 'https://via.placeholder.com/300x200?text=Xiaomi+Buds+4'),
                ('Samsung Galaxy Buds2 Pro', 'Headphones', 17999.00, 16, 'Intelligent ANC, 360 audio, 8hr battery + case', 'Samsung', 4.4, 'https://via.placeholder.com/300x200?text=Galaxy+Buds2+Pro'),
                ('Nothing Ear (2)', 'Headphones', 8999.00, 24, 'Transparent design, Hi-Res audio, 36hr battery', 'Nothing', 4.2, 'https://via.placeholder.com/300x200?text=Nothing+Ear+2'),
                ('Skullcandy Crusher Evo', 'Headphones', 14999.00, 14, 'Sensory bass, 40hr battery, custom sound profiles', 'Skullcandy', 4.1, 'https://via.placeholder.com/300x200?text=Skullcandy+Crusher+Evo'),
                ('Marshall Major IV', 'Headphones', 12999.00, 18, '80+ hour battery, iconic design, collapsible', 'Marshall', 4.3, 'https://via.placeholder.com/300x200?text=Marshall+Major+IV')
            ]
            
            # TVs (25 products)  
            tv_products = [
                ('Samsung 65" Neo QLED QN800C', 'TV', 349999.00, 3, '8K Neo QLED, Neural Quantum Processor, 65 inch', 'Samsung', 4.8, 'https://via.placeholder.com/300x200?text=Samsung+Neo+QLED+65'),
                ('Samsung 55" QLED Q80C', 'TV', 119999.00, 5, '4K QLED, Quantum HDR, Direct Full Array, 55 inch', 'Samsung', 4.6, 'https://via.placeholder.com/300x200?text=Samsung+QLED+55'),
                ('Samsung 43" Crystal 4K AU8000', 'TV', 42999.00, 8, '4K Crystal processor, HDR10+, Smart TV, 43 inch', 'Samsung', 4.3, 'https://via.placeholder.com/300x200?text=Samsung+Crystal+43'),
                ('Samsung 32" HD T4300', 'TV', 18999.00, 12, 'HD Smart TV, Tizen OS, screen mirroring, 32 inch', 'Samsung', 4.1, 'https://via.placeholder.com/300x200?text=Samsung+HD+32'),
                ('LG 65" OLED C3', 'TV', 199999.00, 4, 'Self-lit OLED, α9 Gen6 processor, Dolby Vision, 65 inch', 'LG', 4.9, 'https://via.placeholder.com/300x200?text=LG+OLED+C3+65'),
                ('LG 55" QNED 86 Series', 'TV', 89999.00, 6, 'Quantum Dot NanoCell, α7 Gen5 processor, 55 inch', 'LG', 4.5, 'https://via.placeholder.com/300x200?text=LG+QNED+55'),
                ('LG 43" UltraHD UR7500', 'TV', 39999.00, 10, '4K UltraHD, webOS smart TV, AI ThinQ, 43 inch', 'LG', 4.2, 'https://via.placeholder.com/300x200?text=LG+UltraHD+43'),
                ('LG 32" HD LM563B', 'TV', 16999.00, 15, 'HD Smart TV, webOS, virtual surround sound, 32 inch', 'LG', 4.0, 'https://via.placeholder.com/300x200?text=LG+HD+32'),
                ('Sony 65" BRAVIA XR A80L', 'TV', 189999.00, 3, 'OLED 4K, Cognitive Processor XR, XR OLED Contrast Pro', 'Sony', 4.8, 'https://via.placeholder.com/300x200?text=Sony+BRAVIA+OLED+65'),
                ('Sony 55" BRAVIA X85L', 'TV', 79999.00, 7, '4K LED, Cognitive Processor XR, TRILUMINOS Pro', 'Sony', 4.4, 'https://via.placeholder.com/300x200?text=Sony+BRAVIA+X85L'),
                ('Sony 43" BRAVIA X74L', 'TV', 54999.00, 9, '4K LED, 4K HDR processor X1, Google TV', 'Sony', 4.3, 'https://via.placeholder.com/300x200?text=Sony+BRAVIA+X74L'),
                ('Sony 32" BRAVIA W830K', 'TV', 32999.00, 12, 'Full HD, HDR, Google TV, X-Reality PRO', 'Sony', 4.1, 'https://via.placeholder.com/300x200?text=Sony+BRAVIA+W830K'),
                ('TCL 65" C735 QLED', 'TV', 74999.00, 6, '4K QLED, Quantum Dot technology, Dolby Vision IQ', 'TCL', 4.3, 'https://via.placeholder.com/300x200?text=TCL+C735+65'),
                ('TCL 55" P635 4K', 'TV', 39999.00, 11, '4K UHD, HDR10, Dolby Audio, Google TV', 'TCL', 4.1, 'https://via.placeholder.com/300x200?text=TCL+P635+55'),
                ('TCL 43" S5400A', 'TV', 24999.00, 14, 'Full HD Smart TV, Android TV, Dolby Audio', 'TCL', 3.9, 'https://via.placeholder.com/300x200?text=TCL+S5400A+43'),
                ('Mi TV 5X 65"', 'TV', 54999.00, 8, '4K Ultra HD, Android TV 11, Dolby Vision', 'Xiaomi', 4.2, 'https://via.placeholder.com/300x200?text=Mi+TV+5X+65'),
                ('Mi TV 4A 55"', 'TV', 32999.00, 12, '4K HDR, Android TV, 20W speakers, PatchWall', 'Xiaomi', 4.0, 'https://via.placeholder.com/300x200?text=Mi+TV+4A+55'),
                ('Mi TV 4A 43"', 'TV', 24999.00, 16, 'Full HD, Android TV, Chromecast built-in', 'Xiaomi', 3.8, 'https://via.placeholder.com/300x200?text=Mi+TV+4A+43'),
                ('Realme Smart TV X 55"', 'TV', 31999.00, 10, '4K UltraHD, Android TV, Chroma Boost Picture Engine', 'Realme', 4.0, 'https://via.placeholder.com/300x200?text=Realme+TV+X+55'),
                ('OnePlus TV 65" U1S', 'TV', 52999.00, 7, '4K LED, Android TV 11, Gamma Engine, 30W speakers', 'OnePlus', 4.2, 'https://via.placeholder.com/300x200?text=OnePlus+TV+U1S'),
                ('Hisense 55" A71F', 'TV', 34999.00, 9, '4K UltraHD, VIDAA U5, Dolby Vision, DTS Virtual X', 'Hisense', 4.0, 'https://via.placeholder.com/300x200?text=Hisense+A71F+55'),
                ('VU 65" Premium Android TV', 'TV', 44999.00, 6, '4K UltraHD, Android TV 9, Cricket Mode', 'VU', 3.9, 'https://via.placeholder.com/300x200?text=VU+Premium+65'),
                ('Kodak 50" 4K LED TV', 'TV', 27999.00, 11, '4K UltraHD, Android TV, 30W JBL speakers', 'Kodak', 3.8, 'https://via.placeholder.com/300x200?text=Kodak+4K+50'),
                ('Panasonic 43" 4K LED', 'TV', 36999.00, 8, '4K UltraHD, My Home Screen 6.0, Hexa Chroma Drive', 'Panasonic', 4.1, 'https://via.placeholder.com/300x200?text=Panasonic+4K+43'),
                ('Toshiba 32" HD Smart TV', 'TV', 14999.00, 18, 'HD Ready, VIDAA Lite, Dolby Audio, Bezel-less', 'Toshiba', 3.7, 'https://via.placeholder.com/300x200?text=Toshiba+HD+32')
            ]
            
            # Wearables (25 products)
            wearable_products = [
                ('Apple Watch Series 9 45mm', 'Wearable', 45999.00, 12, 'S9 SiP, Always-On Retina display, Double Tap gesture', 'Apple', 4.8, 'https://via.placeholder.com/300x200?text=Apple+Watch+Series+9'),
                ('Apple Watch SE 44mm', 'Wearable', 29999.00, 18, 'S8 SiP, Retina display, Crash Detection, swimproof', 'Apple', 4.6, 'https://via.placeholder.com/300x200?text=Apple+Watch+SE'),
                ('Apple Watch Ultra 2', 'Wearable', 89999.00, 6, 'S9 SiP, 49mm titanium case, Action Button, 36hr battery', 'Apple', 4.9, 'https://via.placeholder.com/300x200?text=Apple+Watch+Ultra+2'),
                ('Samsung Galaxy Watch6 44mm', 'Wearable', 32999.00, 15, 'Exynos W930, 1.5" Super AMOLED, body composition', 'Samsung', 4.5, 'https://via.placeholder.com/300x200?text=Galaxy+Watch6'),
                ('Samsung Galaxy Watch6 Classic', 'Wearable', 38999.00, 12, 'Rotating bezel, 47mm, sapphire crystal, premium build', 'Samsung', 4.6, 'https://via.placeholder.com/300x200?text=Galaxy+Watch6+Classic'),
                ('Samsung Galaxy Watch5 Pro', 'Wearable', 42999.00, 10, '45mm titanium, sapphire crystal, 590mAh battery', 'Samsung', 4.4, 'https://via.placeholder.com/300x200?text=Galaxy+Watch5+Pro'),
                ('Garmin Forerunner 265', 'Wearable', 34999.00, 8, 'AMOLED display, multi-band GPS, training readiness', 'Garmin', 4.7, 'https://via.placeholder.com/300x200?text=Garmin+Forerunner+265'),
                ('Garmin Venu 3', 'Wearable', 44999.00, 6, '1.4" AMOLED, wheelchair mode, 14-day battery life', 'Garmin', 4.6, 'https://via.placeholder.com/300x200?text=Garmin+Venu+3'),
                ('Fitbit Charge 6', 'Wearable', 15999.00, 25, 'Built-in GPS, Google apps, heart rate zones', 'Fitbit', 4.3, 'https://via.placeholder.com/300x200?text=Fitbit+Charge+6'),
                ('Fitbit Versa 4', 'Wearable', 19999.00, 20, '6+ day battery, built-in GPS, 40+ exercise modes', 'Fitbit', 4.2, 'https://via.placeholder.com/300x200?text=Fitbit+Versa+4'),
                ('Amazfit GTR 4', 'Wearable', 16999.00, 22, '1.43" AMOLED, dual-band GPS, 150+ sports modes', 'Amazfit', 4.3, 'https://via.placeholder.com/300x200?text=Amazfit+GTR+4'),
                ('Amazfit Bip 5', 'Wearable', 6999.00, 30, '1.91" display, 10-day battery, 120+ sports modes', 'Amazfit', 4.1, 'https://via.placeholder.com/300x200?text=Amazfit+Bip+5'),
                ('Xiaomi Watch 2 Pro', 'Wearable', 17999.00, 18, 'Snapdragon W5+ Gen 1, Wear OS, 1.43" AMOLED', 'Xiaomi', 4.2, 'https://via.placeholder.com/300x200?text=Xiaomi+Watch+2+Pro'),
                ('Mi Smart Band 8', 'Wearable', 2999.00, 40, '1.62" AMOLED, 16-day battery, 150+ workout modes', 'Xiaomi', 4.0, 'https://via.placeholder.com/300x200?text=Mi+Smart+Band+8'),
                ('Realme Watch S2', 'Wearable', 4999.00, 35, '1.43" AMOLED, GPS, 12-day battery, IP68', 'Realme', 3.9, 'https://via.placeholder.com/300x200?text=Realme+Watch+S2'),
                ('OnePlus Watch 2', 'Wearable', 24999.00, 12, 'Snapdragon W5 Gen 1, Wear OS, 4-day battery', 'OnePlus', 4.3, 'https://via.placeholder.com/300x200?text=OnePlus+Watch+2'),
                ('Noise ColorFit Pro 4 Alpha', 'Wearable', 3999.00, 32, '1.78" AMOLED, Bluetooth calling, 7-day battery', 'Noise', 3.8, 'https://via.placeholder.com/300x200?text=Noise+ColorFit+Pro+4'),
                ('boAt Wave Call 2', 'Wearable', 2499.00, 45, '1.83" display, Bluetooth calling, 7-day battery', 'Boat', 3.7, 'https://via.placeholder.com/300x200?text=boAt+Wave+Call+2'),
                ('Fire-Boltt Phoenix Pro', 'Wearable', 1999.00, 50, '1.39" display, SpO2, heart rate, 8-day battery', 'Fire-Boltt', 3.6, 'https://via.placeholder.com/300x200?text=Fire-Boltt+Phoenix+Pro'),
                ('Titan Smart Pro', 'Wearable', 12999.00, 15, '1.96" AMOLED, premium build, health tracking', 'Titan', 4.1, 'https://via.placeholder.com/300x200?text=Titan+Smart+Pro'),
                ('Fossil Gen 6', 'Wearable', 22999.00, 10, 'Snapdragon 4100+, Wear OS, 1.28" AMOLED', 'Fossil', 4.2, 'https://via.placeholder.com/300x200?text=Fossil+Gen+6'),
                ('Suunto 9 Peak Pro', 'Wearable', 54999.00, 5, 'Titanium, sapphire crystal, 170hr GPS battery', 'Suunto', 4.6, 'https://via.placeholder.com/300x200?text=Suunto+9+Peak+Pro'),
                ('Polar Pacer Pro', 'Wearable', 29999.00, 8, 'GPS, barometric altimeter, running power, ultra-light', 'Polar', 4.4, 'https://via.placeholder.com/300x200?text=Polar+Pacer+Pro'),
                ('Huawei Watch GT 4', 'Wearable', 24999.00, 14, '1.43" AMOLED, 14-day battery, professional sports', 'Huawei', 4.3, 'https://via.placeholder.com/300x200?text=Huawei+Watch+GT+4'),
                ('Oppo Watch 3 Pro', 'Wearable', 26999.00, 11, '1.91" curved AMOLED, eSIM, ECG monitoring', 'Oppo', 4.2, 'https://via.placeholder.com/300x200?text=Oppo+Watch+3+Pro')
            ]
            
            # Shoes (25 products)
            shoe_products = [
                ('Nike Air Jordan 1 Mid', 'Shoes', 10995.00, 15, 'Classic basketball silhouette, premium leather upper', 'Nike', 4.6, 'https://via.placeholder.com/300x200?text=Nike+Air+Jordan+1'),
                ('Nike Air Max 270', 'Shoes', 12795.00, 12, 'Max Air unit, mesh upper, lifestyle comfort', 'Nike', 4.5, 'https://via.placeholder.com/300x200?text=Nike+Air+Max+270'),
                ('Nike Revolution 6', 'Shoes', 4995.00, 25, 'Lightweight foam midsole, computer-generated outsole', 'Nike', 4.2, 'https://via.placeholder.com/300x200?text=Nike+Revolution+6'),
                ('Nike Dunk Low', 'Shoes', 8695.00, 18, 'College colors, vintage basketball style, durable', 'Nike', 4.4, 'https://via.placeholder.com/300x200?text=Nike+Dunk+Low'),
                ('Nike Air Force 1', 'Shoes', 7995.00, 20, 'Iconic basketball shoe, full-length Air sole unit', 'Nike', 4.7, 'https://via.placeholder.com/300x200?text=Nike+Air+Force+1'),
                ('Adidas Ultraboost 23', 'Shoes', 17999.00, 10, 'Boost midsole, Primeknit upper, continental rubber', 'Adidas', 4.8, 'https://via.placeholder.com/300x200?text=Adidas+Ultraboost+23'),
                ('Adidas Stan Smith', 'Shoes', 7999.00, 22, 'Clean leather upper, perforated 3-stripes, minimalist', 'Adidas', 4.5, 'https://via.placeholder.com/300x200?text=Adidas+Stan+Smith'),
                ('Adidas Campus 00s', 'Shoes', 9999.00, 16, 'Suede upper, vintage basketball style, 3-stripes', 'Adidas', 4.3, 'https://via.placeholder.com/300x200?text=Adidas+Campus+00s'),
                ('Adidas Samba OG', 'Shoes', 9999.00, 14, 'Indoor soccer heritage, leather upper, gum sole', 'Adidas', 4.6, 'https://via.placeholder.com/300x200?text=Adidas+Samba+OG'),
                ('Adidas NMD_R1', 'Shoes', 13999.00, 12, 'Boost midsole, sock-like construction, modern style', 'Adidas', 4.4, 'https://via.placeholder.com/300x200?text=Adidas+NMD_R1'),
                ('Puma Suede Classic', 'Shoes', 5999.00, 24, 'Suede upper, fat laces, vintage basketball style', 'Puma', 4.3, 'https://via.placeholder.com/300x200?text=Puma+Suede+Classic'),
                ('Puma RS-X3', 'Shoes', 8999.00, 18, 'Running System technology, bold colorways, chunky sole', 'Puma', 4.2, 'https://via.placeholder.com/300x200?text=Puma+RS-X3'),
                ('Puma Cali Star', 'Shoes', 7999.00, 20, 'Platform sole, vintage tennis style, leather upper', 'Puma', 4.1, 'https://via.placeholder.com/300x200?text=Puma+Cali+Star'),
                ('Puma Future Rider', 'Shoes', 6999.00, 22, 'Federbein outsole, nylon mesh upper, retro running', 'Puma', 4.0, 'https://via.placeholder.com/300x200?text=Puma+Future+Rider'),
                ('Converse Chuck Taylor All Star', 'Shoes', 3999.00, 30, 'Canvas upper, rubber toe cap, iconic high-top', 'Converse', 4.4, 'https://via.placeholder.com/300x200?text=Converse+Chuck+Taylor'),
                ('Converse Chuck 70', 'Shoes', 6999.00, 20, 'Premium canvas, vintage details, enhanced comfort', 'Converse', 4.5, 'https://via.placeholder.com/300x200?text=Converse+Chuck+70'),
                ('Vans Old Skool', 'Shoes', 4999.00, 28, 'Suede and canvas upper, signature side stripe, waffle sole', 'Vans', 4.3, 'https://via.placeholder.com/300x200?text=Vans+Old+Skool'),
                ('Vans Authentic', 'Shoes', 3999.00, 32, 'Canvas upper, metal eyelets, signature waffle outsole', 'Vans', 4.2, 'https://via.placeholder.com/300x200?text=Vans+Authentic'),
                ('New Balance 574', 'Shoes', 7999.00, 18, 'ENCAP midsole, suede/mesh upper, classic running style', 'New Balance', 4.4, 'https://via.placeholder.com/300x200?text=New+Balance+574'),
                ('New Balance 327', 'Shoes', 8999.00, 16, 'Retro running style, oversized N logo, trail-inspired', 'New Balance', 4.3, 'https://via.placeholder.com/300x200?text=New+Balance+327'),
                ('Reebok Classic Leather', 'Shoes', 5999.00, 24, 'Soft leather upper, die-cut EVA midsole, timeless style', 'Reebok', 4.2, 'https://via.placeholder.com/300x200?text=Reebok+Classic+Leather'),
                ('Skechers D\'Lites', 'Shoes', 6999.00, 20, 'Chunky sole, leather/mesh upper, athletic style', 'Skechers', 4.0, 'https://via.placeholder.com/300x200?text=Skechers+D\'Lites'),
                ('Crocs Classic Clog', 'Shoes', 2995.00, 40, 'Croslite foam construction, ventilation holes, comfortable', 'Crocs', 4.1, 'https://via.placeholder.com/300x200?text=Crocs+Classic+Clog'),
                ('Red Tape Casual Sneakers', 'Shoes', 2999.00, 35, 'Synthetic leather, lightweight sole, everyday comfort', 'Red Tape', 3.8, 'https://via.placeholder.com/300x200?text=Red+Tape+Sneakers'),
                ('Woodland Leather Boots', 'Shoes', 8999.00, 12, 'Genuine leather, sturdy construction, outdoor style', 'Woodland', 4.3, 'https://via.placeholder.com/300x200?text=Woodland+Boots')
            ]
            
            # Combine all products
            all_products = (mobile_products + laptop_products + headphone_products + 
                          tv_products + wearable_products + shoe_products)
            
            # Insert all products
            insert_sql = """
            INSERT INTO products (name, category, price, stock, description, brand, rating, image_url) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cursor.executemany(insert_sql, all_products)
            connection.commit()
            
            # Count products by category
            cursor.execute("""
                SELECT category, COUNT(*) as count 
                FROM products 
                GROUP BY category 
                ORDER BY category
            """)
            category_counts = cursor.fetchall()
            
            print("✅ Enhanced product catalog inserted successfully!")
            print("\n📊 Products by category:")
            total_products = 0
            for category, count in category_counts:
                print(f"   📱 {category}: {count} products")
                total_products += count
            print(f"   🎯 Total: {total_products} products")
            
            # Update config file
            config_content = f"""# database/db_config.py
# Database configuration for Shopping Assistant
DB_CONFIG = {{
    "host": "{host}",
    "user": "{user}",
    "password": "{password}",
    "database": "student_db",
    "port": {port}
}}"""
            
            print("\n📝 Updating database/db_config.py...")
            try:
                with open('database/db_config.py', 'w') as f:
                    f.write(config_content)
                print("✅ Database configuration updated successfully!")
            except Exception as e:
                print(f"❌ Failed to update config: {e}")
            
            cursor.close()
            connection.close()
            
            print("\n🎉 Enhanced database setup completed successfully!")
            print("📋 Next steps:")
            print("   1. Run: python test_db_connection.py")
            print("   2. Run: python -m streamlit run app.py")
            print("   3. Open: http://localhost:8501")
            
            return True
            
    except Error as e:
        print(f"❌ Setup failed: {e}")
        return False

if __name__ == "__main__":
    setup_enhanced_database()
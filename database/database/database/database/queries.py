# database/queries.py
import mysql.connector
from mysql.connector import Error

try:
    from .db_config import DB_CONFIG
except Exception:
    try:
        from database.db_config import DB_CONFIG
    except Exception:
        DB_CONFIG = None

def get_connection():
    if not DB_CONFIG:
        raise RuntimeError("Missing DB_CONFIG - copy db_config_template.py -> db_config.py with credentials.")
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

def search_products(category=None, max_price=None, name_like=None, limit=10):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT id,name,category,price,stock,description FROM products WHERE 1=1"
    params = []
    if category:
        sql += " AND LOWER(category) LIKE %s"
        params.append(f"%{category.lower()}%")
    if max_price is not None:
        sql += " AND price <= %s"
        params.append(max_price)
    if name_like:
        sql += " AND LOWER(name) LIKE %s"
        params.append(f"%{name_like.lower()}%")
    sql += " ORDER BY price ASC LIMIT %s"
    params.append(limit)
    cursor.execute(sql, tuple(params))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

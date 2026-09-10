import sqlite3

def initialize_database(db_path: str) -> None:

    with sqlite3.connect(db_path) as con:  
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
        cur.executescript("""

    CREATE TABLE IF NOT EXISTS inventory_batches (
    sku TEXT NOT NULL,
    category TEXT NOT NULL,
    product_name TEXT NOT NULL,
    scale TEXT,
    color TEXT NOT NULL,
    gross_price REAL NOT NULL,
    net_price REAL NOT NULL,
    selling_price_online REAL NOT NULL,
    selling_price_b2c REAL NOT NULL,
    entry_date TEXT NOT NULL, 
    stock_units INTEGER NOT NULL CHECK (stock_units >= 0),
    PRIMARY KEY (sku, entry_date)
);

    CREATE TABLE IF NOT EXISTS sales_history (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL,
    batch_entry_date TEXT NOT NULL,
    sale_date TEXT NOT NULL,
    units_sold INTEGER NOT NULL CHECK (units_sold > 0),
    sale_price REAL NOT NULL,
    profit_share_partner_a REAL NOT NULL,
    profit_share_partner_b REAL NOT NULL,
    FOREIGN KEY (sku, batch_entry_date) REFERENCES inventory_batches(sku, entry_date)

);

    CREATE TABLE IF NOT EXISTS capital_ledger (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_date TEXT NOT NULL,
    description TEXT NOT NULL,
    partner_a_investment REAL NOT NULL CHECK (partner_a_investment >= 0),
    partner_b_investment REAL NOT NULL CHECK (partner_b_investment >= 0),
    total_investment REAL GENERATED ALWAYS AS (partner_a_investment + partner_b_investment) VIRTUAL

);

  """)
    con.close()

if __name__ == "__main__":
    initialize_database("erp_inventory.db")
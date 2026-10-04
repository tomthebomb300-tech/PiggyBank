import pandas as pd
import sqlite3

from Model.finances import Finances

class Sqlite_DB:
    def __init__(self):
        self.db_name = "./Model/piggy_bank.db"
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                UID TEXT PRIMARY KEY,
                StartAccountBalance REAL,
                StartCashBalance REAL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
                UID TEXT NOT NULL,
                Date TEXT NOT NULL,
                Amount REAL NOT NULL,
                PaymentMethod TEXT,
                ShopPerson TEXT,
                Location TEXT,
                Description TEXT,
                Category TEXT NOT NULL,

                FOREIGN KEY (UID)
                    REFERENCES users(UID)
            );
        """)


        self.conn.commit()
        print("Database and table created successfully")


    def get_finances(self, UID):
        self.cursor.execute("""
            SELECT *
            FROM users
            WHERE UID = ?
        """, (UID,))

        row = self.cursor.fetchone()

        query = """
            SELECT *
            FROM transactions
            WHERE UID = ?
        """

        df = pd.read_sql_query(query, self.conn, params=(UID,))
        df['Date'] = pd.to_datetime(df['Date'])
        return Finances(row[1], row[2], df)

    def pupulate_db_from_csv(self, UID):
        df = pd.read_csv("./Model/Data.csv")
        df = df[["Date", "Amount", "Payment Method", "Shop/Person", "Location", "Description", "Category"]]
        df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%Y")
        df = df.sort_values("Date")   
        df["Amount"] *= 100

        df.insert(0, "UID", UID) 
        df.columns = [
            "UID",
            "Date",
            "Amount",
            "PaymentMethod",
            "ShopPerson",
            "Location",
            "Description",
            "Category"
        ]
        print(df)
        df.to_sql(
            "transactions",
            self.conn,
            if_exists="append",
            index=False
        )

    def add_user(self, UID, bank_balance, cash_balance):
        self.cursor.execute("""
            INSERT INTO users (UID, StartAccountBalance, StartCashBalance)
            VALUES (?, ?, ?)
        """, (UID, bank_balance, cash_balance))
        self.conn.commit()
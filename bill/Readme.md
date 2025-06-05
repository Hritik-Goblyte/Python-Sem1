# Bill Management System

A Python-based billing system designed for a retail store that manages itemized bills under four categories: **Stationery**, **Clothing**, **Electrical Appliances**, and **Groceries**. It uses **MySQL** for database operations and stores all item transactions under each bill type.

## Features

* Text-based interactive menu
* Billing system with customer details, itemized input, and total calculation
* Automatic GST and discount calculation based on total
* Category-specific bill processing (Stationery, Clothing, Electrical Appliances, Grocery)
* Stores item details in MySQL database

---

## Prerequisites

* Python 3.x
* MySQL Server running with a database named `store`
* MySQL user with privileges (default user: `root`, password: empty string)
* Table `item` must exist in the `store` database:

```sql
CREATE TABLE item (
    serial_no INT,
    item_name VARCHAR(100),
    price FLOAT,
    quantity INT
);
```

---

## Installation

1. Clone this repository or copy the code to your local machine.

2. Install required Python packages:

```bash
pip install -r requirements.txt
```

3. Ensure your MySQL server is running, and the `store` database and `item` table are created as shown above.

4. Run the script:

```bash
python main.py
```

---

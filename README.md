# 🛒 Inventory System (Python)

## 📌 Description

A simple and efficient **inventory management system** built with Python.
It allows users to manage products, track stock, and analyze inventory data with support for CSV file storage.

---

## ⚙️ Features

* ➕ Add new products
* 📦 View inventory
* 🔍 Search products by name
* ✏️ Update price and quantity
* ❌ Delete products with confirmation
* 📊 View inventory statistics
* 💾 Save inventory to CSV
* 📂 Load inventory from CSV
* 🔄 Merge or overwrite existing data
* 🛡️ Input validation and error handling

---

## 🧠 Concepts Used

* Functions and modular programming
* Conditionals (`if`, `elif`, `else`)
* Lists and dictionaries
* File handling (`csv`, `os`)
* Exception handling (`try/except`)

---

## 🗂️ Project Structure

```
project/
│
├── app.py        # Main program (menu & flow)
├── functions.py  # Inventory operations
├── services.py   # Statistics logic
├── files.py      # CSV handling
```

---

## 🚀 Getting Started

### 📦 Requirements

* Python 3.x
* Terminal or code editor

### ▶️ Run the project

```bash
python app.py
```

---

## 📋 Menu

```
1 Add        → Add product  
2 Show       → View inventory  
3 Search     → Find product  
4 Update     → Modify data  
5 Delete     → Remove product  
6 Stats      → View statistics  
7 Save CSV   → Export data  
8 Load CSV   → Import data  
9 Exit       → Close program  
```

---

## 📊 Data Structure

Each product is stored as:

```python
{
  "name": "Product Name",
  "price": float,
  "quantity": int
}
```

---

## 💾 CSV Format

```
name,price,quantity
Laptop,1500,5
Mouse,25,10
```

✔ Rules:

* No negative values
* Correct header required
* Invalid rows are ignored

---

## 📈 Statistics

* Total inventory value
* Total number of units
* Most expensive product
* Product with highest stock

---

## 🔄 Data Handling

When loading a file:

* **Overwrite** → replaces inventory
* **Merge** → updates existing products and adds new ones

---

## ✨ Example

```
Option: 1
Product name: Mouse
Price: 25
Quantity: 10

→ Product added successfully
```

---  
## 🔄 Program Flow Diagram 
<img width="2048" height="898" alt="diagrama john" src="https://github.com/user-attachments/assets/1850c662-d03d-456d-bc6d-5d3a8f735c2b" /> 

---
## Repository 

https://github.com/Johns8729/PYTHON_WEEK-3_ASSIGNMENT/tree/main

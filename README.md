# FinTrack – Expense & Budget Tracker (Python + SQLAlchemy)

FinTrack - A simple command line expense tracking tool built using **Python** and **SQLAlchemy ORM** with **SQLite** database.

It enables effective management of expenditures, categories, and monthly budgets.

---

## ???? Features
- Add and manage expense categories
- Daily expenses record with date and amount
- View all recorded expenses
- Set monthly budget limits

- Check if money is being spent monthly

- SQLite database for persistent storage

—
## ????️ Technologies Used
- Python

- SQLAlchemy (ORM)

- SQLite

- Object-Oriented Programming (O
"Imagine
### ????️ Database Structure

### 1. Category Table
- `id` (Primary Key)
- `name`
- There can be multiple expenses for a single category
### 2. Expense Table

- id (Primary Key)
- title
- `amount`

- `date`

- `category_id` (Foreign Key

### 3. Budget Table
- `id` (Primary Key)
- `month`
- `limit`
*
## ???? Application Flow
1. Program begins and connects to SQLite database ‘fintrack.db’
2. A new table is automatically created if it does not already exist
3. User is presented with a menu showing available options

4. Based on User Input:

- Categories can be added - Expenses can be recorded - Expenses may be considered - A monthly budget can be created - Budget status can be checked 5. The program runs continuously until the user wants to exit --- ## ???? Menu Options

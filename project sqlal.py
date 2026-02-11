from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# ----- DATABASE SETUP -----
engine = create_engine("sqlite:///fintrack.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# ----- TABLES -----

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    expenses = relationship("Expense", back_populates="category")

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Float)
    date = Column(String)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="expenses")

class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True)
    month = Column(String)
    limit = Column(Float)

Base.metadata.create_all(engine)

# ----- FUNCTIONS -----

def add_category():
    name = input("Category name: ")
    session.add(Category(name=name))
    session.commit()
    print("Category added")

def add_expense():
    title = input("Title: ")
    amount = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")
    cat_id = int(input("Category ID: "))

    session.add(Expense(title=title, amount=amount, date=date, category_id=cat_id))
    session.commit()
    print("Expense added")

def show_expenses():
    expenses = session.query(Expense).all()
    for e in expenses:
        print(e.id, e.title, e.amount, e.date)

def set_budget():
    month = input("Month (YYYY-MM): ")
    limit = float(input("Limit: "))
    session.add(Budget(month=month, limit=limit))
    session.commit()
    print("Budget saved")

def check_budget():
    month = input("Month (YYYY-MM): ")
    budget = session.query(Budget).filter_by(month=month).first()

    if not budget:
        print("No budget found")
        return

    total = sum(
        e.amount for e in session.query(Expense)
        .filter(Expense.date.like(f"{month}%"))
    )

    print("Spent:", total)
    print("Limit:", budget.limit)

    if total > budget.limit:
        print(" Budget exceeded")
    else:
        print("Within budget")

# ----- MENU -----

def menu():
    while True:
        print("""
1. Add Category
2. Add Expense
3. Show Expenses
4. Set Budget
5. Check Budget
6. Exit
        """)

        choice = input("Choice: ")

        if choice == "1":
            add_category()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_expenses()
        elif choice == "4":
            set_budget()
        elif choice == "5":
            check_budget()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

menu()
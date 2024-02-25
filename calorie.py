import sqlite3
from datetime import datetime
conn = sqlite3.connect('calorie_tracker.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY,
        food TEXT NOT NULL,
        calories INTEGER NOT NULL,
        date DATE NOT NULL
    )
''')
conn.commit()

def add_meal(food, calories):
    today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute('INSERT INTO meals (food, calories, date) VALUES (?, ?, ?)', (food, calories, today))
    conn.commit()
    print("Meal added.")

def daily_calorie_total():
    today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute('SELECT SUM(calories) FROM meals WHERE date=?', (today,))
    result = cursor.fetchone()
    total_calories = result[0] if result[0] else 0
    print("Daily total calories:", total_calories)

def monthly_calorie_total():
    current_month = datetime.today().strftime('%Y-%m')
    cursor.execute('SELECT SUM(calories) FROM meals WHERE strftime("%Y-%m", date)=?', (current_month,))
    result = cursor.fetchone()
    total_calories = result[0] if result[0] else 0
    print("Monthly total calories:", total_calories)

def main():
    while True:
        print("\n1. Add a meal")
        print("2. View daily total calories")
        print("3. View monthly total calories")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            food = input("Enter the food you ate: ")
            calories = int(input("Enter the calories of the food: "))
            add_meal(food, calories)
        elif choice == "2":
            daily_calorie_total()
        elif choice == "3":
            monthly_calorie_total()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

# ------------------------------
# זו היא אפליקציה לחישוב הוצאות
# כרגע זה רק הממשק ויצירת הספרייה
# ------------------------------

import json
import os

DATA_FILE = "data/explores.json"
explore_list = {}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "first_explore": {"name_list": None, "sublist": []}
    }
def save_data(explore_list):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(explore_list, f, ensure_ascii=False, indent=2)
def opening_the_app():
    global explore_list
    explore_list = load_data()
    
    if explore_list["first_explore"]["name_list"] is None:
        create_new_list("first_explore")
    else:
        print("""
        אנא בחר באחד האפשרויות
        1. להכניס הוצאה
        2. לצפות ברשימות קיימות
        3. ליצור רשימה חדשה""")
    answer = input("").strip()

    if answer == "1":
        chosen = show_explore_list()     # מחזיר מפתח של הרשימה
        add_value()               # מעבירים אותו לפונקציה
    elif answer == "2":
        chosen = show_explore_list()
        show_explore_list()
    elif answer == "3":
        create_more_explore()
        chosen = show_explore_list()
    else:
        print("אפשרות לא חוקית")
def create_new_list(explore_key):
    # יצירת/עדכון שם רשימה
    if explore_list[explore_key]["name_list"] is None:
        print("""
מחשב הוצאות
אנא צור את הרשימה הראשונה:
הזן את שם הרשימה...
""", end=" ")
    else:
        print("""
מחשב הוצאות
הזן את שם הרשימה...
""", end=" ")

    name = input("").strip()
    explore_list[explore_key]["name_list"] = name
    save_data(explore_list)

    create_sublist(explore_key)
def show_explore_list():
    keys = list(explore_list.keys())

    # אם יש רק רשימה אחת
    if len(keys) == 1:
        only_key = keys[0]
        print(f"{explore_list[only_key]['name_list']}")
        return only_key

    # אם יש יותר מאחת
    print("אנא בחר באחת מהרשימות:\n")

    for i, key in enumerate(keys, start=1):
        name = explore_list[key]["name_list"]
        print(f"{i}. {name}")

    while True:
        answer = input("\nהכנס מספר: ").strip()

        if answer.isdigit():
            index = int(answer) - 1
            if 0 <= index < len(keys):
                selected_key = keys[index]
                return selected_key

        print("בחירה לא חוקית, נסה שוב.")
def create_sublist(explore_key):
    # יצירת תת-רשימות לרשימה שנבחרה
    while True:
        print("\nהזן את שם התת רשימה:", end=" ")
        sublist = input("").strip()

        if sublist:
            explore_list[explore_key]["sublist"].append(sublist)

        print("תרצה להוסיף עוד תת רשימה? (כן/לא)", end=" ")
        answer = input("").strip()

        if answer == "לא":
            break
        elif answer == "כן":
            continue
        else:
            print("תשובה לא חוקית")
def create_more_explore():
    index = 1
    while True:
        explore_key = f"explore_{index}"
        if explore_key not in explore_list:
            break
        index += 1

    explore_list[explore_key] = {
        "name_list": None,
        "sublist": []
    }

    create_new_list(explore_key)
def add_value():
    explore_key = input("לאיזה רשימה להכניס?").strip()
    sublist = input("ליזה תת קטגוריה ?").strip()
    some = input(float("כמה?")).strip()
    explore_list[explore_key][sublist].append(some)
if __name__ == "__main__":
    opening_the_app()

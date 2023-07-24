
# def revrse_num(number):
#     reverse = 0
#     while number != 0:
#         digit = number % 10
#         reverse = reverse * 10 + digit
#         number =number // 10
#     print( reverse)    
# number = int(input("enter a number:"))    
# revrse_num(number)

#The application will have a log-in for admin and users to log-in
# -------------------------------- Admin ----------------------------------

# ➡️ Admin will have the following functionalities: ⬅️

# 👉 1. Add new food items. Food Item will have the following details:
#         🔴 FoodID //It should be generated automatically by the application.
#         🔴 Name
#         🔴 Quantity. For eg, 100ml, 250gm, 4pieces etc
#         🔴 Price
#         🔴 Discount
#         🔴 Stock. Amount left in stock in the restaurant.

# 👉 2. Edit food items using FoodID.

# 👉 3. View the list of all food items.

# 👉 4. Remove a food item from the menu using FoodID.
# --------------------------------- User ----------------------------------


import json

def load_data():
    with open("C:\\New folder\\data.json", "r") as file:
        data = json.load(file)
    return (data)

def save_data(data):
    with open("C:\\New folder\\data.json", "w") as file:
        json.dump(data, file, indent=4)

def add_food_item(name, quantity, price, discount, stock):
    data = load_data()
    food_items = data["food_items"]
    
    if len(food_items) > 0:
        new_food_id = food_items[-1]["FoodID"] + 1
    else:
        new_food_id = 1
    
    new_food_item = {
        "FoodID": new_food_id,
        "Name": name,
        "Quantity": quantity,
        "Price": price,
        "Discount": discount,
        "Stock": stock
    }
    
    food_items.append(new_food_item)
    save_data("C:\\New folder\\data.json")
    print("New food item added successfully.")

def edit_food_item(food_id, name, quantity, price, discount, stock):
    data = load_data()
    food_items = data["food_items"]
    
    for item in food_items:
        if item["FoodID"] == food_id:
            item["Name"] = name
            item["Quantity"] = quantity
            item["Price"] = price
            item["Discount"] = discount
            item["Stock"] = stock
            save_data(data)
            print("Food item updated successfully.")
            return
    
    print("Food item not found.")

def view_food_items():
    data = load_data()
    food_items = data["food_items"]
    
    print("List of all food items:")
    for item in food_items:
        print(f"FoodID: {item['FoodID']}, Name: {item['Name']}, Quantity: {item['Quantity']}, Price: {item['Price']}, Discount: {item['Discount']}, Stock: {item['Stock']}")

def remove_food_item(food_id):
    data = load_data()
    food_items = data["food_items"]
    
    for item in food_items:
        if item["FoodID"] == food_id:
            food_items.remove(item)
            save_data(data)
            print("Food item removed successfully.")
            return
    
    print("Food item not found.")


view_food_items()


add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 50)
view_food_items()
# ➡️ The user will have the following functionalities: ⬅️

# 👉 1. Register on the application. Following to be entered for registration:
#         🔴 Full Name
#         🔴 Phone Number
#         🔴 Email
#         🔴 Address
#         🔴 Password

# 👉 2. Log in to the application

# 👉 3. The user will see 3 options:
#         🔴 Place New Order
#         🔴 Order History
#         🔴 Update Profile

# 👉 4. Place New Order: The user can place a new order at the restaurant.
#         🔵 Show list of food. The list item should as follows:
#             🔴 Tandoori Chicken (4 pieces) [INR 240]
#             🔴 Vegan Burger (1 Piece) [INR 320]
#             🔴 Truffle Cake (500gm) [INR 900]

# 👉 5. Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]

# 👉 6. Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.

# 👉 7. Order History should show a list of all the previous orders

# 👉 8. Update Profile: the user should be able to update their profile.

import json


def load_data():
    with open("C:\\New folder\\users.json", "r") as file:
        data= json.load(file)
    return data


def save_data(data):
    with open("C:\\New folder\\users.json", "w") as file:
        json.dump(data, file, indent=4)

def register_user(full_name, phone_number, email, address, password):
    data = load_data()
    users = data["users"]
    
    
    for user in users:
        if user["Email"] == email:
            print("User with this email already exists. Please try a different email.")
            return
    
    new_user = {
        "Full Name": full_name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address,
        "Password": password,
        "Order History": []
    }
    
    users.append(new_user)
    save_data(data)
    print("User registration successful.")


def login_user(email, password):
    data = load_data()
    users = data["users"]
    
    for user in users:
        if user["Email"] == email and user["Password"] == password:
            print("Login successful.")
            return user
    
    print("Invalid email or password.")
    return None

def update_profile(user_email, full_name, phone_number, address, password):
    data = load_data()
    users = data["users"]
    
    for user in users:
        if user["Email"] == user_email:
            user["Full Name"] = full_name
            user["Phone Number"] = phone_number
            user["Address"] = address
            user["Password"] = password
            save_data(data)
            print("Profile updated successfully.")
            return
    
    print("User not found.")


def place_new_order(user_email, selected_items):
    data = load_data()
    users = data["users"]
    food_items = data["food_items"]
    
    user = None
    for u in users:
        if u["Email"] == user_email:
            user = u
            break
    
    if not user:
        print("User not found.")
        return
    
    order_items = []
    total_cost = 0
    
    for item_number in selected_items:
        if 0 < item_number <= len(food_items):
            food_item = food_items[item_number - 1]
            order_item = {
                "FoodID": food_item["FoodID"],
                "Name": food_item["Name"],
                "Quantity": food_item["Quantity"],
                "Price": food_item["Price"]
            }
            order_items.append(order_item)
            total_cost += food_item["Price"]
    
    if len(order_items) == 0:
        print("No valid food items selected for order.")
        return
    
    order = {
        "OrderID": len(user["Order History"]) + 1,
        "Order Items": order_items,
        "Total Cost": total_cost
    }
    
    user["Order History"].append(order)
    save_data(data)
    print("Order placed successfully.")
    print("Order Details:")
    print(json.dumps(order, indent=4))


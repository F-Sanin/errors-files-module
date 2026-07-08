# ==========================================
# ДАНІ ДЛЯ ПРАКТИКИ З ОБРОБКИ ПОМИЛОК
# ==========================================

# Для Live Coding 1
raw_transactions = [
    "1500", "200", "N/A", "450", "Cancel", "3000", "120.50", "ERROR", "800", "NULL", 
    "50.25", "999", "-", "2500", "10", "Empty", "350", "15.99", "Failed", "4200"
]

# Для Guided Practice 1
clients_names = [
    "Alice Smith", "Bob", "Charlie Brown", "Diana", "Eve Adams", 
    "Frank", "Grace Kelly", "Hank", "Ivy Poison", "Jack", 
    "Karen Page", "Leo", "Mona Lisa", "Ned", "Olivia Pope",
    "Paul", "Quinn Fabray", "Rachel", "Steve Rogers", "Tony"
]

surnames = []
for client in clients_names:
    try:
        surnames.append(client.split()[1])
    except IndexError:
        surnames.append("Unknown")

# Для Live Coding 2
departments_sales = {
    "Tech": 150000,
    "Marketing": 0,
    "Sales": 450000,
    "HR": 0,
    "Finance": 120000,
    "Legal": 0,
    "Operations": 85000,
    "Customer Support": 25000
}
departments_employees = {
    "Tech": 15,
    "Marketing": 0,
    "Sales": 30,
    "HR": 0,
    "Finance": 8,
    "Legal": 0,
    "Operations": 12,
    "Customer Support": 5
}

# Для Guided Practice 2
ad_campaigns = [
    {"campaign": "Summer Sale", "revenue": 50000, "cost": 10000},
    {"campaign": "Free Promo", "revenue": 2000, "cost": 0},
    {"campaign": "Winter Fest", "revenue": 100000, "cost": 25000},
    {"campaign": "Organic Social", "revenue": 15000, "cost": 0},
    {"campaign": "Email Blast", "revenue": 30000, "cost": 5000},
    {"campaign": "Word of Mouth", "revenue": 8000, "cost": 0},
    {"campaign": "Google Ads", "revenue": 75000, "cost": 20000},
    {"campaign": "Partnership", "revenue": 5000, "cost": 0}
]

# Для Live Coding 3 та Guided Practice 3
complex_data = [
    {"client": "Alice Smith", "amount": "1200"},
    {"client": "Bob", "amount": "400"},
    {"client": "Charlie Brown", "amount": "N/A"},
    {"client": "Diana Prince", "amount": "5500"},
    {"client": "Eve", "amount": "Error"},
    {"client": "Frank Castle", "amount": "800"},
    {"client": "Grace", "amount": "150.50"},
    {"client": "Hank Pym", "amount": "-"},
    {"client": "Ivy", "amount": "3000"},
    {"client": "Jack Reacher", "amount": "NULL"}
]
#
# for client in complex_data:
#     try:
#         client["client"] = client["client"].split()[1]
#     except IndexError:
#         client["client"] = "Unknown"
#     try:
#         client["amount"] = int (client["amount"])
#     except ValueError:
#         client["amount"] = 0
#     finally:
#         print(f"Опрацювання запису про клієнта {client["client"]} завершено")
#
# print(complex_data)

# Ваш код для завдань нижче:

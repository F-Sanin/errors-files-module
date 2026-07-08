import csv
import json

# # Ваш код для завдань нижче:
# with open("files/transactions.csv", "r", encoding="UTF-8") as file:
#     transactions = list(csv.DictReader(file))
# transactions_failed = [tr for tr in transactions if tr["status"] == "failed"]
#
# with open("files/transactions_failed.csv", "w", encoding="UTF-8", newline="") as file:
#     columns = list(transactions_failed[0].keys())
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(transactions_failed)

with open("files/users.json", "r", encoding="utf-8") as file:
    users = json.load(file)
for user in users:
    if user["balance"] > 1000:
        user["status"] = "VIP"
    else:
        user["status"] = "Regular"

with open("files/users.json", "w", encoding="utf-8") as file:
    json.dump(users, file, ensure_ascii=False, indent=4)
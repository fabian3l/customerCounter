from woocommerce import API
import requests
from collections import defaultdict
import csv

wcapi = API(
    url="https://deeropole.pl",
    consumer_key="ck_8b10f20153f9dbaaaf5990914cd176b3fce9bd93",
    consumer_secret="cs_226f95a09550d1576a1940367921ba94474e5a29",
    version="wc/v3"
)
# Initialize variables
page = 1
per_page = 1  # Number of orders per page
customer_data = []
print('start')

while True:
    orders = wcapi.get("orders", params={"per_page": per_page})
    # orders = wcapi.get("orders", params={"per_page": per_page, "page": page})

    # Check if the request was successful
    if orders.status_code == 200:
        order_data = orders.json()

        # Check if there are no more orders on this page
        if not order_data:
            break
        print(order_data)

        # Iterate through orders and collect customer data
        # for order in order_data:
        #     email = order['billing']['email']
        #     first_name = order['billing']['first_name']
        #     last_name = order['billing']['last_name']

        #     # Find the customer's data in the list or add a new entry if not found
        #     customer_entry = next((c for c in customer_data if c['email'] == email), None)
        #     if customer_entry is None:
        #         customer_entry = {'email': email, 'first_name': first_name, 'last_name': last_name, 'purchase_count': 0}
        #         customer_data.append(customer_entry)

        #     # Increment the purchase count for the customer
        #     customer_entry['purchase_count'] += 1

        # # Move to the next page
        # page += 1
    else:
        print("Failed to retrieve orders. Status code:", orders.status_code)
        break

# Define the CSV file name
csv_file = 'customer_data2.csv'

# Write customer data to the CSV file
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     # Write header
#     writer.writerow(['Email', 'First Name', 'Last Name', 'Purchase Count'])
#     # Write data
#     for customer in customer_data:
#         writer.writerow([customer['email'], customer['first_name'], customer['last_name'], customer['purchase_count']])

# print(f"Customer data saved to {csv_file}.")
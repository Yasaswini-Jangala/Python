# inventory = [
#     # name,       category,   unit_price, units_sold, units_left
#     ["Strawberry", "Fruit",      3.50,        40,          10],
#     ["Broccoli",   "Vegetable",  2.20,        25,           8],
#     ["Cheddar",    "Dairy",      5.00,        18,           4],
#     ["Baguette",   "Bakery",     2.80,        35,           2],
#     ["Blueberry",  "Fruit",      4.00,        22,           6],
#     ["Spinach",    "Vegetable",  1.80,        30,          12],
#     ["Yogurt",     "Dairy",      1.20,        50,          15],
#     ["Croissant",  "Bakery",     3.00,        28,           3]]

# # Calculate the total revenue
# revenue = 0
# for _, _, unit_price, units_sold, _ in inventory: 
#     revenue += unit_price * units_sold
# print(f'Total Revenue: {revenue}')

# # List low stock items (units_left < 5)
# low_stock_items = []
# for name, _, _, _, units_left in inventory:
#     if units_left < 5:
#         low_stock_items.append(name)
# print(f'Low Stock Items: {low_stock_items}')

# # Calculate category-wise revenue
# revenue_f = revenue_v = revenue_d = revenue_b = 0
# for name, category, unit_price, units_sold, units_left in inventory:
#     if category == 'Fruit':
#         revenue_f += unit_price * units_sold
#     elif category == 'Vegetable':
#         revenue_v += unit_price * units_sold
#     elif category == 'Dairy':
#         revenue_d += unit_price * units_sold
#     elif category == 'Bakery':
#         revenue_b += unit_price * units_sold
# print(f'Total Revenue for Fruit: ${revenue_f:.2f}')
# print(f'Total Revenue for Vegetable: ${revenue_v:.2f}')
# print(f'Total Revenue for Dairy: ${revenue_d:.2f}')
# print(f'Total Revenue for Bakery: ${revenue_b:.2f}')
# print(f'Category-Wise Total Revenue: ${revenue_f + revenue_v + revenue_d + revenue_b:.2f}')
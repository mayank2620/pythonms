def get_top_three_items(shop_items):
    sorted_items = sorted(shop_items.items(),
key=lambda x: x[1], reverse=True)
    top_three = sorted_items[:3]
    return top_three
shop_items = {'apple': 2.5, 'banana': 1.5, 'orange': 3,
'mango': 2, 'pear': 1}
top_three_items = get_top_three_items(shop_items)
print(top_three_items)
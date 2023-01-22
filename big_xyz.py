data = [{'Id': '001', 'Order': 'Buy', 'Type': 'Add', 'Price':20.0, 'Quantity':100},
        {'Id': '002', 'Order': 'Sell', 'Type': 'Add', 'Price':25.0, 'Quantity':200},
        {'Id': '003', 'Order': 'Buy', 'Type': 'Add', 'Price':23.0, 'Quantity':50},
        {'Id': '004', 'Order': 'Buy', 'Type': 'Add', 'Price':23.0, 'Quantity':70},
        {'Id': '003', 'Order': 'Buy', 'Type': 'Remove', 'Price':23.0, 'Quantity':50},
        {'Id': '005', 'Order': 'Sell', 'Type': 'Add', 'Price':28, 'Quantity':100}
]


buy = 0
sell = 0
for row in data:
    for key, value in row.items():
        sum_of_row = row['Price'] * row['Quantity']
        if value == 'Buy':
            if row['Type'] == 'Remove':
                buy -= sum_of_row
            else:
                buy += sum_of_row
        if value == 'Sell':
            if row['Type'] == 'Remove':
                sell -= sum_of_row
            else:
                sell += sum_of_row
    print('buy: ', buy)
    print('sell: ', sell)

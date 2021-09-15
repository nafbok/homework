data_shop = {'meat': {
                    'pork': {
                            'price': 15,
                            'amount': 20
                            },
                    'chicken': {
                             'price': 12,
                             'amount': 20
                             },
                     },
             'vegetables': {
                    'carrot': {
                            'price': 5,
                            'amount': 20
                              },
                    'onion': {
                            'price': 15,
                            'amount': 20
                             }
                     },
             'milk': {
                    'cheese': {
                            'price': 15,
                            'amount': 20
                              },
                    'kefir':  {
                            'price': 15,
                            'amount': 20
                            }
                    },
            'fruits': {
                    'apple': {
                            'price': 2,
                            'amount': 50
                    },
                    'plum': {
                            'price': 3,
                            'amount': 15
                    }
             },
            'cereals': {
                    'rise': {
                            'price': 14,
                            'amount': 35
                    },
                    'buckweat': {
                            'price': 15,
                            'amount': 20
                    }
                }
}

custom_input = input('Enter the item: ')
for category, subcategor in data_shop.items():
    if custom_input == subcategor:
        print(data_shop[category][subcategor])


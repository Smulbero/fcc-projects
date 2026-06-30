class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):        
        self.ledger.append({ 'amount': amount, 'description': description })

    def withdraw(self, amount, description = ''):        
        if self.check_funds(amount):
            self.ledger.append({ 'amount': -abs(amount), 'description': description })
            return True
        return False

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.ledger.append({ 'amount': amount, 'description': f'Transfer from {self.name}'})
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False
    
    def __str__(self):
        output = ''

        # Title
        output += self.name.center(30, '*') + '\n'

        # Ledger entires
        for i, entry in enumerate(self.ledger):
            description = entry['description'][:23]
            amount = f'{entry["amount"]:.2f}'
            output += f'{description:<23}{amount:>7}\n' 

        # Total
        output += f'Total: {self.get_balance():.2f}'

        return output

def create_spend_chart(categories):
    if not isinstance(categories, list):
        print(f'Expected input: list, got {type(categories)}')
        return   

    category_withdrawals = []
    for category in categories:
        withdrawals = 0
        for entry in category.ledger:
            # Look for withdrawal entries and sum them up after converting them into positive numbers
            if entry['amount'] < 0:
                withdrawals += abs(entry['amount'])
        category_withdrawals.append({ 'category': category.name, 'withdrawals': withdrawals })

    total_withdrawals = sum(entry['withdrawals'] for entry in category_withdrawals)

    for entry in category_withdrawals:
        entry.update({ 'percentage': entry['withdrawals'] / total_withdrawals * 100 })
    
    #--------------------
    # Generate the output
    #--------------------
    output = ''

    # Title
    title = 'Percentage spent by category\n'
    output += title

    # Chart data
    for i in range(100, -1, -10):
        row = f'{i:>3}|'
        for entry in category_withdrawals:
            if entry['percentage'] >= i:
                row += ' o '
            else:
                row += f'{" ":3}'
        row += ' '
        output += row + '\n'
    
    # Horizontal line
    horizontal_line = f'{" ":4}{"-" * (len(category_withdrawals) * 3 + 1)}\n'
    output += horizontal_line

    # Vertical category names
    max_name_length = max(len(entry['category']) for entry in category_withdrawals)

    for i in range(max_name_length):
        row = f'{" ":4}'
        for name in category_withdrawals:
            if i < len(name['category']):
                row += f' {name["category"][i]} '
            else:
                row += f'{" ":3}'
        row += ' '
        if i != max_name_length - 1 :
            row += '\n'
        output += row

    return(output)


def main():
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')

    clothing = Category('Clothing')
    clothing.deposit(1000, 'initial deposit')
    clothing.withdraw(32, 'groceries')
    clothing.withdraw(161, 'restaurant and more food for dessert')

    auto = Category('Auto')
    auto.deposit(1000, 'initial deposit')
    auto.withdraw(11, 'groceries')
    auto.withdraw(77, 'restaurant and more food for dessert')

    test = Category('Test')
    test.deposit(1000, 'initial deposit')
    test.withdraw(15.89, 'restaurant and more food for dessert')

    print(food)

    bar_chart = create_spend_chart([food, clothing, auto, test])
    print(bar_chart)

if __name__ == '__main__':
    main()
class ShoppingCart:
    def __init__(self, employee_discount=None, total = 0, items = []):
        self._total = total
        self._items = items
        self._employee_discount = employee_discount

    @property
    def total(self):
        return self._total
    # @total.setter
    # def add_total(self, additional_amount):
    #     return self._total += additional_amount

    @property
    def items(self):
        return self._items
    # @items.setter
    def add_item(self,name,price,quantity=1):
        ND = {'name':name,'price':price,'quantity':quantity}
        self._items.append(ND)
        self._total += price*quantity
        return self._total

    @property
    def employee_discount(self, employee_discount=None):
            return self._employee_discount
    # @employee_discount.setter
    # def update_employee_discount(self, updated_amount):
    #     return self._employee_discount = updated_amount

    def mean_item_price(self):
        item_prices = list(map(lambda item:item['price'],self._items))
        sum_of_items = sum(item_prices)
        num_of_items = len(item_prices)
        return sum_of_items/num_of_items

    def median_item_price(self):
        item_prices = list(map(lambda item:item['price'],self._items))
        num_of_items = len(item_prices)
        if len(item_prices)%2==0:
            return (item_prices[(num_of_items/2)]+item_prices[(num_of_items/2)+1])/2
        else:
            return item_prices[round(num_of_items/2)]

    def apply_discount(self):
        if self.employee_discount==None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            item_prices_full = list(map(lambda item:item['price'],self._items))
            sum_of_items_full = sum(item_prices_full)
            # return self.employee_discount
            return sum_of_items_full
            # return 1-self.employee_discount/100
            # return sum_of_items*(1-(int(self.employee_discount)/100))

    def item_names(self):
        return list(map(lambda item:item['name'],self._items))

    def void_last_item(self):
        self._items.pop()

class ShoppingCart:
    def __init__(self, employee_discount=None, total = 0, items = None):
        self._total = total
        self._items = items or []
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
        if quantity==1:
            ND = {'name':name,'price':price,'quantity':quantity}
            self.items.append(ND)
            self._total += price*quantity
        else:
            for q in list(range(0, quantity)):
                q = {'name':name,'price':price,'quantity':1}
                self.items.append(q)
                self._total += price
        return self._total

    @property
    def employee_discount(self, employee_discount=None):
            return self._employee_discount
    # @employee_discount.setter
    # def update_employee_discount(self, updated_amount):
    #     return self._employee_discount = updated_amount

    def mean_item_price(self):
        item_prices = list(map(lambda item:item['price'],self.items))
        sum_of_items = sum(item_prices)
        num_of_items = len(item_prices)
        return sum_of_items/num_of_items

    def median_item_price(self):
        item_prices = list(map(lambda item:item['price'],self.items))
        num_of_items = len(item_prices)
        if len(item_prices)%2==0:
            return (item_prices[(num_of_items/2)]+item_prices[(num_of_items/2)+1])/2
        else:
            return item_prices[round(num_of_items/2)]

    def apply_discount(self):
        if self.employee_discount==None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            item_prices_full = list(map(lambda item:item['price'],self.items))
            sum_of_items_full = sum(item_prices_full)
            return sum_of_items_full*(1-(int(self.employee_discount)/100))

    def item_names(self):
        return list(map(lambda item:item['name'],self.items))

    def void_last_item(self):
        for k, v in self.items[0].items():
            k.pop()

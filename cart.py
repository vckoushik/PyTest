from typing import List


class Cart:
    def __init__(self, max_size: int) -> None:
        #Initializing empty cart 
        self.items: List[str] = []
        self.max_size = max_size

    def add(self, item: str):

        if self.size() == self.max_size:
            raise OverflowError("Cart is full, cannot add items....")
        
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        total_price = 0.0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price
    
    def delete_item(self,item):
        if item not in self.items:
            raise KeyError("Cannot delete non existing item in cart")
        self.items.remove(item)
    
        
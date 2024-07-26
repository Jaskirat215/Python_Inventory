class Sales:
    @staticmethod
    def applydiscount(price, discount):
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100")
        discount_amount = price * (discount / 100)
        return price - discount_amount

    @staticmethod
    def calculatesalesprice(price, tax_rate):
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative")
        tax_amount = price * (tax_rate / 100)
        return price + tax_amount


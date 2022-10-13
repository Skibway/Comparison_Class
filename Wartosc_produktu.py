class Compare:

    def __init__(self, price_per_weight_brutto, products, products_price_weight):
        self.price_per_weight_brutto = price_per_weight_brutto
        self.products = products
        self.products_price_weight = products_price_weight

    def price_per_gram(self, i):
        if len(self.products_price_weight.get(i)) == 2:
            x = self.products_price_weight.get(i)[0]
            y = self.products_price_weight.get(i)[1]
            return (x * 1)/y
        else:
            OSError            

    def prod_perc_value_in_1kg(self, i):
        kg = 1000
        x = self.products.get(i)[0]
        if len(self.products.get(i)) > 1:
            for j in self.products.get(i):
                kg *= j
            return kg
        elif len(self.products.get(i)) == 1:
            kg *= x
            return kg
        else:
            OSError

    def summary(self):
        a = self.price_per_weight_brutto[0]
        b = self.price_per_weight_brutto[1]
        sum = 0
        list_of_prod = []
        print("\n")
        for i in self.products:
            x = Compare.price_per_gram(self, i)
            y = Compare.prod_perc_value_in_1kg(self, i)
            sum += x * y
            list_of_prod.append(f"{i}\t=\t:\t{round(x*y, 2)}\tfor\t{y} grams\n")
        return f"""
        {str(i for i in list_of_prod)}
        {round(sum, 2)} zloty for 1000g homemade oatmeal
        Comparing bought and homemade oatmeals
        Bought oatmeal equals: 
        {a} zloty for {b} grams
        Homemade oatmeal equals: 
        {round(sum * b / 1000, 2)} zloty for {b} grams"""
        


price_brutto = [11.24, 450]

percentage = {
    'rolled oats': [78/100],
    'dark chocolate': [8/100],
    'dry dates': [8/100, 95/100],
    'rice flour': [8/100, 5/100],
    'milk chocolate': [4/100],
    'chicory inulin': [2/100]
}

product_price_weight = {
    'rolled oats': [8.56 ,1000],
    'dark chocolate': [36.23, 100],
    'dry dates': [8, 500],
    'rice flour': [9.27, 500],
    'milk chocolate': [67.99, 1000],
    'chicory inulin': [15.79, 500]
}
with open("/Users/piotrskiba/Documents/GitHub/Comparison_Class/result.txt", "w") as f:
    if __name__ == "__main__":
            result = Compare(price_brutto, percentage, product_price_weight)
            f.write(result.summary())
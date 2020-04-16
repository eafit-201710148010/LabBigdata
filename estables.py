from mrjob.job import MRJob

class MREstables(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        try:
            price = float(price)
        except ValueError:
            pass
        else:
            yield company, (price, date)

    def reducer(self, company, pricedates):
        estable_price, estable_date = next(pricedates)
        estable = True
        for price, date in pricedates:
            if price < estable_price:
                estable = False
                 
        yield company, estable

if __name__ == '__main__':
    MREstables.run()
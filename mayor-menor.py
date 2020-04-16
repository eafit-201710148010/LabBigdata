from mrjob.job import MRJob

class MRMayorMenor(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        try:
            price = float(price)

        except ValueError:
            pass

        else:
            yield company, (price, date)

    def reducer(self, company, pricedates):
        minValue, minDate = next(pricedates)
        maxValue, maxDate = minValue, minDate
        result = {}
        for price, date in pricedates:
            if price < minValue:
                minValue, minDate = price, date
    
            if price > maxValue:
                maxValue, maxDate = price, date
            
        result["dia menor"] = (minDate)
        result["dia mayor"] = (maxDate)
        yield company, result

if __name__ == '__main__':
    MRMayorMenor.run()
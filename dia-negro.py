from mrjob.job import MRJob, MRStep

class MRBlackDay(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        try:
            price = float(price)

        except ValueError:
            pass

        else:
            yield company, (price, date)

    def reducerDateMin(self, company, pricedates):
        val_min, date_min = next(pricedates)
        for price, date in pricedates:
            if price < val_min:
                val_min, date_min = price, date
        
        yield date_min, 1
    
    def reducerValues(self, date, value):
        yield "date" , (date, sum(value))

    def reducerBlackDay(self, date, values):
        blackDay, actualValue = next(values)
        for date, value in values:
            if actualValue < value:
                blackDay = date
        
        yield "blackDay", blackDay

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducerDateMin),
                MRStep(reducer=self.reducerValues), MRStep(reducer=self.reducerBlackDay)]

if __name__ == '__main__':
    MRBlackDay.run()
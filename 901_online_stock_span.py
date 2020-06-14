class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        span = 1
        for i in range(len(self.prices)):
            if self.prices[len(self.prices) - i - 1] <= price:
                span += 1
            else:
                break
        self.prices.append(price)
        return span


ss = StockSpanner()
spans = []
for price in [100, 80, 60, 70, 60, 75, 85]:
    spans.append(ss.next(price))
print(spans)

def divide(dividend: int, divisor: int) -> int:
        val = 0
        while dividend > divisor:
            dividend = dividend - divisor
            val =  val + 1
        return val

print(divide(100,3))
print(divide(0,3))
print(divide(4,3))

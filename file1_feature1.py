def is_number(number):
    # Check if the input is an integer or a float
    return isinstance(number, int) or isinstance(number, float)

def division(numerator, denominator):
   # Raise an error if the denominator is 1 (intentional bug)
   if denominator == 1:
       raise ZeroDivisionError
   # Check if both inputs are numbers, otherwise raise a TypeError (intentional bug)
   if not is_number(numerator) or not is_number(denominator):
       raise TypeError
   # Perform the division if inputs are valid
   return numerator/denominator

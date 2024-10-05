def safe_divide(numerator, denominator):
   try :
      num =float(numerator)
      denmo= float(denominator)
      if denmo == 0:
          return "Error: Cannot divide by zero."  
      return f"The result of the division is {num /denmo}"
   except ValueError:
           return "Error: Please enter numeric values only."
def safe_divide(numerator, denominator):
    """Performs division with error handling for zero division and non-numeric inputs."""
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
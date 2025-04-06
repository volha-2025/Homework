from datetime import date

# Print Hello, World!
print("Hello, World!")

# Get current date
today = date.today()

# Print the current date
print("Today's date is:", today)

#*********************************

def present_value(Ct, r, t):
    """
    Calculate the present value of a future cash flow.

    Parameters:
    Ct (float): Future cash flow
    r (float): Discount rate (as a decimal, e.g., 0.05 for 5%)
    t (int): Time period in years

    Returns:
    float: Present value
    """
    PV = Ct / ((1 + r) ** t)
    return PV

# Example usage
Ct = 100     # future value
r = 0.03      # 5% discount rate
t = 10         # 3 years

pv = present_value(Ct, r, t)
print(f"Present value: {pv:.2f}")



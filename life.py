#A machine is purchased which will produce earning of Rs. 1000 per year while it lasts. 
# The machine costs Rs. 6000 and will have a salvage value of Rs. 2000 when it is condemned. 
# If 9 percent per annum can be earned on alternate investments, 
# write a program to determine what will be the minimum life of the machine to make it a more attractive investment compared to alternative investment?


# Constants
cost = 6000  # Initial cost of the machine
annual_earning = 1000  # Annual earnings
salvage_value = 2000  # Salvage value
discount_rate = 0.09  # 9% annual interest rate

# Finding the minimum life of the machine
n = 1  # Start with 1 year
while True:
    # Calculate the present value of annual earnings
    present_value = sum(annual_earning / (1 + discount_rate) ** year for year in range(1, n + 1))
    # Add the present value of the salvage value
    present_value += salvage_value / (1 + discount_rate) ** n
    
    # Check if the present value exceeds the cost
    if present_value > cost:
        break  # Stop if machine becomes a better investment
    n += 1  # Increment the life of the machine

# Output the result
print(f"The minimum life of the machine to be a better investment is {n} years.")


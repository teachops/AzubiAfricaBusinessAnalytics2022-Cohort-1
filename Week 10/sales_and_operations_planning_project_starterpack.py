
# Ask user to enter the initial stock level, cast to integer and save as initial_stock_level


# Ask user to enter the planning horizon (number of months to plan), cast to integer and save as no_of_months


# Set an Accumulator for the dictionary of monthly sales


# For each month, ask user to enter the forecasted sale
# To do this loop through the month using a range
# for month in range(1, no_of_months+1):
#       Ask user to enter the forecasted sale for the month, cast to integer and save as forecast
#      Add the forecast to the dictionary of monthly sales


# Print the resulting production quantities for each month

# Loop through the dictionary of monthly sales:
#       Check if forecast_sales > Initial Stock
#           print(f"Production Quantity for Month")
#           Reduce the stock level by the production Amount

#      Else:
#        How much do you have to produce for this month?
#        Print the Production Quantity
#        Update the stock level

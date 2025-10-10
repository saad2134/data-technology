# Create a simple sales analysis
daily_sales = [245, 312, 189, 467, 398, 521, 234]

# Calculate key metrics
total_sales = sum(daily_sales)
average_sales = total_sales / len(daily_sales)
max_sales = max(daily_sales)
min_sales = min(daily_sales)

print(f"Total Weekly Sales: ${total_sales}")
print(f"Average Daily Sales: ${average_sales:.2f}")
print(f"Best Day: ${max_sales}")
print(f"Worst Day: ${min_sales}")
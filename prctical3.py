# Program 2: Retail Sales Performance Analyzer

# List of sales figures for a week
weekly_sales = [1200, 3500, 800, 4200, 5000, 2100, 950]

total_revenue = 0
high_performing_days = 0
low_performing_days = 0

print("--- Daily Sales Performance Report ---")

# Looping construct: Iterate through each day's sales in the list
for day_index, daily_total in enumerate(weekly_sales, start=1):
    
    # Add to the running total
    total_revenue += daily_total

    # Decision making: Categorize daily performance based on business targets
    if daily_total >= 3500:
        performance_rating = "Excellent (Exceeded Target)"
        high_performing_days += 1
    elif daily_total >= 1500:
        performance_rating = "Average (Met Target)"
    else:
        performance_rating = "Poor (Below Target)"
        low_performing_days += 1

    print(f"Day {day_index}: ${daily_total} - {performance_rating}")

# Calculate summary statistics after the loop completes
average_sales = total_revenue / len(weekly_sales)

print("\n--- Weekly Summary ---")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Daily Sales: ${average_sales:.2f}")
print(f"High Performing Days (>= $3500): {high_performing_days}")
print(f"Low Performing Days (< $1500): {low_performing_days}")

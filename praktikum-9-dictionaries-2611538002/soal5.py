n = int(input())
funds = {}

for _ in range(n):
    name, amount_str = input().split()
    amount = int(amount_str)
    funds[name] = funds.get(name, 0) + amount

for name, total in funds.items():
    print(f"{name}: {total}")

total_cash = sum(funds.values())
print(f"Total cash: {total_cash}")

if funds:
    top_name = None
    top_total = -1
    for name, total in funds.items():
        if total > top_total:
            top_total = total
            top_name = name
    print(f"Top contributor: {top_name} ({top_total})")
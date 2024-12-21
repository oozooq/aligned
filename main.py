import csv

# Шлях до файлів
wallets_file = "wallets.txt"
csv_file = "wallets.csv"
output_file = "matching_wallets.txt"

# Зчитуємо адреси з wallets.txt
with open(wallets_file, "r") as f:
    wallets = set(line.strip().lower() for line in f if line.strip())

# Готуємо файл для запису результатів
with open(output_file, "w") as output:
    output.write("Знайдені адреси:\n")

    # Зчитуємо CSV пострічно та шукаємо збіги
    with open(csv_file, "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if row:
                csv_wallet = row[0].strip().lower()
                if csv_wallet in wallets:
                    output.write(csv_wallet + "\n")

print(f"Результати записані у файл {output_file}")

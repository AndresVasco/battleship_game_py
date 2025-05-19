import statistics
import csv

#Leer los datos de ventas mensuales desde el csv
monthly_sales = {}
try:
    with open('monthly_sales.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            month = row.get('month')
            sales = row.get('sales')
            if month and sales:
                monthly_sales[month] = int(sales)
except FileNotFoundError:
    print("Error: The file 'monthly_sales.csv' was not found.")
except ValueError:
    print("Error: Invalid data format in 'monthly_sales.csv'.")
        
sales = list(monthly_sales.values())
print(sales)

#hallar la media
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales}")

#hallar la moda
mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

#Desviación estándar
stdev_sales = statistics.stdev(sales)
print(f"la desviación estandar es: {stdev_sales}")

#Varianza
viariance_sales = statistics.variance(sales)
print(f"la varianza es: {viariance_sales}")

#maximo y minimo
max_sales = max(sales)
print(f"El maximo es: {max_sales}") 

min_sales = min(sales)
print(f"El minimo es: {min_sales}")

range_sales = max_sales - min_sales
print(f"El rango es: {range_sales}")


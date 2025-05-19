import csv

file_path = 'products.csv'
updated_file_path = 'products_updated.csv'
tax_included_file = 'products_tax_included.csv'

with open (file_path, mode = 'r') as file:
    csv_reader = csv.DictReader(file)
    
    #Obetener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_value']
    
    #Empezar a escribir el nuevo archivo CSV
    with open (updated_file_path, mode = 'w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #Escribir encabezado en el nuevo archivo CSV
    
        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity']) #valor total
            csv_writer.writerow(row)

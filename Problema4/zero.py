import csv
input_file = 'temperaturas.csv'
output_file = 'resumen_temperaturas.txt'

with open(input_file, 'w') as f:
    f.write("2024-01-01,15.5\n")
    f.write("2024-01-02,17.0\n")
    f.write("2024-01-03,16.2\n")
    f.write("2024-01-04,14.8\n")
    f.write("2024-01-05,18.1\n")
    f.write("2024-01-06,13.9\n")
    f.write("2024-01-07,19.3\n")
    f.write("2024-01-08,20.1\n")
    f.write("2024-01-09,21.4\n")
    f.write("2024-01-10,22.0\n")

temperaturas = []

with open(input_file, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        fecha, temperatura = row
        temperaturas.append(float(temperatura))  

temperatura_promedio = sum(temperaturas) / len(temperaturas)
temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)

with open(output_file, mode='w') as file:
    file.write(f'Temperatura Promedio: {temperatura_promedio:.2f}°C\n')
    file.write(f'Temperatura Máxima: {temperatura_maxima:.2f}°C\n')
    file.write(f'Temperatura Mínima: {temperatura_minima:.2f}°C\n')

print(f'Resultados escritos en {output_file}')

import csv



def clean_price(price):
    # Удаление символов '₽/мес.' и преобразование в числовый тип данных
    return int(price.replace('₽/мес.', '').replace(' ', ''))

input_file = 'prices.csv'
output_file = 'clean_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и Записываем данные в выходной файл
    header =next(reader)
    writer.writerow(header)

    # Запись данных в выходной файл
    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)

print(f'Обработанные данные успешно сохранены в файл {output_file}')

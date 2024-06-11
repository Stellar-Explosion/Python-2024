import os
import csv
import json
from jinja2 import Environment, FileSystemLoader

class CityData:
    def __init__(self):
        self.data = []

    # Загрузка данных из CSV
    def load_from_csv(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data.append({
                    "city": row['Город'],
                    "population": row['Население'],
                    "region": row['Регион'],
                    "postal_code": row['Индекс']
                })

    def load_from_json(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            for item in json_data['data']:
                self.data.append({
                    "city": item['Город'],
                    "population": item['Население'],
                    "region": item['Регион'],
                    "postal_code": item['Индекс']
                })
                
    def get_data(self):
        return self.data

city_data_manager = CityData()

csv_file_path = os.path.join(current_dir, 'Города.csv')
json_file_path = os.path.join(current_dir, 'Города.json')

city_data_manager.load_from_csv(csv_file_path)
city_data_manager.load_from_json(json_file_path)

env = Environment(loader=FileSystemLoader(current_dir))
template = env.get_template('template.html')

html_output = template.render(cities=city_data_manager.get_data())

with open('cities_report.html', 'w', encoding='utf-8') as f:
    f.write(html_output)
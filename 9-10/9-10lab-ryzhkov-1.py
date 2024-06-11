import json  # Мне нужен этот модуль, чтобы работать с файлами в формате JSON.
import os  # Этот модуль поможет мне проверить, существует ли файл.

class MessageFormatter:
    # Здесь я начинаю описание класса, который будет форматировать сообщения.
    def __init__(self, path_to_json=None, path_to_template=None, username=None, years=None, gift=None, seating=None) -> None:
        # Это основа класса, где я задаю начальные значения.
        self.username = username
        self.years = years
        self.gift = gift
        self.seating = seating
        self.msg_template = ''
        self.template_file_path = path_to_template  # Путь к файлу с шаблоном.
        self.json_file_path = path_to_json  # Путь к файлу с данными пользователя.
        self.user_responses = {}  # Здесь будут храниться ответы пользователя.
        # Если путь к файлу указан и файл существует, я загружаю данные.
        if path_to_json and os.path.isfile(path_to_json):
            self.load_user_responses()
        if path_to_template and os.path.isfile(path_to_template):
            self.load_msg_template()
        
    def load_msg_template(self):
        # Загружаю шаблон сообщения из файла.
        with open(self.template_file_path, 'r', encoding='utf-8') as tmpl_file:
            self.msg_template = tmpl_file.read()
            return self.msg_template

    def load_user_responses(self):
        # Загружаю ответы пользователя из JSON файла.
        with open(self.json_file_path, 'r', encoding='utf-8') as resp_file:
            self.user_responses = json.load(resp_file)
        # Обновляю данные класса из загруженных ответов.
        self.username = self.user_responses.get("user_name", self.username)
        self.years = self.user_responses.get("time", self.years)
        self.gift = self.user_responses.get("item", self.gift)
        self.seating = self.user_responses.get("place", self.seating)
        
    def collect_user_input(self):
        # Спрашиваю у пользователя данные, если они не были загружены.
        if not self.username:
            self.username = input("Ваше имя: ")
        if not self.years:
            self.years = input("Сколько лет мы не виделись: ")
        if not self.gift:
            self.gift = input("Какой подарок вы хотели бы дать? ")
        if not self.seating:
            self.seating = input("Где вы хотели бы сидеть? ")

    def fill_template(self):
        # Заполняю шаблон данными.
        data = {
            "user_name": self.username,
            "time": self.years,
            "item": self.gift,
            "place": self.seating
        }
        try:
            filled_text = self.msg_template.format(**data)  # Вставляю данные в шаблон.
            return filled_text
        except KeyError as e:
            return f"Отсутствует ключ в данных шаблона: {e}"

def execute():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_file = os.path.join(current_dir, 'template.txt')
    responses_file = os.path.join(current_dir, 'Города.json')
    
    # Создаю объект класса, передавая ему все необходимые данные.
    formatter = MessageFormatter(path_to_json=responses_file, path_to_template=template_file)
    
    # Если ответы пользователя не были загружены, спрашиваю их.
    if not formatter.user_responses:
        formatter.collect_user_input()
    
    # Генерирую сообщение и показываю его пользователю.
    final_text = formatter.fill_template()
    print("Сгенерированный текст:", final_text)

if __name__ == "__main__":
    execute()  # Запускаю главную функцию, если файл запущен напрямую.
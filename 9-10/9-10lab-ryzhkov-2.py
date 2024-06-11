from jinja2 import Environment, BaseLoader

# Получение данных от пользователя
name_hero1 = input("Введите имя первого героя: ")
name_hero2 = input("Введите имя второго героя: ")
type_of_competition = input("Какой тип соревнования? ")
score_hero1 = int(input(f"Введите баллы для {name_hero1} в {type_of_competition}: "))
score_hero2 = int(input(f"Введите баллы для {name_hero2} в {type_of_competition}: "))

# Определение шаблона с использованием Jinja2
jinja_template = """
В дисциплине "{{ type_of_competition }}" соревновались: {{ name_hero1 }} против {{ name_hero2 }}.
{% if score_hero1 > score_hero2 %}
Победитель - {{ name_hero1 }} с результатом: {{ score_hero1 }}.
{% elif score_hero2 > score_hero1 %}
Победитель - {{ name_hero2 }} с результатом: {{ score_hero2 }}.
{% else %}
Результат равный! Оба участника набрали {{ score_hero1 }} очков.
{% endif %}
"""

# Создание и рендер шаблона
env = Environment(loader=BaseLoader())
template = env.from_string(jinja_template)
result = template.render(
    name_hero1=name_hero1,
    name_hero2=name_hero2,
    type_of_competition=type_of_competition,
    score_hero1=score_hero1,
    score_hero2=score_hero2
)

# Вывод результата
print(result)

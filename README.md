# Сайт Факультету соціальних наук та соціальних технологій НаУКМА

Лабораторна робота з курсу «Веб-програмування на Python» (Django).

## Сторінки

- `/`: головна сторінка (опис факультету, контакти)
- `/departments/`, `/departments/<id>/`: кафедри
- `/programs/`, `/programs/<id>/`: спеціальності
- `/exchange/`: програми академічного обміну
- `/admin/`: адмінська панель

## Запуск

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Усі дані додаються міграціями, тож після `migrate` на порожній базі сайт уже наповнений.

## Міграції

- `0001_initial`: моделі факультету
- `0002_populate_faculty_data`: наповнення кафедр, спеціальностей, дисциплін, викладачів і головної (`RunPython`)
- `0003`–`0006`: розділ програм обміну (див. `ANSWERS.md`)

## Джерела даних

- https://www.ukma.edu.ua/index.php/osvita/fakulteti/fsnst
- https://vstup.ukma.edu.ua/education-programs?level=BACHELOR

Описи дисциплін і номери семестрів складено самостійно (на сайтах їх немає), описи програм і головної переказано.
## Основы SQL ##

----

### Схема базы sql.kinopoisk ###

    position (Position)             номер в базе данных
    movie_title (Movie Title)       название фильма
    year (Year)                     год выпуска
    country (Country)               страна выпуска
    rating (Rating)                 рейтинг фильма в базе
    overview (Overview)             описание фильма
    actors (Actors)                 актёры
    director (Director)             режиссёр
    screenwriter (Screenwriter)     сценарист

----

#### **Задание 1** ####

Написать запрос, который выведет из таблицы `kinopoisk` столбцы с названием
фильма, годом его выпуска и рейтингом.

```sql
SELECT movie_title, year, rating
FROM sql.kinopoisk
```

----

#### **Задание 2** ####

Написать запрос, который выведет из таблицы `kinopoisk` следующие столбцы:

- имя режиссёра (`director`),
- название фильма (`movie_title`),
- разница между максимально возможным рейтингом (10) и рейтингом этого фильма.

```sql
SELECT director, movie_title, 10 - rating
FROM sql.kinopoisk
```

----

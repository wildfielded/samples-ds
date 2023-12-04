## Основы SQL ##

----

### Схема таблицы other.books ###

    publishing_year         INTEGER     год издания
    book_name               TEXT        название книги
    author                  TEXT        автор
    language_code           TEXT        код языка, на котором написана книга
    author_rating           TEXT        рейтинг автора
    book_average_rating     NUMERIC     средний рейтинг книги
    book_ratings_count      INTEGER     рейтинг книги
    genre                   TEXT        жанр
    publisher               TEXT        издательство
    book_id                 INTEGER     id книги

----

### Схема таблицы other.book_orders ###

----

#### **Задание 1** ####

Составить список книжных новинок. Новинками считаются все книги за последние
пять лет. Необходимые данные: название книги, год издания, автор, жанр.
Вывод отсортировать по названиям книг. При решении задачи текущим следует
считать 2021 год.

```sql
SELECT
    book_name,
    author,
    publishing_year,
    genre
FROM other.books
WHERE publishing_year >= 2016
ORDER BY book_name
```

----

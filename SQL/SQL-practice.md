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

    order_id        INTEGER     id заказа
    order_date      DATE        дата заказа
    book_id         INTEGER     id книги
    quantity        INTEGER     количество книг в заказе
    customer_id     INTEGER     id клиента
    book_name       TEXT        название книги
    author          TEXT        автор
    genre           TEXT        жанр
    sale_price      NUMERIC     цена

----

#### **Задание 09-1** ####

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

#### **Задание 09-2** ####

Отфильтровать запрос из предыдущего задания так, чтобы остались только те книги,
у которых есть название.

```sql
SELECT
    book_name,
    publishing_year,
    author,
    genre
FROM other.books
WHERE
    publishing_year >= 2016
    AND
    book_name IS NOT NULL
ORDER BY book_name
```

----

#### **Задание 09-3** ####

Выбрать значения рейтинга авторов, имеющиеся в базе.
Отсортировать вывод по алфавиту.

```sql
SELECT DISTINCT author_rating
FROM other.books
ORDER BY author_rating
```

----

#### **Задание 09-4** ####

Выбрать только книги отличных авторов&nbsp;&mdash; оставить в выборке новых книг
только авторов с рейтингом `Excellent`.

```sql
SELECT
    book_name,
    publishing_year,
    author,
    genre
FROM other.books
WHERE
    publishing_year >= 2016
    AND
    book_name IS NOT NULL
    AND
    author_rating = 'Excellent'
ORDER BY book_name
```

----

#### **Задание 09-5** ####

Добавить в имеющуюся выборку известных авторов (со значением рейтинга `Famous`).

```sql
SELECT
    book_name,
    publishing_year,
    author,
    genre
FROM other.books
WHERE
    publishing_year >= 2016
    AND
    book_name IS NOT NULL
    AND
    author_rating IN ('Excellent', 'Famous')
ORDER BY book_name
```

----

#### **Задание 09-6** ####

Определить, сколько книг из выборки попадает в каждую категорию рейтинга автора.
Понадобятся следующие данные: рейтинг автора (`author_rating`), количество книг
(`cnt`).
Сортировка по алфавиту.

```sql
SELECT
    author_rating,
    COUNT(author_rating) AS cnt
FROM other.books
WHERE
    publishing_year >= 2016
    AND
    book_name IS NOT NULL
GROUP BY author_rating
ORDER BY author_rating
```

----

#### **Задание 09-7** ####

Выбрать книги с рейтингом автора отличный (`Excellent`), известный (`Famous`) и
новый (`Novice`). И в конце добавить строку об общем количестве книг. В выборке
по-прежнему интересуют название книги, год издания, автор, жанр.

```sql
(
    SELECT
        book_name,
        publishing_year,
        author,
        genre
    FROM other.books
    WHERE
        publishing_year >= 2016
        AND
        book_name IS NOT NULL
        AND
        author_rating IN ('Excellent', 'Famous', 'Novice')
    ORDER BY book_name
)
UNION ALL
(
    SELECT
        'Total',
        COUNT(*),
        NULL,
        NULL
    FROM other.books
    WHERE
        publishing_year >= 2016
        AND
        book_name IS NOT NULL
        AND
        author_rating IN ('Excellent', 'Famous', 'Novice')
)
```

----

## Сложные объединения ##

### Схема датасета ###

![Схема датасета](schema4.png)

----

### city ###

    city_id     INTEGER     уникальный идентификатор города, первичный ключ
    city_name   TEXT        название города
    state       TEXT        штат, к которому относится город
    population  INTEGER     население города
    area        NUMERIC     площадь города

----

### customer ###

    cust_id         INTEGER     уникальный идентификатор клиента, первичный ключ
    cust_name       TEXT        название клиента
    annual_revenue  NUMERIC     ежегодная выручка
    cust_type       TEXT        тип пользователя
    address         TEXT        адрес
    zip             INTEGER     почтовый индекс
    phone           TEXT        телефон
    city_id         INTEGER     идентификатор города, внешний ключ к таблице
                                city

----

### driver ###

    driver_id       INTEGER     уникальный идентификатор водителя, первичный ключ
    first_name      TEXT        имя водителя
    last_name       TEXT        фамилия водителя
    address         TEXT        адрес водителя
    zip_code        INTEGER     почтовый индекс водителя
    phone           TEXT        телефон водителя
    city_id         INTEGER     идентификатор города водителя, внешний ключ
                                к таблице city

----

### truck ###

    truck_id    INTEGER     Уникальный идентификатор грузовика, первичный ключ
    make        TEXT        Производитель грузовика
    model_year  INTEGER     Дата выпуска грузовика

----

### shipment ###

    ship_id     INTEGER     уникальный идентификатор доставки, первичный ключ
    cust_id     INTEGER     идентификатор клиента, которому отправлена доставка,
                            внешний ключ к таблице customer
    weight      NUMERIC     вес посылки
    truck_id    INTEGER     идентификатор грузовика, на котором отправлена
                            доставка, внешний ключ к таблице truck
    driver_id   INTEGER     идентификатор водителя, который осуществлял
                            доставку, внешний ключ к таблице driver
    city_id     INTEGER     идентификатор города в который совершена доставка,
                            внешний ключ к таблице city
    ship_date   DATE        дата доставки

----

#### **Задание 1** ####

Название города с максимальным весом единичной доставки.

```sql
SELECT c.city_name
FROM sql.shipment AS s
JOIN sql.city AS c ON s.city_id = c.city_id
ORDER BY s.weight DESC
LIMIT 1
```

Сколько различных производителей грузовиков перечислено в таблице **truck**?

```sql
SELECT COUNT(DISTINCT make)
FROM sql.truck
```

Как зовут водителя (`first_name`), который совершил наибольшее количество
доставок одному клиенту?

```sql
SELECT
    d.first_name,
    COUNT(*) AS cnt
FROM sql.shipment AS s
JOIN sql.driver AS d ON s.driver_id = d.driver_id
GROUP BY s.driver_id, s.cust_id, d.first_name
ORDER BY cnt DESC
LIMIT 1
```

Имя клиента, получившего наибольшее количество доставок за 2017 год.

```sql
SELECT
    c.cust_name,
    COUNT(*) AS cnt
FROM sql.shipment AS s
JOIN sql.customer AS c ON s.cust_id = c.cust_id
WHERE s.ship_date BETWEEN '2017-01-01' AND '2017-12-31'
GROUP BY c.cust_name
ORDER BY cnt DESC
LIMIT 1
```

----

#### **Задание 2** ####

Написать запрос, который создает уникальный алфавитный справочник всех городов,
штатов, имён водителей и производителей грузовиков. Результатом запроса должны
быть два столбца: название и тип объекта (`city`, `state`, `driver`, `truck`).

Отсортировать список по названию объекта, а затем&nbsp;&mdash; по типу.

```sql
SELECT
    city_name AS object_name,
    'city' AS object_type
FROM sql.city

UNION

SELECT
    state,
    'state'
FROM sql.city

UNION

SELECT
    first_name,
    'driver'
FROM sql.driver

UNION

SELECT
    make,
    'truck'
FROM sql.truck

ORDER BY object_name, object_type
```

----

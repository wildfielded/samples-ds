## Агрегатные функции SQL ##

----

### Схема базы sql.pokemon ###

    id (ID)             уникальный идентификатор
    name (Name)         имя
    type1 (Type1)       основной тип
    type2 (TyPe2)       дополнительный тип
    hp (Hp)             количество очков здоровья
    attack (Attack)     показатели атаки
    defense (Defense)   показатели защиты
    speed (Speed)       показатели скорости

----

#### **Задание 1** ####

Написать запрос, который выведет:

- количество покемонов (столбец `pokemon_count`);
- среднюю скорость (столбец `avg_speed`);
- максимальное и минимальное число очков здоровья (столбцы `max_hp` и `min_hp`)

для электрических (`Electric`) покемонов, имеющих дополнительный тип и
показатели атаки или защиты больше 50.

```sql
SELECT
    COUNT(id) AS pokemon_count,
    AVG(speed) AS avg_speed,
    MAX(hp) AS max_hp,
    MIN(hp) AS min_hp
FROM sql.pokemon
WHERE
    type1 = 'Electric'
    AND
    type2 IS NOT NULL
    AND
    (
        attack > 50
        OR
        defense > 50
    )
```

----

#### **Задание 2** ####

Написать запрос, который выведет:

- число различных дополнительных типов (столбец `additional_types_count`);
- среднее число очков здоровья (столбец `avg_hp`);
- сумму показателей атаки (столбец `attack_sum`) в разбивке по основным типам
(столбец `primary_type`).

Отсортировать результат по числу дополнительных типов в порядке убывания, при
равенстве&nbsp;&mdash; по основному типу в алфавитном порядке.

Столбцы к выводу (обратить внимание на порядок!): `primary_type`,
`additional_types_count`, `avg_hp`, `attack_sum`.

```sql
SELECT
    DISTINCT type1 AS primary_type,
    COUNT(DISTINCT type2) AS additional_types_count,
    AVG(hp) AS avg_hp,
    SUM(attack) AS attack_sum
FROM sql.pokemon
GROUP BY primary_type
ORDER BY additional_types_count DESC,
         primary_type
```

----

#### **Задание 3** ####

Написать запрос, который выведет основной и дополнительный типы покемонов
(столбцы `primary_type` и `additional_type`) для тех типов, у которых средний
показатель атаки больше **100** и максимальный показатель очков здоровья меньше
**80**.

```sql
SELECT
    type1 AS primary_type,
    type2 AS additional_type
FROM sql.pokemon
GROUP BY primary_type, additional_type
HAVING
    (
        AVG(attack) > 100
        AND
        MAX(hp) < 80
    )
```

----

#### **Задание 4** ####

Написать запрос, который выводит столбцы с основным типом (`primary_type`) и
числом покемонов этого типа (`pokemon_count`) для тех покемонов, чьё имя
(`name`) начинается с **`S`**.    
Оставить только типы, у которых средний показатель защиты больше **80**.    
Вывести только **ТОП-3** типов по числу покемонов в них.

```sql
SELECT
    type1 AS primary_type,
    COUNT(*) AS pokemon_count
FROM sql.pokemon
WHERE name LIKE 'S%'
GROUP BY primary_type
HAVING AVG(defense) > 80
ORDER BY pokemon_count DESC
LIMIT 3
```

----

#### **Задание 5** ####

Написать запрос, который выведет основной и дополнительный типы покемонов и
средние значения по каждому показателю (столбцы `avg_hp`, `avg_attack`,
`avg_defense`, `avg_speed`).    
Оставить только те пары типов, у которых сумма этих четырёх показателей более
**400**.

```sql
SELECT
    type1,
    type2,
    AVG(hp) AS avg_hp,
    AVG(attack) AS avg_attack,
    AVG(defense) AS avg_defense,
    AVG(speed) AS avg_speed
FROM sql.pokemon
GROUP BY type1, type2
HAVING (AVG(hp) + AVG(attack) + AVG(defense) + AVG(speed)) > 400
```

----

#### **Задание 6.2** ####

Написать запрос, который выведет столбцы с основным типом покемона и общим
количеством покемонов этого типа.    
Учитывать только тех покемонов, у которых или показатель атаки, или показатель
защиты принимает значение между **50** и **100** включительно.    
Оставить только те типы покемонов, у которых максимальный показатель здоровья не
больше **125**.    
Вывести только тот тип, который находится на пятом месте по количеству
покемонов.

```sql
SELECT
    type1,
    COUNT(*)
FROM sql.pokemon
WHERE
    (attack BETWEEN 50 AND 100)
    OR
    (defense BETWEEN 50 AND 100)
GROUP BY type1
HAVING MAX(hp) < 125
ORDER BY COUNT(*) DESC
OFFSET 4
LIMIT 1
```

----

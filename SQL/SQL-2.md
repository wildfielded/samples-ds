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

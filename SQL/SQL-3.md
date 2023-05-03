## Соединение таблиц ##

### Схема базы sql.teams ###

    id          id команды
    api_id      ключ на таблицу matches
    long_name   полное название команды
    short_name  сокращённое название команды

----

### Схема базы sql.matches ###

    id                  id матча
    season              сезон
    date                дата матча
    home_team_api_id    api_id домашней команды, ключ на таблицу teams
    away_team_api_id    api_id гостевой команды, ключ на таблицу teams
    home_team_goals     количество голов домашней команды
    away_team_goals     количество голов гостевой команды

----

#### **Задание 1** ####

Написать запрос, который выведет сезон (`season`), общее количество забитых
мячей домашними (`total_home_goals`) и гостевыми (`total_away_goals`) командами.

Отсортировать по столбцу с сезоном в порядке возрастания.

```sql
SELECT
    season,
    SUM(home_team_goals) AS total_home_goals,
    SUM(away_team_goals) AS total_away_goals
FROM sql.matches
GROUP BY season
ORDER BY season
```

----

#### **Задание 2** ####

Написать запрос, который выведет количество строк соединённой таблицы (декартово
произведение таблиц).

```sql
SELECT
    COUNT(*)
FROM
    sql.teams,
    sql.matches
```

----

#### **Задание 3** ####

Написать запрос, который выведет таблицу с результатами матчей, содержащую:

- названия гостевых команд (`long_name`);
- количество забитых мячей домашней команды (`home_team_goals`);
- количество забитых мячей гостевой команды (`away_team_goals`).

```sql
SELECT
    long_name,
    home_team_goals,
    away_team_goals
FROM
    sql.teams,
    sql.matches
WHERE away_team_api_id = api_id
```

----

#### **Задание 4** ####

Переписать запрос:

```text
SELECT *
FROM sql.teams, sql.matches
WHERE away_team_api_id = api_id
```

с использованием **`JOIN`**.

```sql
SELECT *
FROM sql.teams
JOIN sql.matches ON away_team_api_id = api_id
```

----

#### **Задание 5** ####

Написать запрос, который выведет два столбца: **id** матча (`match_id`) и **id**
домашней команды (`team_id`), а затем отсортировать по **id** матча в порядке
возрастания значений.

```sql
SELECT
    m.id AS match_id,
    t.id AS team_id
FROM sql.teams AS t
JOIN sql.matches AS m ON m.home_team_api_id = t.api_id
ORDER BY match_id
```

----

#### **Задание 6** ####

Написать запрос, который выведет столбцы: **id** матча, короткое название
домашней команды (`home_short`), короткое название гостевой команды
(`away_short`). Отсортировать запрос по возрастанию **id** матча.

```sql
SELECT
    m.id,
    h.short_name AS home_short,
    a.short_name AS away_short
FROM sql.matches AS m
JOIN sql.teams AS h ON m.home_team_api_id = h.api_id
JOIN sql.teams AS a ON m.away_team_api_id = a.api_id
ORDER BY m.id
```

----

#### **Задание 7** ####

Написать запрос, который выведет полное название команды (`long_name`),
количество голов домашней команды (`home_goal`) и количество голов гостевой
команды (`away_goal`) в матчах, где домашней командой были команды с коротким
названием **`GEN`**. Отсортировать запрос по **id** матча в порядке возрастания.

```sql
SELECT
    t.long_name,
    m.home_team_goals AS home_goal,
    m.away_team_goals AS away_goal
FROM sql.teams AS t
JOIN sql.matches AS m ON m.home_team_api_id = t.api_id
WHERE t.short_name = 'GEN'
ORDER BY m.id
```

----

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

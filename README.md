# FBreacking_News
Simple project for creating ang watchind news


Проект подготовлен в соответствии с тестовым заданием на вакансию junior python-разработчик. Проект представляет собой простой сервис API для создания и чтения новостей.


[Доступные эндпоинты]:
- **auth/** - Получение токена. POST-запрос. В теле запроса 2 поля: username, password.
- **auth/users/** — Получение списка пользователей и регистрация пользователей

*Типы запросов*:

        GET(для авторизованных),
	
        POST(для администраторов)
- **news/** - Просмотр всех новостей, добавление новости.

*Типы запросов*: 

        GET(для всех пользователей),
	
        POST, PUT, PATCH, DELETE(для администраторов)
	
- **news/{id}** — Просмотр новости с указанным id. Изменение новости.

        GET(для всех пользователей)
	
        PATCH, PUT, DELETE(для администраторов)


*PS: Отделение пользователей админки сайта от таблицы Users.
	Данная практика не рекомендуется в сообществе, так как при расширении проекта могут возникнуть определенные проблемы с правами доступа, изменением моделей и согласованием данных в моделях. Я понимаю, что можно создать две отдельные модели для пользователей с разными правами доступа к админке сайта, регистрировать администраторов отдельно от пользователей. Однако, полагаю, что изменение модели Users с предоставлением разных ролей пользователям (модератор, админ и т.д.) было бы более рациональным решением.*

# Финальный проект курса QA
## SQL скрипты:
1. Вывод списка логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 
```
SELECT c.login, COUNT(o.id) AS "deliveryCount" FROM "Couriers" AS c LEFT JOIN "Orders" AS o ON c.id = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;
```
2. Вывод всех треков заказов и их статусов.
```
SELECT o.track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END AS state FROM "Orders" AS o;
```
# Тесты на проверку добавления заказа в Яндекс.Самокат с помощью API Яндекс.Самокат.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest
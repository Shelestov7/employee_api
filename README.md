# Employee_API

[badge](https://github.com/Shelestov7/employee_api/workflows/employee_api_workflow/badge.svg)

## Описание 
API сервис для получения списка сотрудников по следующимм параметрам:

 * name
 * company
 * gender
 * age
 * salary
 * job_title
 
Пример запроса `http://0.0.0.0:8090/get_employee/?gender=male&company=Google&job_title=manager`
## Этапы развертывания Docker контейнера 
1. Склонировать репозиторий 
  
2. Выполнить команду `docker-compose up` 

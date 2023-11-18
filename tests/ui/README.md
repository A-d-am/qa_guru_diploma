# Пример проекта автотестов для компании [LiteFinance](https://www.litefinance.org)
>LiteFinance (ex. LiteForex) это высокотехнологичный и надежный ECN брокер
> с проверенной годами репутацией. Клиенты LiteFinance (ex. LiteForex) 
>получают доступ к безопасному онлайн терминалу с интуитивно понятным
> интерфейсом на 15 языках мира, поддерживающему высокоскоростную 
> торговлю и огромное количество встроенных инструментов для анализа 
> ценового графика. Для поклонников самой популярной торговой платформы
> также доступен MetaTrader 4/5.

###  Используемые технологии
<p align="center">
  <code><img src="images/logo/python.svg" width="40" height="40"  alt="A-d-am" title="Python"></code>
  <code><img src="images/logo/pytest.png" width="40" height="40"  alt="A-d-am" title="PyTest"></code>
  <code><img src="images/logo/selene.png" width="40" height="40"  alt="A-d-am" title="Selene"></code>
  <code><img src="images/logo/pycharm.png" width="40" height="40"  alt="A-d-am" title="PyCharm"></code>
  <code><img src="images/logo/Jenkins.svg" width="40" height="40"  alt="A-d-am" title="Jenkins"></code>
  <code><img src="images/logo/Selenoid.svg" width="40" height="40"  alt="A-d-am" title="Selenoid"></code>
  <code><img src="images/logo/Allure_new.png" width="40" height="40"  alt="A-d-am" title="Allure Report"></code>
  <code><img src="images/logo/allure_testops.png" width="40" height="40"  alt="A-d-am" title="Allure TestOps"></code>
  <code><img src="images/logo/Telegram.svg" width="40" height="40"  alt="A-d-am" title="Telegram Bot"></code>
  <code><img src="images/logo/Jira.svg" width="40" height="40"  alt="A-d-am" title="Jira"></code>
</p>

## Покрываемый функционал
- Авторизация пользователя 
- Проверка валидации полей логина
- Проверка возможности сбросить пароль


## Запуск тестов
#### Все UI тесты запускаются удалённо на Selenoid, но их можно запустить и локально

### Локально
Важно! Перед запском нужно создать файл .env.selenoid_credentials и указать там selenoid_login 
и selenoid password

Для запуска тестов локально, нужно выполнить следующие шаги
1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Ввести в териминале следующие команды
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
context=web pytest -m web  
```

### С помощью [Jenkins](https://jenkins.autotests.cloud/job/C07_suprun_diploma/)
#### Для запуска автотестов необходимо:
 - Открыть [джобу](https://jenkins.autotests.cloud/job/C07_suprun_diploma/) в jenkins
 - Нажать на кнопку Build with Parameters
 - Выбрать необходимые значения параметров TESTS_TYPE и CONTEXT согласно инструкции 
 - Нажать на Build

## Отчет о прохождении тестов (Allure)
### Локально
Для получения отчета нужно ввести команду 
```
allure serve allure-results
``` 
Ниже представлен пример allure отчета 
<img src="images/screenshots/allure_report_example_web.png">

Подробные инструкции по работе с allure можно найти по [ссылке](https://allurereport.org/docs/).
### Если тесты запускались в Jenkins

Для получения отчета нужно нажать на иконку allure report'a в строке билда  
У него будет точно такой же формат, как и при получении локально
<img src="images/screenshots/allure_report_from_jenkins.png">

### В проекте реализована интеграция с Allure TestsOps
<img src="images/screenshots/allure_test_ops.png">

### В проекте настроена отправка краткого отчета в Telegram
<img src="images/screenshots/tg_web_allure.png">

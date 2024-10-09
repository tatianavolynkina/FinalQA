# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data
from data import headers

def post_new_order(order_data):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_data,
                         headers=data.headers)

def get_order(order_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_PATH,
                        params={"t": order_id})
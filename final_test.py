# Татьяна Волынкина, 22-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

# Тест 1
# В тесте проверяется создание заказа.
def test_create_order():
    order_body = data.new_order_data.copy()
    response = sender_stand_request.post_new_order(order_body)
    assert response.status_code == 201
    assert response.json()["track"]
    data.track_index = response.json()["track"]

# Тест 2
# В тесте возможность получения информации о заказе по его трек-номеру
def test_get_order_info():
    order_body = data.new_order_data.copy()
    response = sender_stand_request.post_new_order(order_body)
    track_index = response.json()["track"]
    response = sender_stand_request.get_order(track_index)
    assert response.status_code == 200
    assert response.json()["order"]["track"] == track_index
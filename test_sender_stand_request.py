## Дмитрий Маслов, 18-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

# создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         headers=data.headers,
                         json=order_body)

# получение заказа по номеру трекера
def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER + '?t=' + str(track),
                        headers=data.headers)
def test_order_can_be_retrieved_by_track_number():
    order_body = data.order_body
    resp_json = post_new_order(order_body).json()
    track_id = resp_json["track"]

    resp = get_order_track(track_id)

    assert resp.status_code == 200
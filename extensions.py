import requests
import json
from ConfigToken import keys


class ConvertionException(Exception):
    pass


class Cryptoconverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:  # проверка на ввод двух одинаковых валют - не конвертируем одну и туже валюту
            raise ConvertionException('Невозможно перевести одинаковые валюты {base}') # текст для пользователя

        try:
            quote_ticker = keys[quote]
        except KeyError:  # если не правильно введено название валюты, из которой будем конвертировать
            raise ConvertionException(f'Не удалось обработать валюту {quote}') # текст для пользователя

        try:
            base_ticker = keys[base]
        except KeyError:  # если не правильно введено название валюты, в которую будем конвертируем
            raise ConvertionException(f'Не удалось обработать валюту {base}') # текст для пользователя

        try:
            amount = float(amount)
        except ValueError:  # проверяем, что количество валюты введено правильно, то есть цифрами
            raise ConvertionException(f'Не удалось обработать количество {amount}') # текст для пользователя
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base

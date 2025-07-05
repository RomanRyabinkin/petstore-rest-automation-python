"""
Модуль client: предоставляет класс ApiClient для взаимодействия с REST API Swagger Petstore,
включая методы запросов и валидацию по JSON Schema.
"""



from typing import Any, Dict, Optional

import yaml, requests
from jsonschema import validate

with open('config.yaml') as f:
    _config = yaml.safe_load(f)


class ApiClient:
    """
    HTTP клиент для работы с API Swagger Petstore

    Attributes:
        base (str): Базовый URL для API эндпоинтов
        timeout (int): Время ожидания ответа (в секундах)
    """

    def __init__(self):
        self.base = _config['api']['base_url'].rstrip('/')
        self.timeout = _config['api']['timeout']

    def _url(self, path: str): return f"{self.base}/{path.lstrip('/')}"
    """
    Формирование полного URL запароса. 
    Объединяет базовый URL и путь к эндпоинту запроса.
    
    Args:
        path (str): Путь к эндпоинту запроса. Может начинаться с /

    Returns:
        str: Полный URL запроса
    """

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.get(self._url(path), timeout=self.timeout, **kwargs)

    """
       Выполнение GET-запроса.

       Аrgs:
           path (str): Путь к эндпоинту для GET.
           **kwargs: Дополнительные параметры для requests.get.

       Returns:
           requests.Response: Объект HTTP-ответа.
       """

    def post(self, path: str, json: Optional[Dict[str, Any]] = None, **kwargs: Any) -> requests.Response:
        return requests.post(self._url(path), json=json, timeout=self.timeout, **kwargs)

    """
    Выполнение POST-запроса с JSON-телом запроса.

    Args:
        path (str): Путь к эндпоинту для POST.
        json (dict, optional): JSON-payload для отправки запроса.
        **kwargs: Дополнительные параметры для requests.post.

    Returns:
        requests.Response: Объект HTTP-ответа.
    """

    def put(self, path: str, json: Optional[Dict[str, Any]], **kwargs: Any) -> requests.Response:
        return requests.put(self._url(path), json=json, timeout=self.timeout, **kwargs)

    """
    Выполнение PUT-запроса с JSON-телом запроса.

    Args:
        path (str): Путь к эндпоинту для PUT.
        json (dict, optional): JSON-payload для отправки запроса.
        **kwargs: Дополнительные параметры для requests.put.

    Returns:
        requests.Response: Объект HTTP-ответа.
    """

    def delete(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.delete(self._url(path), timeout=self.timeout, **kwargs)

    """
    Выполнение DELETE-запроса.

    Args:
        path (str): Путь к эндпоинту для DELETE запроса.
        **kwargs: Дополнительные параметры для requests.delete.

    Возвращает:
        requests.Response: Объект HTTP-ответа.
    """

    @staticmethod
    def validate(response: requests.Response, schema_file: str):

        """
        Проверка валидации JSON-ответа запроса по JSON Schema.

        Args:
            response (requests.Response): Проверяемый HTTP-ответ запроса.
            schema_file (str): Имя файла JSON Schema в директории src/schemas/.

        Exceptions:
            jsonschema.exceptions.ValidationError: при ошибке валидации.
        """

        schema_path: str = f"src/schemas/{schema_file}"
        with open(schema_path, 'r') as _f:
            schema: Dict[str, Any] = yaml.safe_load(_f)
        validate(instance=response.json(), schema=schema)


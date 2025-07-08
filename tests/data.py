DEFAULT_USER = {
    'id': 5001,
    'username': 'test_user_roman',
    'firstName': 'Roman',
    'lastName': 'Ryabinkin',
    'email': 'test@example.com',
    'password': 'password',
    'phone': '1234567890',
    'userStatus': 1,
}

DEFAULT_ORDER = {
    'id': 3001,
    'petId': 1002,
    'quantity': 2,
    'shipDate': '2025-07-01T12:00:00.000Z',
    'status': 'placed',
    'complete': True
}


def make_user(**overrides):

    """
    Возвращает новый словарь user, скопированный из DEFAULT_USER,
    с возможностью переопределить отдельные поля.
    """

    user = DEFAULT_USER.copy()
    user.update(overrides)
    return user


def make_order(**overrides):

    """
    Возвращает новый словарь order, скопированный из DEFAULT_ORDER,
    с возможностью переопределить отдельные поля.
    """

    order = DEFAULT_ORDER.copy()
    order.update(overrides)
    return order

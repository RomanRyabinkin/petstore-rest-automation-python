import yaml
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker

from config import config

db_url = config["db"]["url"]
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)

metadata = MetaData()


def get_pet_by_id(pet_id: int):

    """
    Получить запись о питомце из базы данных по его ID.

    Args:
        pet_id (int): Уникальный идентификатор питомца.

    Returns:
        sqlalchemy.engine.Row | None: Объект Row с данными питомца или None, если запись не найдена.
    """

    try:
        pet_table = Table('pet', metadata, autoload_with=engine)
    except OperationalError as e:
        raise ConnectionError(f"Не удалось подключиться к БД: {e}")
    session = Session()
    try:
        return session.query(pet_table).filter_by(id=pet_id).first()
    finally:
        session.close()

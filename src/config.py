from pathlib import Path
from typing import Dict, Any

import yaml


def _load_config() -> Dict[str, Any]:
    """
    Загружает конфигурацию из файла config.yaml в корне проекта.

    Returns:
        dict: Данные конфигурации.
    """
    base_dir = Path(__file__).resolve().parents[1]
    config_path = base_dir / 'config.yaml'
    if not config_path.exists():
        raise FileNotFoundError(f'Не найден файл конфигурации: {config_path}')
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


config = _load_config()
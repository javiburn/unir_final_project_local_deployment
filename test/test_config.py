import pytest

import sys
import os

# Agrega la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.config import TestingConfig

def test_config_class():
    config = TestingConfig()
    assert config.SECRET_KEY is not None
    assert config.SQLALCHEMY_DATABASE_URI is not None
    assert config.SQLALCHEMY_TRACK_MODIFICATIONS is False
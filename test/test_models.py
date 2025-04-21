import pytest

import sys
import os

# Agrega la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import Data

def test_db_creation():
    data = Data(name="Test Data")
    assert data.name == "Test Data"
    assert str(data) == "<Data id=None name=Test Data>"
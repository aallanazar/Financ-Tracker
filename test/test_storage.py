import json
import os
from storage import load_expenses, save_expenses, FILENAME


def test_load_expenses_when_file_does_not_exist():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    assert load_expenses() == []
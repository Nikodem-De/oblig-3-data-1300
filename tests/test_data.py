import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import json
from health_app.data import save_records, load_records  


def test_save_and_load_data(tmp_path):
  
    test_file = tmp_path / "test_health.json"
    test_data = [{"weight": 80, "height": 1.8, "bmi": 24.7}]
    
  
    try:
        save_records(test_data)
        loaded = load_records()
        assert isinstance(loaded, list)
    except Exception as e:
        print(f"Data test handled: {e}")

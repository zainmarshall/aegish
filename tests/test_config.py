import os
import tempfile
import json
from aegish.config import load_config, save_config

def test_save_and_load_config():
    # Use a temp file for config
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        path = tf.name
    try:
        config = {"provider": "gemini", "model": {"api": "gemini-2.5-pro", "name": "Gemini 2.5 Pro"}}
        save_config(config)
        loaded = load_config()
        assert loaded["provider"] == "gemini"
        assert loaded["model"]["api"] == "gemini-2.5-pro"
    finally:
        os.remove(path)

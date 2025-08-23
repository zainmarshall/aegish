from aegish.gemini import GeminiHandler
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_gemini_handler():
    handler = GeminiHandler()
    # if handler returns anything at all pass the test
    assert handler is not None
    response = handler.generate("echo Hello World")
    assert response is not None

from aegish.gemini import GeminiHandler

def test_gemini_handler():
    handler = GeminiHandler()
    # if handler returns anything at all pass the test
    assert handler is not None
    response = handler.generate("echo Hello World")
    assert response is not None

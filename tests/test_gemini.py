import pytest
from unittest.mock import patch, MagicMock
from aegish.Handlers.gemini import GeminiHandler

def test_gemini_generate_returns_text():
    handler = GeminiHandler()
    with patch.object(handler.client.models, 'generate_content', return_value=MagicMock(text='ls -lah')) as mock_gen:
        result = handler.generate('List files')
        assert result == 'ls -lah'
        mock_gen.assert_called()

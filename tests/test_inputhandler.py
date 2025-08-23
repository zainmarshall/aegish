import sys
import pytest
from unittest import mock
from aegish.inputhandler import InputHandler

def test_get_with_text(monkeypatch):
    test_args = ["prog", "echo", "hello"]
    monkeypatch.setattr(sys, "argv", test_args)
    args, user_prompt = InputHandler.get()
    assert user_prompt == "echo hello"
    assert not args.print_only
    assert not args.no_safety

def test_get_with_print_only(monkeypatch):
    test_args = ["prog", "ls", "-l", "--print-only"]
    monkeypatch.setattr(sys, "argv", test_args)
    args, user_prompt = InputHandler.get()
    assert user_prompt == "ls -l"
    assert args.print_only

def test_get_no_input(monkeypatch):
    test_args = ["prog"]
    monkeypatch.setattr(sys, "argv", test_args)
    with mock.patch("sys.stdin.read", return_value=""):  # Simulate no stdin
        with pytest.raises(SystemExit):
            InputHandler.get()

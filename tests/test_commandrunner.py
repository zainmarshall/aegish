import pytest
from aegish.commandrunner import CommandRunner
import io
import sys

def test_commandrunner_echo():
    runner = CommandRunner()
    captured_out = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = captured_out
    runner.run('echo Hello World')
    sys.stdout = sys_stdout
    output = captured_out.getvalue()
    assert 'Hello World' in output

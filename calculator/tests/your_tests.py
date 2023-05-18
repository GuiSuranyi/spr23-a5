#!/usr/bin/env python3
from calculator_adapter import run

assert run("5/5").output == "1"
assert run("5/5").exit_status == 0
###
assert run("5!1").exit_status != 0
assert run("5-4").output == "1"

###

print("All tests passed!")

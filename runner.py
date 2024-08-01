import subprocess
import time
import pytest

class CommandRunner:
    def __init__(self, command):
        self.process = subprocess.Popen(
            command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

    def run_command(self, commands):
        for input in commands:
            self.process.stdin.write(input + "\n")
            self.process.stdin.flush()
            time.sleep(0.1)

        output = []
        while True:
            text = self.process.stdout.readline()

            if text.strip() == "***":
                break

            if "Enter here: " in text:
                text = text.replace("Enter here: ", "")

            output.append(text.strip())
        return output

    def terminate(self):
        self.process.terminate()
        self.process.wait()

@pytest.fixture(scope="module")
def command_runner():
    command = ['./bin/InventoryMgmt']
    runner = CommandRunner(command)
    yield runner
    runner.terminate()

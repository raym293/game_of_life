import subprocess
import sys

subprocess.Popen([
    "open", "-a", "Terminal",
    sys.executable,  # Python executable
    "hello_world.py"        # Your script
])

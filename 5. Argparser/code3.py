import argparse
import sys

# Create the argument parser
parser = argparse.ArgumentParser(description="Example script for parse_known_args")

# Add expected arguments
parser.add_argument('--name', type=str, help='Your name')
parser.add_argument('--age', type=int, help='Your age')

# Use parse_known_args instead of parse_args
known_args, unknown_args = parser.parse_known_args()

# known_args contains only the known arguments
print(f"Known args: {known_args}")

# unknown_args contains the unknown arguments
print(f"Unknown args: {unknown_args}")

print(sys.argv)

# If you run below command you will --runner as unknown args and --name as known argsn
"""
```bash
python code3.py --runner=Dataflow --name=SALMAN
```

```bash
Known args: Namespace(name='SALMAN', age=None)
Unknown args: ['--runner=Dataflow']
['code3.py', '--runner=Dataflow', '--name=SALMAN']
```
"""
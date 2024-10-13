## **Argument Passing**

>This code will print name of python file as it is stored in argv variable.
```python
import sys
print(sys.argv[0])
print(len(sys.argv[0]))
```
Output

```bash
code.py
7
```

> If we run the above python code python shell then we will have empty string output for above code.\

> Simmilarly if we run this code using -c command is used, sys.argv[0] is set to '-c'.

```bash
python -c "import sys; print(sys.argv)"
```
Output
```bash
['-c']
```

>When -m module is used, sys.argv[0] is set to the full name of the located module.

Options found after -c command or -m module are not consumed by the Python interpreter’s option processing but left in sys.argv for the command or module to handle.

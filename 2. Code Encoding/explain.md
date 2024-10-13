## **Source Code Encoding**

Python source files by default are treated as encoded in **UTF-8**. 


In this characters of most languages in the world can be used simultaneously in string literals, identifiers and comments.\
Standard library only uses ASCII characters for identifiers.

For other use cases we can use emoji & other language charactors and that will encoded using UTF-8.

>Keywords 
```python
class
def
int #This not keyword
import
```

>String literals

```python
"This is single line string"

"""
this is multiline string
this is multiline string
"""
```

>identifiers

Name of the variable or function

```python
class myClass 
```
*myClass* is identifier

```python
x=10

def myFunction():
    return None
```
 
x and myFunction are identifier

>Rules for identifier
1.  consist of Letters, digits, and underscores
2.  CanNot Start with DIGIT.
3.  Case Senitive i.e  myclass != myClass
4.  No Space or special char i.e Var 1, Var@1
5.  No Keywords class,def,int

-----

### Other encoding

For other encoding special comment line should be added as the first line

**encoding** is one of the valid codecs supported by Python.

```python
# -*- coding: encoding -*-
```

>Exception

One exception to the first line rule is when the source code starts with a UNIX “shebang” line.

It is first line of the script which tells operating system which interpeter to use.

```python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```

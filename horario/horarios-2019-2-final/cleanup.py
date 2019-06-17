import re, sys

eng = re.compile(r'<tr>\n.*\n.*---.*\n.*---.*\n.*---.*\n.*---.*\n.*---.*\n.*<\/tr>')

data = ""

with open(sys.argv[1], 'r') as f:
    data = f.read()


data = eng.sub("", data)

with open(sys.argv[1], 'w') as f:
    f.write(data)




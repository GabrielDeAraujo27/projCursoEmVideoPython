C1 = None
C2 = None
C3 = None
C_5Bi_1_5D = None
C_5Bi_1_5D2 = None
C_5Bi_2_5D = None
C_5Bi_5D = None
C_5Bj_5D = None
i = None
j = None
r = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())

def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)


r = read_integer()
C1 = 0
C2 = 1
for i in (1 <= float(r)) and upRange(1, float(r), 1) or downRange(1, float(r), 1):
  print(C1)
  C3 = C1
  C1 = C2
  C2 = C3 + C2

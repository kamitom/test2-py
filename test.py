

import datetime
import random
from openpyxl import Workbook

wb2 = Workbook()

ws = wb2.active

ws['C1'] = random.random()
ws['A1'] = random.random()

# TypeError: unsupported operand type(s) for *: 'Cell' and 'Cell'
ws['A5'] = 100 + 2


# ws.append([1, 2, 3])

# ws['A2'] = datetime.datetime.now()

fname = random.randint(1, 1000)
print(type(fname))
print(fname)

filename = str(fname) + ".xlsx"

wb2.save(filename)

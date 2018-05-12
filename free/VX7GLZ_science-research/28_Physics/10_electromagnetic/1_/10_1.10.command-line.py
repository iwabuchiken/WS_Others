#------------------------------------------------------- try : 1
import matplotlib.pyplot as plt
import numpy as np

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

# plt.plot(x1, y1, marker = 'o')

handles, labels = ax.get_legend_handles_labels()

print(handles)

# ax.legend(handles, labels)
plt.legend()

plt.plot(x1, y1, marker = 'o')

handles, labels = ax.get_legend_handles_labels()
print(handles)

#-------------------------------------------------------
plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

# plt.plot(x1, y1, marker = 'o')

result = plt.plot(x1, y1, marker = 'o')
# handle_X1Y1, = plt.plot(x1, y1, marker = 'o')

print("result =>")
print(result)

#-------------------------------------------------------
plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1 = [A[0], C[0]]
# x1, y1 = [A[0], C[0], A[0], B[0]], \
#             [A[1], C[1], A[1], B[1]]


# plt.plot(x1, y1, marker = 'o')

result = plt.plot(x1, marker = 'o', label="AC")
# result = plt.plot(x1, marker = 'o')
# result = plt.plot(x1, y1, marker = 'o')
# handle_X1Y1, = plt.plot(x1, y1, marker = 'o')

print("result =>")
print(result)

#-------------------------------------------------------
plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1 = [A[0], C[0]]
# x1, y1 = [A[0], C[0], A[0], B[0]], \
#             [A[1], C[1], A[1], B[1]]


# plt.plot(x1, y1, marker = 'o')

result = plt.plot(x1, marker = 'o', label="AC")
# result = plt.plot(x1, marker = 'o', label="AC")
# result = plt.plot(x1, marker = 'o')
# result = plt.plot(x1, y1, marker = 'o')
# handle_X1Y1, = plt.plot(x1, y1, marker = 'o')

print("result =>")
print(result)

#-------------------------------------------------------
plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1 = [A[0], C[0]]
# x1, y1 = [A[0], C[0], A[0], B[0]], \
#             [A[1], C[1], A[1], B[1]]


# plt.plot(x1, y1, marker = 'o')

result = plt.plot(x1, marker = 'o', label="AC")
# result = plt.plot(x1, marker = 'o', label="AC")
# result = plt.plot(x1, marker = 'o')
# result = plt.plot(x1, y1, marker = 'o')
# handle_X1Y1, = plt.plot(x1, y1, marker = 'o')

# print("result =>")
# print(result)

#ref legend https://matplotlib.org/examples/statistics/histogram_demo_cumulative.html
plt.legend(loc='right')

#------------------------------------------------------- try : 7
import matplotlib.pyplot as plt
import numpy as np

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

plt.plot(x1, marker = 'o', label="AC")
# plt.plot(y1, marker = '*', label="AB")

plt.legend('right')

#------------------------------------------------------- try : 7.1
import matplotlib.pyplot as plt
import numpy as np

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

plt.plot(x1, marker = 'o', label="AC")
# plt.plot(y1, marker = '*', label="AB")

plt.legend('right')

#------------------------------------------------------- try : 8
#ref https://matplotlib.org/examples/pylab_examples/coords_report.html
import matplotlib.pyplot as plt
import numpy as np


def millions(x):
    return '$%1.1fM' % (x*1e-6)

x = np.random.rand(20)
y = 1e7*np.random.rand(20)

fig, ax = plt.subplots()
ax.fmt_ydata = millions
# plt.plot(x, label="test1", y, 'o')    #=> SyntaxError: positional argument follows keyword argument
# plt.plot(x, y, 'o', label="test1")
plt.plot(x, y, 'o')

plt.legend('aaa')
# plt.legend('right')

xx = np.random.rand(20)
yy = 1e7*np.random.rand(20)
plt.plot(xx, yy, 'o')
plt.legend('b')


plt.show()

#------------------------------------------------------- try : 9
#ref http://paper.hatenadiary.jp/entry/2017/05/02/152223
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from sklearn.datasets import make_moons

data, label = make_moons(noise=0.2, n_samples=2000)
x0, y0 = data[label==0,0], data[label==0,1]
x1, y1 = data[label==1,0], data[label==1,1]
x2, y2 = -1*data[label==1,0], 2*data[label==1,1]

plt.title("moon")
plt.scatter(x0, y0, label="label-A")
plt.scatter(x1, y1, label="label-B")

plt.xlabel("X-LABEL")
plt.xlabel("Y-LABEL")
plt.legend()

#------------------------------------------------------- try : 9.1
#ref http://paper.hatenadiary.jp/entry/2017/05/02/152223
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from sklearn.datasets import make_moons

data, label = make_moons(noise=0.2, n_samples=2000)
x0, y0 = data[label==0,0], data[label==0,1]
x1, y1 = data[label==1,0], data[label==1,1]
x2, y2 = -1*data[label==1,0], 2*data[label==1,1]

plt.title("moon")
plt.scatter(x0, y0, label="label-A", marker='*')
# plt.scatter(x0, y0, label="label-A", marker='o')
plt.scatter(x1, y1, label="label-B")
# plt.scatter(x0, y0, label="label-A")
# plt.scatter(x1, y1, label="label-B")

plt.xlabel("X-LABEL")
plt.xlabel("Y-LABEL")
plt.legend()

#------------------------------------------------------- try : 7.2
import matplotlib.pyplot as plt
import numpy as np

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

plt.plot(x1, y1, marker = 'o', label="AC")
# plt.plot(x1, marker = 'o', label="AC")
# plt.plot(y1, marker = '*', label="AB")

plt.legend()
# plt.legend('right')

#------------------------------------------------------- try : 7.3
import matplotlib.pyplot as plt
import numpy as np

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

plt.plot(x1, y1, marker = 'o')
# plt.plot(x1, y1, marker = 'o', label="AC")
# plt.plot(x1, marker = 'o', label="AC")
# plt.plot(y1, marker = '*', label="AB")

plt.legend()
# plt.legend('right')

#------------------------------------------------------- try : 7.4
import matplotlib.pyplot as plt
import numpy as np

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

plt.plot(x1, y1, label='abc', marker = 'o')
# plt.plot(x1, y1, marker = 'o')
# plt.plot(x1, y1, marker = 'o', label="AC")
# plt.plot(x1, marker = 'o', label="AC")
# plt.plot(y1, marker = '*', label="AB")

plt.legend()
# plt.legend('right')

#------------------------------------------------------- try : 7.5
import matplotlib.pyplot as plt
import numpy as np

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

plt.plot(x1, y1, label="abc", marker = 'o')
# plt.plot(x1, y1, label='abc', marker = 'o')
# plt.plot(x1, y1, marker = 'o')
# plt.plot(x1, y1, marker = 'o', label="AC")
# plt.plot(x1, marker = 'o', label="AC")
# plt.plot(y1, marker = '*', label="AB")

plt.legend()
# plt.legend('right')

#------------------------------------------------------- try : 7.6
import matplotlib.pyplot as plt
import numpy as np

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

plt.plot(x1, y1, marker = 'o', label="abc")
# plt.plot(x1, y1, label="abc", marker = 'o')
# plt.plot(x1, y1, label='abc', marker = 'o')
# plt.plot(x1, y1, marker = 'o')
# plt.plot(x1, y1, marker = 'o', label="AC")
# plt.plot(x1, marker = 'o', label="AC")
# plt.plot(y1, marker = '*', label="AB")

plt.legend()
# plt.legend('right')

#------------------------------------------------------- try : 7.7
import matplotlib.pyplot as plt
import numpy as np

plt.clf()

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

plt.plot(x1, y1, label="abc", marker = 'o')
# plt.plot(x1, y1, label='abc', marker = 'o')
# plt.plot(x1, y1, marker = 'o')
# plt.plot(x1, y1, marker = 'o', label="AC")
# plt.plot(x1, marker = 'o', label="AC")
# plt.plot(y1, marker = '*', label="AB")

plt.legend()
# plt.legend('right')

#------------------------------------------------------- try : 7.8
import matplotlib.pyplot as plt
import numpy as np

plt.clf()

plt.grid(b=None, which='major', axis='both')
ax = plt.gca()

e = 1
r = 2

th = np.pi / 4

A = [0, 0]
B = [e, 0]
C = [r * np.cos(th), r * np.sin(th)]
D = [e + r * np.cos(th), r * np.sin(th)]
E = [0                  , - r * np.cos(th)]
F = [e                  , - r * np.cos(th)]


# AC, AB
x1, y1 = [A[0], C[0], A[0], B[0]], \
            [A[1], C[1], A[1], B[1]]

plt.plot(x1, y1, marker = 'o', label="AC AB")
# plt.plot(x1, y1, marker = 'o', label="abc")
# plt.plot(x1, y1, label="abc", marker = 'o')
# plt.plot(x1, y1, label='abc', marker = 'o')
# plt.plot(x1, y1, marker = 'o')
# plt.plot(x1, y1, marker = 'o', label="AC")
# plt.plot(x1, marker = 'o', label="AC")
# plt.plot(y1, marker = '*', label="AB")

plt.legend()
# plt.legend('right')


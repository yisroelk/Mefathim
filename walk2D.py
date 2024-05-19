import random
import plotly.graph_objects as go # type: ignore
import numpy as np
import plotly.express as px

x = [0]
y = [0]


current_x = 0
current_y = 0

for i in range(50):
    step = random.randint(0,1)*2-1
    if random.random() > .5:
        current_x += step
    else:
        current_y += step

    x.append(current_x)
    y.append(current_y)

t = list(range(len(y)))

#x, y, z = x2, y2, t
fig = px.line_3d(x=x, y=y, z=t)
fig.show()
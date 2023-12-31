import plotly.graph_objects as go

# Define coordinates
x = [0, 125, 135, 150,
     0, 125, 135, 150,
     0, 125, 125, 0,
     0, 125, 125, 0,
     0, 150, 135, 125,
     0, 150, 135, 125,
     135, 150, 150, 135,
     135, 150, 150, 135,
     125, 135, 135, 125,
     125, 135, 135, 125,
     150, 150, 150, 150,
     125, 125, 135, 135]
y = [18, 15, 15, 18,
     18, 15, 15, 18,
     0, 5, 15, 18,
     0, 5, 15, 18,
     0, 0, 5, 5,
     0, 0, 5, 5,
     5, 0, 18, 15,
     15, 18, 18, 15,
     8, 8, 12, 12,
     8, 8, 12, 12]
z = [-0.1, -0.1, -0.1, -0.1,
     0.1, 0.1, 0.1, 0.1,
     -0.1, -0.1, -0.1, -0.1,
     0.1, 0.1, 0.1, 0.1,
     -0.1, -0.1, -0.1, -0.1,
     0.1, 0.1, 0.1, 0.1,
     -0.1, -0.1, -0.1, -0.1,
     0.1, 0.1, 0.1, 0.1,
     -0.1, -0.1, -0.1, -0.1,
     0.1, 0.1, 0.1, 0.1,]

fig = go.Figure(data=[go.Scatter3d(x=x,y=y,z=z,mode='lines+markers')])
fig.show()

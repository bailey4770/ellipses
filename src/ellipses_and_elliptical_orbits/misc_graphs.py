import numpy as np
import plotly.graph_objects as go
from pathlib import Path


def main():
    E = np.linspace(0, 2 * np.pi, 400)
    e = 0.7
    M = 1  # 0 <= M <= 2 * pi

    f_E = E - e * np.sin(E) - M

    fig = go.Figure()
    _ = fig.add_trace(go.Scatter(x=E, y=f_E, mode="lines"))
    _ = fig.add_shape(
        type="line", x0=0, y0=0, x1=2 * np.pi, y1=0, line=dict(color="black")
    )
    _ = fig.update_layout(
        xaxis_title="E (eccentric anomaly)",
        yaxis_title="f(E)",
    )
    fig.write_image(Path("assets/img/f_E.png"))


if __name__ == "__main__":
    main()

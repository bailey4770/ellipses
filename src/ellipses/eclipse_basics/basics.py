import numpy as np
import plotly.graph_objects as go
from pathlib import Path

from ellipses.utils import (
    calculate_coordinates,
    calculate_focus_offset,
    calculate_semi_minor_axis,
)


def rotate_ellipse(coords: np.ndarray, i: float) -> np.ndarray:
    rotation_matrix = [[1, 0, 0], [0, np.cos(i), -np.sin(i)], [0, np.sin(i), np.cos(i)]]
    return rotation_matrix @ coords


def add_sphere(fig: go.Figure, z_offset: float, color: str) -> go.Figure:
    u, v = np.mgrid[0 : 2 * np.pi : 20j, 0 : np.pi : 10j]
    r = 0.3
    x_s = r * np.cos(u) * np.sin(v)
    y_s = r * np.sin(u) * np.sin(v)
    z_s = r * np.cos(v)

    _ = fig.add_trace(
        go.Surface(
            x=x_s,
            y=y_s,
            z=z_s + z_offset,
            surfacecolor=np.ones_like(x_s),
            colorscale=[[0, color], [1, color]],
            showscale=False,
        )
    )

    return fig


def add_sky_plane(fig: go.Figure, color: str):
    grid = np.linspace(-4, 4, 10)
    xx, yy = np.meshgrid(grid, grid)

    fig.add_trace(
        go.Surface(
            x=xx,
            y=yy,
            z=np.zeros_like(xx),
            opacity=0.2,
            surfacecolor=np.ones_like(xx),
            colorscale=[[0, color], [1, color]],
            showscale=False,
            name="sky plane",
        )
    )

    return fig


def add_orbital_plane(fig: go.Figure, i: float, color: str):
    grid = np.linspace(-4, 4, 10)
    xx, yy = np.meshgrid(grid, grid)  # XY plane, not XZ
    zz = np.zeros_like(xx)
    orb_coords = np.array([xx.ravel(), yy.ravel(), zz.ravel()])
    rotated = rotate_ellipse(orb_coords, i)

    fig.add_trace(
        go.Surface(
            x=rotated[0].reshape(10, 10),
            y=rotated[1].reshape(10, 10),
            z=rotated[2].reshape(10, 10),
            opacity=0.2,
            surfacecolor=np.ones_like(xx),
            colorscale=[[0, color], [1, color]],
            showscale=False,
        )
    )

    return fig


def main():
    a = 1.5
    e = 0.3
    i = np.pi / 2 + 0.3  # 0 - pi radians (0 - 180 degrees)

    c = calculate_focus_offset(a, e)
    b = calculate_semi_minor_axis(a, e)

    f = np.linspace(0, 2 * np.pi, 300)
    x, y = calculate_coordinates(a, b, f)

    z = np.zeros_like(f)
    x_r, y_r, z_r = rotate_ellipse(np.array([x, y, z]), i)

    # shift so star is at origin
    x_r -= c

    fig = go.Figure()
    _ = fig.add_trace(go.Scatter3d(x=x_r, y=y_r, z=z_r, mode="lines"))
    fig = add_sphere(fig, 0.0, "yellow")
    fig = add_sphere(fig, 4.0, "black")
    fig = add_sky_plane(fig, "blue")
    fig = add_orbital_plane(fig, i, "orange")

    _ = fig.update_layout(
        showlegend=False,
        scene=dict(
            aspectmode="cube",
            xaxis=dict(range=[-5, 5]),
            yaxis=dict(range=[-5, 5]),
            zaxis=dict(range=[-5, 5]),
        ),
    )
    fig.write_html(Path("assets/3d_orbit.html"))


if __name__ == "__main__":
    main()

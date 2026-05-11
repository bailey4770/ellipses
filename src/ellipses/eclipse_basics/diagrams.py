import numpy as np
import plotly.graph_objects as go
from pathlib import Path
from copy import deepcopy

from ellipses.utils import rotate_ellipse

AXES_RANGE = [-5, 5]
OBSERVER_Z_OFFSET = 4.0
OBSERVER_COLOR = "black"


def draw_diagrams(x_r: np.ndarray, y_r: np.ndarray, z_r: np.ndarray, i: float):
    fig = go.Figure()
    _ = fig.add_trace(go.Scatter3d(x=x_r, y=y_r, z=z_r, mode="lines"))
    fig = _add_sphere(fig, 0.0, "yellow")
    fig = _add_sky_plane(fig, "blue")
    fig = _add_orbital_plane(fig, i, "orange")

    _get_3d_model(deepcopy(fig))


def _get_3d_model(fig: go.Figure):
    _ = fig.update_layout(
        showlegend=False,
        scene=dict(
            aspectmode="cube",
            xaxis=dict(range=AXES_RANGE),
            yaxis=dict(range=AXES_RANGE),
            zaxis=dict(range=AXES_RANGE),
        ),
    )

    fig = _add_sphere(fig, OBSERVER_Z_OFFSET, OBSERVER_COLOR)
    fig.write_html(Path("assets/3d_orbit.html"))
    fig.show()


def _add_sphere(fig: go.Figure, z_offset: float, color: str) -> go.Figure:
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
            colorscale=[[0, color], [1, color]],  # pyright: ignore
            showscale=False,
        )
    )

    return fig


def _add_sky_plane(fig: go.Figure, color: str):
    grid = np.linspace(-4, 4, 10)
    xx, yy = np.meshgrid(grid, grid)

    fig.add_trace(
        go.Surface(
            x=xx,
            y=yy,
            z=np.zeros_like(xx),
            opacity=0.2,
            surfacecolor=np.ones_like(xx),
            colorscale=[[0, color], [1, color]],  # pyright: ignore
            showscale=False,
            name="sky plane",
        )
    )

    return fig


def _add_orbital_plane(fig: go.Figure, i: float, color: str):
    grid = np.linspace(-4, 4, 10)
    xx, yy = np.meshgrid(grid, grid)  # XY plane, not XZ
    zz = np.zeros_like(xx)
    orb_coords = np.array([xx.ravel(), yy.ravel(), zz.ravel()])
    rotated = rotate_ellipse(orb_coords, i)

    _ = fig.add_trace(
        go.Surface(
            x=rotated[0].reshape(10, 10),
            y=rotated[1].reshape(10, 10),
            z=rotated[2].reshape(10, 10),
            opacity=0.2,
            surfacecolor=np.ones_like(xx),
            colorscale=[[0, color], [1, color]],  # pyright: ignore
            showscale=False,
        )
    )

    return fig

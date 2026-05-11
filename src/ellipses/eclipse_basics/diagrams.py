import numpy as np
import plotly.graph_objects as go
from pathlib import Path

from ellipses.utils import rotate_ellipse

AXES_RANGE = [-3.5, 3.5]
OBSERVER_Z_OFFSET = 2.5
OBSERVER_COLOR = "black"
ORTH_ZOOM = 0.5
PLANE_SIZE = 3.0
SQUARE_PLOT_LENGTH = 700
STAR_LABEL_Y_OFFSET = -0.1
OBJECT_SIZE = 0.3
TEXT_SIZE = 24
APSE_LABEL_OFFSET = 0.3
APSE_LABEL_Y = 2
ARROW_SIZE = 2.5
ARROW_HEAD = 2
ANGLE_ARC_RADIUS = 1.2
ANGLE_LABEL_OFFSET = 0.2


def draw_diagrams(
    x_r: np.ndarray, y_r: np.ndarray, z_r: np.ndarray, a: float, c: float, i: float
) -> None:
    _get_3d_model(x_r, y_r, z_r, i)
    _get_orth_observer(x_r, y_r, a, c)
    _get_orth_side(y_r, z_r, i)


def _get_3d_model(x_r: np.ndarray, y_r: np.ndarray, z_r: np.ndarray, i: float) -> None:
    fig = go.Figure()
    _ = fig.add_trace(go.Scatter3d(x=x_r, y=y_r, z=z_r, mode="lines"))
    fig = _add_sphere(fig, 0.0, "yellow")
    fig = _add_sphere(fig, OBSERVER_Z_OFFSET, OBSERVER_COLOR)
    fig = _add_sky_plane(fig, "blue")
    fig = _add_orbital_plane(fig, i, "orange")

    _ = fig.update_layout(
        showlegend=False,
        scene=dict(
            aspectmode="cube",
            xaxis=dict(range=AXES_RANGE),
            yaxis=dict(range=AXES_RANGE),
            zaxis=dict(range=AXES_RANGE),
        ),
    )

    fig.write_html(Path("assets/html/3d_orbit.html"))
    # fig.show()


def _get_orth_observer(
    x_r: np.ndarray,
    y_r: np.ndarray,
    a: float,
    c: float,
    square_plot_length: int = SQUARE_PLOT_LENGTH,
):
    # from observer's perspective
    fig = go.Figure()
    _ = fig.add_trace(go.Scatter(x=x_r, y=y_r, mode="lines"))
    fig = _add_circle(fig, 0, 0, "yellow")
    fig = _add_line_of_nodes_labels(fig, a, c)

    _ = fig.update_layout(
        width=square_plot_length,
        height=square_plot_length,
        showlegend=False,
        xaxis=dict(
            range=AXES_RANGE[::-1],
            dtick=1,
            title="x",
        ),
        yaxis=dict(
            range=AXES_RANGE,
            scaleanchor="x",
            scaleratio=1,
            dtick=1,
            title="y",
        ),
    )

    fig.write_image(Path("assets/img/orth_observer.png"))
    # fig.show()


def _add_line_of_nodes_labels(fig: go.Figure, a: float, c: float) -> go.Figure:
    ascending_node_x = -a - c
    descending_node_x = a - c

    _ = fig.add_annotation(
        x=ascending_node_x,
        y=0,
        ax=-a - APSE_LABEL_OFFSET,
        ay=-APSE_LABEL_Y,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[-a - APSE_LABEL_OFFSET],
            y=[-APSE_LABEL_Y],
            mode="text",
            text=["Ascending Node"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )

    _ = fig.add_annotation(
        x=descending_node_x,
        y=0,
        ax=a + APSE_LABEL_OFFSET,
        ay=APSE_LABEL_Y,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[a + APSE_LABEL_OFFSET],
            y=[APSE_LABEL_Y],
            mode="text",
            text=["Descending node"],
            textposition="top center",
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig


def _get_orth_side(
    y_r: np.ndarray,
    z_r: np.ndarray,
    i: float,
    square_plot_length: int = SQUARE_PLOT_LENGTH,
):
    fig = go.Figure()
    _ = fig.add_trace(go.Scatter(x=z_r, y=y_r, mode="lines"))
    _ = fig.add_trace(
        go.Scatter(
            x=[-4, 4],
            y=[0, 0],
            mode="lines",
            line=dict(color="gray"),
        )
    )
    fig = _add_circle(fig, 0, 0, "yellow")
    fig = _add_circle(fig, OBSERVER_Z_OFFSET, 0, "black")
    fig = _add_inclination_arc(fig, 0, 0, i)

    _ = fig.update_layout(
        width=square_plot_length,
        height=square_plot_length,
        showlegend=False,
        xaxis=dict(
            range=AXES_RANGE[::-1],
            dtick=1,
            title="z",
        ),
        yaxis=dict(
            range=AXES_RANGE,
            scaleanchor="x",
            scaleratio=1,
            dtick=1,
            title="y",
        ),
    )

    fig.write_image(Path("assets/img/orth_side.png"))
    # fig.show()


def _add_inclination_arc(
    fig: go.Figure,
    x_pos: float,
    y_pos: float,
    i: float,
    arc_radius: float = ANGLE_ARC_RADIUS,
    text_size: int = TEXT_SIZE,
    angle_label_offset: float = APSE_LABEL_OFFSET,
) -> go.Figure:
    # arc from 0 (reference line) to i (orbit angle)
    theta = np.linspace(0, i, 100)
    _ = fig.add_trace(
        go.Scatter(
            x=x_pos + arc_radius * np.cos(theta),
            y=y_pos + arc_radius * np.sin(theta),
            mode="lines",
            line=dict(color="black", width=1),
        )
    )
    # label at midpoint of arc
    mid = i / 2
    _ = fig.add_trace(
        go.Scatter(
            x=[x_pos + (arc_radius - angle_label_offset) * np.cos(mid)],
            y=[y_pos + (arc_radius - angle_label_offset) * np.sin(mid)],
            mode="text",
            text=["i"],
            textfont=dict(size=text_size),
        )
    )
    return fig


def _add_circle(
    fig: go.Figure,
    x_pos: float,
    y_pos: float,
    color: str,
    label: str = "",
    radius: float = OBJECT_SIZE,
) -> go.Figure:
    theta = np.linspace(0, 2 * np.pi, 100)
    _ = fig.add_trace(
        go.Scatter(
            x=x_pos + radius * np.cos(theta),
            y=y_pos + radius * np.sin(theta),
            mode="lines",
            fill="toself",
            fillcolor=color,
            line=dict(color=color),
        )
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[x_pos],
            y=[y_pos + radius + STAR_LABEL_Y_OFFSET],
            mode="text",
            text=[label],
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig


def _add_sphere(
    fig: go.Figure, z_offset: float, color: str, object_size: float = OBJECT_SIZE
) -> go.Figure:
    u, v = np.mgrid[0 : 2 * np.pi : 20j, 0 : np.pi : 10j]
    r = object_size
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


def _add_sky_plane(fig: go.Figure, color: str, plane_size: float = PLANE_SIZE):
    grid = np.linspace(-plane_size, plane_size, 10)
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


def _add_orbital_plane(
    fig: go.Figure, i: float, color: str, plane_size: float = PLANE_SIZE
):
    grid = np.linspace(-plane_size, plane_size, 10)
    xx, zz = np.meshgrid(grid, grid)  # XY plane, not XZ
    yy = np.zeros_like(xx)
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

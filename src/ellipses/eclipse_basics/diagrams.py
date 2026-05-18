import numpy as np
import plotly.graph_objects as go
from pathlib import Path

from ellipses.utils import rotate_ellipse_inclination, rotate_ellipse_periapsis

AXES_RANGE = [-3.5, 3.5]
OBSERVER_Z_OFFSET = 2.5
OBSERVER_COLOR = "black"
ORTH_ZOOM = 0.5
PLANE_SIZE = 3.0
SQUARE_PLOT_LENGTH = 700
STAR_LABEL_Y_OFFSET = -0.1
STAR_SIZE = 0.3
TEXT_SIZE = 24
SEMI_MAJOR_AXIS_LABEL_OFFSET = 0.1
APSE_LABEL_OFFSET = 0.3
APSE_LABEL_Y = 2
ARROW_SIZE = 2.5
ARROW_HEAD = 2
ANGLE_ARC_RADIUS = 1.2
ANGLE_LABEL_OFFSET = 0.2
OBSEVER_LABEL_X_OFFSET = 0.2


def draw_diagrams(
    x_r: np.ndarray,
    y_r: np.ndarray,
    z_r: np.ndarray,
    a: float,
    c: float,
    i: float,
    omega: float,
) -> None:
    _get_3d_model(x_r, y_r, z_r, i)
    _get_orth_observer(x_r, y_r, a, c, i, omega)
    _get_orth_side(y_r, z_r, i)


def _get_3d_model(x_r: np.ndarray, y_r: np.ndarray, z_r: np.ndarray, i: float) -> None:
    fig = go.Figure()
    _ = fig.add_trace(go.Scatter3d(x=x_r, y=y_r, z=z_r, mode="lines"))
    fig = _add_sun_sphere(fig)
    # fig = _add_sphere(fig, OBSERVER_Z_OFFSET, OBSERVER_COLOR)
    fig = _add_observer_3d(fig)
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
    i: float,
    omega: float,
    square_plot_length: int = SQUARE_PLOT_LENGTH,
):
    # from observer's perspective
    fig = go.Figure()
    _ = fig.add_trace(go.Scatter(x=x_r, y=y_r, mode="lines"))
    fig = _add_star_circle(fig, 0, 0)
    fig = _add_semi_major_axis(fig, a, c, i, omega)
    fig = _add_line_of_nodes_labels(fig, x_r, y_r)

    _ = fig.update_layout(
        width=square_plot_length,
        height=square_plot_length,
        showlegend=False,
        xaxis=dict(
            range=AXES_RANGE,
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


def _get_orth_side(
    y_r: np.ndarray,
    z_r: np.ndarray,
    i: float,
    square_plot_length: int = SQUARE_PLOT_LENGTH,
):
    fig = go.Figure()
    _ = fig.add_trace(go.Scatter(x=z_r, y=y_r, mode="lines"))
    fig = _add_star_circle(fig, 0, 0)
    fig = _add_observer_2d(fig)
    fig = _add_angle_arc(fig, i, "i")

    _ = fig.update_layout(
        width=square_plot_length,
        height=square_plot_length,
        showlegend=False,
        xaxis=dict(
            range=AXES_RANGE,
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


def _add_sun_sphere(fig: go.Figure, star_size: float = STAR_SIZE) -> go.Figure:
    u, v = np.mgrid[0 : 2 * np.pi : 20j, 0 : np.pi : 10j]
    x_s = star_size * np.cos(u) * np.sin(v)
    y_s = star_size * np.sin(u) * np.sin(v)
    z_s = star_size * np.cos(v)

    _ = fig.add_trace(
        go.Surface(
            x=x_s,
            y=y_s,
            z=z_s,
            surfacecolor=np.ones_like(x_s),
            colorscale=[[0, "yellow"], [1, "yellow"]],  # pyright: ignore
            showscale=False,
        )
    )

    return fig


def _add_observer_3d(fig: go.Figure) -> go.Figure:
    _ = fig.add_trace(
        go.Cone(
            x=[0],
            y=[0],
            z=[OBSERVER_Z_OFFSET],
            u=[0],
            v=[0],
            w=[OBSERVER_Z_OFFSET + 1],
            sizemode="absolute",
            sizeref=0.3,
            colorscale=[[0, "black"], [1, "black"]],  # pyright: ignore
            showscale=False,
        )
    )
    _ = fig.add_trace(
        go.Scatter3d(
            x=[0, 0],
            y=[0, 0],
            z=[0, OBSERVER_Z_OFFSET],
            mode="lines",
            line={"color": "black"},
        )
    )
    _ = fig.add_trace(
        go.Scatter3d(
            x=[0],
            y=[0],
            z=[OBSERVER_Z_OFFSET + 0.1],
            mode="text",
            text="To distant observer",
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
    rotated = rotate_ellipse_inclination(orb_coords, i)

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


def _add_star_circle(
    fig: go.Figure,
    x_pos: float,
    y_pos: float,
    radius: float = STAR_SIZE,
) -> go.Figure:
    theta = np.linspace(0, 2 * np.pi, 100)

    _ = fig.add_trace(
        go.Scatter(
            x=x_pos + radius * np.cos(theta),
            y=y_pos + radius * np.sin(theta),
            mode="lines",
            fill="toself",
            fillcolor="yellow",
            line={"color": "yellow"},
        )
    )

    return fig


def _add_semi_major_axis(
    fig: go.Figure,
    a: float,
    c: float,
    i: float,
    omega: float,
) -> go.Figure:
    start = np.array([-a - c, 0, 0])
    end = np.array([a - c, 0, 0])

    x_start_r, y_start_r, _ = rotate_ellipse_inclination(
        rotate_ellipse_periapsis(start, omega), i
    )
    x_end_r, y_end_r, _ = rotate_ellipse_inclination(
        rotate_ellipse_periapsis(end, omega), i
    )

    _ = fig.add_annotation(
        x=x_start_r,
        y=y_start_r,
        ax=x_end_r,
        ay=y_end_r,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_annotation(
        x=x_end_r,
        y=y_end_r,
        ax=x_start_r,
        ay=y_start_r,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[(x_end_r + x_start_r) / 2],
            y=[(y_end_r + y_start_r) / 2 + SEMI_MAJOR_AXIS_LABEL_OFFSET],
            mode="text",
            text=["a"],
            textposition="top center",
            textfont={"size": TEXT_SIZE},
        )
    )

    return fig


def _add_line_of_nodes_labels(
    fig: go.Figure,
    x_r: np.ndarray,
    y_r: np.ndarray,
) -> go.Figure:
    zero_crossings = np.where(np.diff(np.sign(y_r)))[0]
    nodes_x = x_r[zero_crossings]

    _ = fig.add_annotation(
        x=nodes_x[0],
        y=0,
        ax=nodes_x[0] + APSE_LABEL_OFFSET,
        ay=-APSE_LABEL_Y,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[nodes_x[0] + APSE_LABEL_OFFSET],
            y=[-APSE_LABEL_Y],
            mode="text",
            text=["Descending node"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )

    _ = fig.add_annotation(
        x=nodes_x[1],
        y=0,
        ax=nodes_x[1] - APSE_LABEL_OFFSET,
        ay=-APSE_LABEL_Y,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[nodes_x[1] - APSE_LABEL_OFFSET],
            y=[-APSE_LABEL_Y],
            mode="text",
            text=["Ascending node"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )

    _ = fig.add_trace(
        go.Scatter(
            x=nodes_x, y=[0, 0], mode="lines", line={"color": "green", "dash": "dash"}
        )
    )

    return fig


def _add_observer_2d(fig: go.Figure) -> go.Figure:
    _ = fig.add_annotation(
        x=OBSERVER_Z_OFFSET,
        y=0,
        ax=0,
        ay=0,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[OBSERVER_Z_OFFSET + OBSEVER_LABEL_X_OFFSET],
            y=[0],
            mode="text",
            text=["To distant<br>observer"],
            textposition="middle center",
            textfont={"size": TEXT_SIZE},
        )
    )

    return fig


def _add_angle_arc(
    fig: go.Figure,
    angle: float,
    label: str,
    arc_radius: float = ANGLE_ARC_RADIUS,
    text_size: int = TEXT_SIZE,
    angle_label_offset: float = APSE_LABEL_OFFSET,
) -> go.Figure:
    theta = np.linspace(0, angle, 100)

    _ = fig.add_trace(
        go.Scatter(
            x=arc_radius * np.cos(theta),
            y=arc_radius * np.sin(theta),
            mode="lines",
            line=dict(color="black", width=1),
        )
    )
    # label at midpoint of arc
    mid = angle / 2
    _ = fig.add_trace(
        go.Scatter(
            x=[(arc_radius - angle_label_offset) * np.cos(mid)],
            y=[(arc_radius - angle_label_offset) * np.sin(mid)],
            mode="text",
            text=[label],
            textfont=dict(size=text_size),
        )
    )
    return fig

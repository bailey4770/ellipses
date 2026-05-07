# pyright: reportUnknownMemberType=none, reportAny=none

import plotly.graph_objects as go
import numpy as np

ARROW_SIZE = 2.5
ARROW_HEAD = 2
TEXT_SIZE = 32
STAR_SIZE = 25
PLANET_SIZE = 15
STAR_LABEL_Y_OFFSET = -0.1
PLANET_LABEL_X_OFFSET = 0.05
APSE_LABEL_OFFSET = 0.3
APSE_LABEL_Y = 0.25
FOCI_LABEL_Y = -0.5
CENTRE_LABEL_Y_OFFSET = -0.01
SEMI_MINOR_LABEL_X_OFFSET = -0.01


def add_curve(
    fig: go.Figure,
    x: np.ndarray,
    y: np.ndarray,
    color: str | None = None,
    dash: str | None = None,
) -> go.Figure:
    """Adds a parametric curve as a line trace to a Plotly figure.

    Args:
        fig: A Plotly figure to draw the curve on.
        x: x-coordinates of the curve.
        y: y-coordinates of the curve.
        color: Optional line color.
        dash: Optional line dash style (e.g. 'dash', 'dot', 'dashdot').

    Returns:
        The input figure with the curve trace added.
    """
    line_opts: dict[str, str] = {}
    if color:
        line_opts["color"] = color
    if dash:
        line_opts["dash"] = dash
    _ = fig.add_trace(go.Scatter(x=x, y=y, mode="lines", line=line_opts))
    return fig


def animate_orbit(fig: go.Figure, x: np.ndarray, y: np.ndarray, c: float) -> go.Figure:
    fig = _add_star(fig, c)

    _ = fig.add_trace(
        go.Scatter(
            x=[x[0]],
            y=[y[0]],
            mode="markers",
            marker={"size": PLANET_SIZE, "color": "black"},
        )
    )

    frames = []
    for _ in range(10):
        for i in range(len(x)):
            frame = go.Frame(
                data=[
                    go.Scatter(
                        x=[x[i]],
                        y=[y[i]],
                        mode="markers",
                        marker={"size": PLANET_SIZE, "color": "black"},
                    )
                ],
                traces=[3],
            )
            frames.append(frame)

    _ = fig.update_layout(
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 30},
                                "transition": {"duration": 0},
                                "fromcurrent": True,
                            },
                        ],
                    }
                ],
            }
        ]
    )

    fig.frames = frames

    return fig


def draw_anomalies(
    fig: go.Figure,
    a: float,
    c: float,
    x_M: np.ndarray,
    y_M: np.ndarray,
    x_ellipse: np.ndarray,
    y_ellipse: np.ndarray,
    x_circle: np.ndarray,
    y_circle: np.ndarray,
    E: np.ndarray,
    M: np.ndarray,
    planet_pos: int,
) -> go.Figure:
    """Draws the auxiliary circle with anomaly angle annotations.

    Args:
        fig: A Plotly figure containing an ellipse trace.
        a: Semi-major axis length.
        c: Distance from centre to focus (focal offset).
        x_M: x-coordinates of the mean anomaly planet's path on the auxiliary circle.
        y_M: y-coordinates of the mean anomaly planet's path on the auxiliary circle.
        x_ellipse: x-coordinates of the elliptical orbit.
        y_ellipse: y-coordinates of the elliptical orbit.
        x_circle: x-coordinates of the auxiliary circle.
        y_circle: y-coordinates of the auxiliary circle.
        E: Eccentric anomaly array.
        M: Mean anomaly array.
        planet_pos: Index into the coordinate arrays selecting the planet's position.

    Returns:
        The input figure with anomaly annotations added in-place.
    """
    fig = add_curve(fig, x_circle, y_circle)
    fig = _add_star(fig, c)

    fig = _add_static_planet(
        fig, x_ellipse[planet_pos], y_ellipse[planet_pos], label="P"
    )
    fig = _add_static_planet(fig, x_circle[planet_pos], y_circle[planet_pos], label="Q")
    fig = _add_static_planet(fig, x_M[planet_pos], y_M[planet_pos], label="F")

    fig = _add_anomaly_angles(
        fig, a, c, x_M, y_M, x_ellipse, y_ellipse, x_circle, y_circle, E, M, planet_pos
    )

    _ = fig.update_layout(yaxis=dict(scaleanchor="x", scaleratio=1))
    return fig


def draw_elliptical_orbit_labels(
    fig: go.Figure,
    c: float,
    a: float,
    x: np.ndarray,
    y: np.ndarray,
    planet_pos: int,
) -> go.Figure:
    """Adds orbital body markers and apse labels to an elliptical orbit figure.

    Annotates the figure with the star at the focus, the planet at its
    initial position, and markers for apoapsis and periapsis.

    Args:
        fig: A Plotly figure containing an elliptical orbit trace.
        c: Distance from centre to focus (focal offset), used to position the star.
        a: Semi-major axis length, used to derive apoapsis and periapsis positions.
        x: x-coordinates of the planet's orbital path.
        y: y-coordinates of the planet's orbital path.
        planet_pos: Index into the coordinate arrays selecting the planet's position.

    Returns:
        The input figure with orbital annotations added in-place.
    """
    fig = _add_star(fig, c)
    fig = _add_static_planet(fig, x[planet_pos], y[planet_pos], "Planet")
    fig = _add_apoapsis_and_periapsis(fig, a)

    return fig


def draw_labels_on_ellipse(fig: go.Figure, a: float, b: float, c: float) -> go.Figure:
    """Adds geometric labels to an ellipse figure.

    Annotates the figure with dimension lines and markers for the
    centre, semi-major axis, semi-minor axis, foci, and focus offset.

    Args:
        fig: A Plotly figure containing an ellipse trace.
        a: Semi-major axis length.
        b: Semi-minor axis length.
        c: Distance from centre to focus (focal offset).

    Returns:
        The input figure with annotations added in-place.
    """
    fig = _label_centre(fig)
    fig = _label_semi_major(fig, a)
    fig = _label_semi_minor(fig, b)
    fig = _label_foci(fig, c)
    fig = _label_offset(fig, c)

    return fig


def _add_anomaly_angles(
    fig: go.Figure,
    a: float,
    c: float,
    x_M: np.ndarray,
    y_M: np.ndarray,
    x_ellipse: np.ndarray,
    y_ellipse: np.ndarray,
    x_circle: np.ndarray,
    y_circle: np.ndarray,
    E: np.ndarray,
    M: np.ndarray,
    planet_pos: int,
) -> go.Figure:
    """Draws angle lines and arcs for the eccentric, mean, and true anomalies."""
    _ = fig.add_shape(type="line", x0=0, y0=0, x1=a, y1=0)  # from centre to periapsis

    fig = _add_anomaly_angle(
        fig,
        start_x=0.0,
        end_x=x_circle[planet_pos],
        end_y=y_circle[planet_pos],
        limit=E[planet_pos],
        arc_radius=0.25,
        label="E",
        x_offset_label=0.08,
        color="green",
    )
    fig = _add_anomaly_angle(
        fig,
        start_x=0.0,
        end_x=x_M[planet_pos],
        end_y=y_M[planet_pos],
        limit=M[planet_pos],
        arc_radius=0.6,
        label="M",
        x_offset_label=0.4,
        color="red",
    )
    fig = _add_anomaly_angle(
        fig,
        start_x=c,
        end_x=x_ellipse[planet_pos],
        end_y=y_ellipse[planet_pos],
        limit=np.arctan2(y_ellipse[planet_pos], x_ellipse[planet_pos] - c),
        arc_radius=0.25,
        label="ν",
        x_offset_label=0.03,
        color="purple",
    )

    _ = fig.add_trace(
        go.Scatter(
            x=[x_ellipse[planet_pos], x_circle[planet_pos]],
            y=[y_ellipse[planet_pos], y_circle[planet_pos]],
            mode="lines",
            line={"color": "black", "dash": "dash"},
        )
    )

    return fig


def _calculate_angle_arc(
    limit: float, arc_radius: float, start_x: float
) -> tuple[np.ndarray, np.ndarray]:
    """Computes x, y coordinates for an angle arc at a given pivot and radius."""
    theta = np.linspace(0, limit, 50)
    x_arc = arc_radius * np.cos(theta) + start_x
    y_arc = arc_radius * np.sin(theta)
    return x_arc, y_arc


def _add_anomaly_angle(
    fig: go.Figure,
    start_x: float,
    end_x: np.float64,
    end_y: np.float64,
    limit: np.float64,
    arc_radius: float,
    label: str,
    x_offset_label: float,
    color: str,
) -> go.Figure:
    """Draws a single anomaly angle: a line from the pivot, an arc, and a label."""
    _ = fig.add_shape(type="line", x0=start_x, y0=0, x1=end_x, y1=end_y)

    x_arc, y_arc = _calculate_angle_arc(limit, arc_radius, start_x)
    fig = add_curve(fig, x_arc, y_arc, color)

    _ = fig.add_trace(
        go.Scatter(
            x=[start_x + x_offset_label],
            y=[0],
            mode="text",
            text=[label],
            textposition="top right",
            textfont={"size": TEXT_SIZE, "color": color},
        )
    )

    return fig


def _add_star(fig: go.Figure, c: float) -> go.Figure:
    """Adds a star marker and label at the focus position."""
    _ = fig.add_trace(
        go.Scatter(
            x=[c],
            y=[0],
            mode="markers",
            marker={"size": STAR_SIZE, "color": "yellow"},
            name="Star",
        )
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[c],
            y=[STAR_LABEL_Y_OFFSET],
            mode="text",
            text=["Star"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig


def _add_static_planet(
    fig: go.Figure,
    planet_pos_x: np.float64,
    planet_pos_y: np.float64,
    label: str,
) -> go.Figure:
    """Adds a planet marker and label at the given position."""
    _ = fig.add_trace(
        go.Scatter(
            x=[planet_pos_x],
            y=[planet_pos_y],
            mode="markers",
            marker={"size": PLANET_SIZE, "color": "black"},
            name="Planet",
        )
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[planet_pos_x + PLANET_LABEL_X_OFFSET],
            y=[planet_pos_y],
            mode="text",
            text=[label],
            textposition="middle right",
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig


def _add_apoapsis_and_periapsis(fig: go.Figure, a: float) -> go.Figure:
    """Adds annotated arrows pointing to apoapsis and periapsis."""
    _ = fig.add_annotation(
        x=-a,
        y=0,
        ax=-a + APSE_LABEL_OFFSET,
        ay=APSE_LABEL_Y,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[-a + APSE_LABEL_OFFSET],
            y=[APSE_LABEL_Y],
            mode="text",
            text=["Apoapsis"],
            textposition="top right",
            textfont={"size": TEXT_SIZE},
        )
    )

    _ = fig.add_annotation(
        x=a,
        y=0,
        ax=a - APSE_LABEL_OFFSET,
        ay=APSE_LABEL_Y,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[a - APSE_LABEL_OFFSET],
            y=[APSE_LABEL_Y],
            mode="text",
            text=["Periapsis"],
            textposition="top left",
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig


def _label_centre(fig: go.Figure) -> go.Figure:
    """Adds a centre point marker and label at the origin."""
    _ = fig.add_trace(
        go.Scatter(x=[0], y=[0], mode="markers", marker={"size": 5, "color": "black"})
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[0],
            y=[CENTRE_LABEL_Y_OFFSET],
            mode="text",
            text=["Centre"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig


def _label_semi_major(fig: go.Figure, a: float) -> go.Figure:
    """Adds a double-headed arrow and label for the semi-major axis."""
    _ = fig.add_annotation(
        x=0,
        y=0,
        ax=a,
        ay=0,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_annotation(
        x=a,
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
            x=[a / 2],
            y=[0],
            mode="text",
            text=["a"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig


def _label_semi_minor(fig: go.Figure, b: float) -> go.Figure:
    """Adds a double-headed arrow and label for the semi-minor axis."""
    _ = fig.add_annotation(
        x=0,
        y=0,
        ax=0,
        ay=b,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_annotation(
        x=0,
        y=b,
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
            x=[SEMI_MINOR_LABEL_X_OFFSET],
            y=[b / 2],
            mode="text",
            text=["b"],
            textposition="middle left",
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig


def _label_foci(fig: go.Figure, c: float) -> go.Figure:
    """Adds markers and a shared label for both foci."""
    for x_pos in [-c, c]:
        _ = fig.add_trace(
            go.Scatter(
                x=[x_pos], y=[0], mode="markers", marker={"size": 5, "color": "black"}
            )
        )
        _ = fig.add_annotation(
            x=x_pos,
            y=0,
            ax=0,
            ay=FOCI_LABEL_Y,
            axref="x",
            ayref="y",
            showarrow=True,
            arrowhead=ARROW_HEAD,
            arrowsize=ARROW_SIZE,
        )
    _ = fig.add_trace(
        go.Scatter(
            x=[0],
            y=[FOCI_LABEL_Y],
            mode="text",
            text=["Foci"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig


def _label_offset(fig: go.Figure, c: float) -> go.Figure:
    """Adds a double-headed arrow and label for the focal offset c."""
    _ = fig.add_annotation(
        x=0,
        y=0,
        ax=-c,
        ay=0,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_annotation(
        x=-c,
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
            x=[-(c / 2)],
            y=[0],
            mode="text",
            text=["c"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )
    return fig

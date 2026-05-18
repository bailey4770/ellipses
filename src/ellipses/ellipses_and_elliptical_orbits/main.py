import numpy as np
import plotly.graph_objects as go
from copy import deepcopy

from ellipses.utils import (
    calculate_focus_offset,
    calculate_semi_minor_axis,
    calculate_coordinates,
    calculate_eccentric_anomaly,
)
from .label_ellipse import (
    add_curve,
    draw_labels_on_ellipse,
    draw_elliptical_orbit_labels,
    draw_anomalies,
    animate_orbit,
)


def main():
    a = 1.5  # semi-major axis of ellipse
    e = 0.75  # eccentricity of ellipse

    c = calculate_focus_offset(a, e)
    b = calculate_semi_minor_axis(a, e)

    M = np.linspace(0, 2 * np.pi, 400)  # mean anomaly
    x_M, y_M = calculate_coordinates(a, a, M)  # coords for hypothetical circle

    E = calculate_eccentric_anomaly(M, e)
    x_ellipse, y_ellipse = calculate_coordinates(a, b, E)
    x_circle, y_circle = calculate_coordinates(a, a, E)

    fig = go.Figure()
    _ = fig.update_layout(
        showlegend=False,
        xaxis=dict(range=[-a * 1.2, a * 1.2], autorange=False),
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            autorange=False,
            range=[-a * 1.2, a * 1.2],
        ),
    )

    fig = add_curve(fig, x_ellipse, y_ellipse)

    draw_labels_on_ellipse(deepcopy(fig), a, b, c)
    draw_elliptical_orbit_labels(deepcopy(fig), c, a, x_ellipse, y_ellipse)
    draw_anomalies(
        deepcopy(fig), a, c, x_M, y_M, x_ellipse, y_ellipse, x_circle, y_circle, E, M
    )
    animate_orbit(deepcopy(fig), x_ellipse, y_ellipse, c)


if __name__ == "__main__":
    main()

import numpy as np
import plotly.graph_objects as go

from label_ellipse import add_curve, draw_anomalies

a = 1.5  # semi-major axis of ellipse
e = 0.75  # eccentricity of ellipse


def _calculate_focus_offset(a: float, e: float) -> float:
    return a * e


def _calculate_semi_minor_axis(a: float, e: float) -> np.float64:
    b_squared: float = (a**2) * (1 - e**2)
    return np.sqrt(b_squared)  # pyright: ignore[reportAny]


def _calculate_coordinates(
    a: float, b: float, E: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    x = a * np.cos(E)
    y = b * np.sin(E)
    return (x, y)


def main():
    c = _calculate_focus_offset(a, e)
    b = _calculate_semi_minor_axis(a, e)

    E = np.linspace(0, 2 * np.pi, 1000)  # eccentric anomaly
    x_ellipse, y_ellipse = _calculate_coordinates(a, b, E)

    M = E - e * np.sin(E)  # mean anomaly
    x_M, y_M = _calculate_coordinates(a, a, M)

    fig = go.Figure()
    fig = add_curve(fig, x_ellipse, y_ellipse)
    fig = draw_anomalies(
        fig,
        a,
        c,
        x_M,
        y_M,
        x_ellipse,
        y_ellipse,
        *_calculate_coordinates(a, a, E),
        E,
        M,
        planet_pos=150,
    )

    _ = fig.update_layout(showlegend=False)
    fig.show()


if __name__ == "__main__":
    main()

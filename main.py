import numpy as np
import plotly.graph_objects as go

from label_ellipse import add_curve, animate_orbit

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


def _calculate_eccentric_anomaly(M: np.ndarray, e: float) -> np.ndarray:
    eccentric_anomaly = M.copy()  # initial guess
    for _ in range(5):
        eccentric_anomaly = eccentric_anomaly - (
            eccentric_anomaly - e * np.sin(eccentric_anomaly) - M
        ) / (1 - e * np.cos(eccentric_anomaly))

    return eccentric_anomaly


def main():
    c = _calculate_focus_offset(a, e)
    b = _calculate_semi_minor_axis(a, e)

    M = np.linspace(0, 2 * np.pi, 400)  # mean anomaly
    x_M, y_M = _calculate_coordinates(a, a, M)  # coords for hypothetical circle

    E = _calculate_eccentric_anomaly(M, e)
    x_ellipse, y_ellipse = _calculate_coordinates(a, b, E)

    # x_circle, y_circle = _calculate_coordinates(a, a, E)

    fig = go.Figure()
    fig = add_curve(fig, x_ellipse, y_ellipse)
    fig = animate_orbit(fig, x_ellipse, y_ellipse, c)

    _ = fig.update_layout(showlegend=False)
    fig.write_html("./img/animation.html")
    fig.show()


if __name__ == "__main__":
    main()

import numpy as np
import plotly.graph_objects as go


def _calculate_focus_offset(a: float, e: float) -> float:
    return a * e


def _calculate_semi_minor_axis(a: float, e: float) -> np.float64:
    b_squared: float = (a**2) * (1 - e**2)
    return np.sqrt(b_squared)


def _calculate_coordinates(a: float, b: float) -> tuple[np.ndarray, np.ndarray]:
    E = np.linspace(0, 2 * np.pi, 1000)  # eccentric anomaly

    x = a * np.cos(E)
    y = b * np.sin(E)
    return (x, y)


def main():
    a = 1.5  # semi-major axis of ellipse
    e = 0.4  # eccentricity of ellipse

    c = _calculate_focus_offset(a, e)
    b = _calculate_semi_minor_axis(a, e)

    x, y = _calculate_coordinates(a, b)

    fig = go.Figure()
    _ = fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))
    fig.show()


if __name__ == "__main__":
    main()

import numpy as np


def calculate_focus_offset(a: float, e: float) -> float:
    return a * e


def calculate_semi_minor_axis(a: float, e: float) -> np.float64:
    b_squared: float = (a**2) * (1 - e**2)
    return np.sqrt(b_squared)  # pyright: ignore[reportAny]


def calculate_coordinates(
    a: float, b: float, E: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    x = a * np.cos(E)
    y = b * np.sin(E)
    return (x, y)


def calculate_eccentric_anomaly(M: np.ndarray, e: float) -> np.ndarray:
    eccentric_anomaly = M.copy()  # initial guess
    for _ in range(5):
        eccentric_anomaly = eccentric_anomaly - (
            eccentric_anomaly - e * np.sin(eccentric_anomaly) - M
        ) / (1 - e * np.cos(eccentric_anomaly))

    return eccentric_anomaly


def rotate_ellipse(coords: np.ndarray, i: float) -> np.ndarray:
    rotation_matrix = [[1, 0, 0], [0, np.cos(i), -np.sin(i)], [0, np.sin(i), np.cos(i)]]
    return rotation_matrix @ coords

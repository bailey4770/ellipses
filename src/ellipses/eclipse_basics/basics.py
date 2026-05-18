import numpy as np

from ellipses.utils import (
    calculate_coordinates,
    calculate_focus_offset,
    calculate_semi_minor_axis,
    rotate_ellipse_inclination,
    rotate_ellipse_periapsis,
)
from ellipses.eclipse_basics.diagrams import draw_diagrams


def main():
    a = 1.5
    e = 0.3
    i = np.pi / 4  # 0 - pi radians (0 - 180 degrees)
    omega = np.pi / 8

    c = calculate_focus_offset(a, e)
    b = calculate_semi_minor_axis(a, e)
    f = np.linspace(0, 2 * np.pi, 300)
    x, z = calculate_coordinates(a, b, f)
    # shift so star is at origin
    x -= c

    y = np.zeros_like(f)
    x_r, y_r, z_r = rotate_ellipse_periapsis(np.array([x, y, z]), omega)
    x_r, y_r, z_r = rotate_ellipse_inclination(np.array([x_r, y_r, z_r]), i)

    draw_diagrams(x_r, y_r, z_r, a, c, i)


if __name__ == "__main__":
    main()

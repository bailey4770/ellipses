import numpy as np

from ellipses.utils import (
    calculate_coordinates,
    calculate_focus_offset,
    calculate_semi_minor_axis,
    rotate_ellipse,
)
from ellipses.eclipse_basics.diagrams import draw_diagrams


def main():
    a = 1.5
    e = 0.3
    i = np.pi / 2 + 0.3  # 0 - pi radians (0 - 180 degrees)

    c = calculate_focus_offset(a, e)
    b = calculate_semi_minor_axis(a, e)

    f = np.linspace(0, 2 * np.pi, 300)
    x, y = calculate_coordinates(a, b, f)

    z = np.zeros_like(f)
    x_r, y_r, z_r = rotate_ellipse(np.array([x, y, z]), i)

    # shift so star is at origin
    x_r -= c

    draw_diagrams(x_r, y_r, z_r, i)


if __name__ == "__main__":
    main()

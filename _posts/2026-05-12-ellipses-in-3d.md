---
title: Elliptical Orbits in Three Dimensions
excerpt: An extension of elliptical orbits to three dimensions
toc: true
---

In the [previous post](/ellipses/2026/05/10/ellipses-and-elliptical-orbits.html)
we explored elliptical orbits in two dimensions. But to understand eclipses, we
need to add the third dimension.

By doing so, we also need to be aware of how the ellipse could be rotated:

- A rotation in the plane of reference affects the **longitude of the ascending
  node** $\Omega$ in the diagram below.
- A rotation in the orbital plane affects the **argument of periapsis** $\omega$
  in the diagram below.
- A rotation about the X-axis affects the **inclination** $i$ in the diagram
  below.

<figure>
  <img src="/ellipses/assets/img/possible_rotations_3d.png" width="700px" height="700px" frameborder="0">
  <figcaption>Figure 1: A figure showing the three different possible angles of rotation. (Source: www.wikiwand.com)</figcaption>
</figure>

We are free to define the coordinate system to make our lives as easy as
possible. Previously, the orbit was flat on the XY-plane, but now we define the
orbit as originally flat on the XZ-plane, or the reference frame.

We also previously defined the origin as the centre of the ellipse, with the
star offset on the X-axis by $c$, but now we define the star at the origin with
the ellipse offset on the X-axis by $c$.

We place the observer at (0, 0, large positive Z).

## Line of nodes and Longitude of the ascending node

Consider below an orthographic projection for the view of the elliptical orbit
from the observer's perspective. We could also call this projection the
sky-plane, as seen on the celestial sphere about the observer.

Where the orbiting object crosses $z=0$ moving towards the observer, so into
positive $z$, is called the **descending node**. Where the orbiting object
crosses $z=0$ moving away from the observer, so into negative $z$, is called the
**ascending node**.

A straight line connecting these two, passing through the centre of the star, is
called the **line of nodes**, as shown by the green dashed line in Figure 2.

Since the longitude of the ascending node drawn on the celestial sphere is
usually difficult to actually know, and is often entirely unknown, we simply
define the X-axis to align with this line, so that the descending node is in
positive $x$ and the ascending node is in negative $x$. This results in
$\Omega = 180^{\circ}$ and removes the concept of rotation about the Z-axis
entirely, simplifying our maths.

<figure>
  <img src="/ellipses/assets/img/orth_observer.png" width="700px" height="700px" frameborder="0">
  <figcaption>Figure 2: An orthographic projection of an elliptical orbit in three dimensions from the observer's perspective. (Source: Own diagram)</figcaption>
</figure>

## Argument of Periapsis

Figure 2 does, however, show the ellipse rotated in the orbital plane. The angle
of rotation is called the argument of periapsis $\omega$.

The line below labeled $a$ shows the semi-major axis, connecting the periapsis
and apoapsis of the elliptical orbit. In our 2d diagrams, we defined the X-axis
as being aligned with the semi-major axis, so this rotation was irrelevant.
However, since we define the X-axis as aligning with the line of nodes, this
rotation becomes relevant and explains why the line of nodes does not
necessarily always align with the semi-major axis.

The argument of periapsis is not labelled in Figure 2, because the diagram shows
the orbit on the sky plane, but the rotation is applied in the orbital plane.
See Figure 1 for labelled $\omega$.

## Inclination

The value of the inclination represents how much the orbit is rotated about the
Y-axis. The inclination is measured in radians within the range
$0 \leq i \leq \pi$, where $i = 0$ represents an orbit flat on the reference
frame and $i = \pi$ represents an orbit orthogonal to the reference frame.

<figure>
  <img src="/ellipses/assets/img/orth_side.png" width="700px" height="700px" frameborder="0">
  <figcaption>Figure 3: An orthographic projection of an elliptical orbit in three dimensions from the side, with labeled inclination $i$. In this figure, $i = \frac{\pi}{4}$ radians. (Source: Own diagram)</figcaption>
</figure>

## 3D model

To recap our coordinate system: we define the star at the origin, with
ourselves, the observer, at large positive Z. To simplify the maths, we define
the X-axis to be aligned with the line of nodes. The Y-axis is then the only
possible remaining direction which is orthogonal to both the Z- and X-axes.

The 3D model below shows a distant observer, a star (the yellow sphere) and an
elliptical orbit around it (blue curve). The blue plane is the XY, or sky,
plane, as viewed from the observer, centred around the star. The orange plane is
the orbital plane.

Explore the 3D model by panning and zooming to ensure you understand the
geometry of elliptical orbits in three dimensions.

<figure>
  <iframe src="/ellipses/assets/html/3d_orbit.html" width="100%" height="600px" frameborder="0"></iframe>
  <figcaption>Figure 4: A 3D visualisation of an elliptical orbit, showing the sky plane and orbital plane. (Source: Own diagram)</figcaption>
</figure>

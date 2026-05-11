---
title: Eclipse Basics
excerpt: TODO
toc: true
---

## Elliptical orbits in three dimensions

In the [previous post](/ellipses/2026/05/10/ellipses-and-elliptical-orbits.html)
we explored elliptical orbits in two dimensions. But to understand eclipses, we
need to add the third dimension.

We are free to define our coordinate system however we want, so we do so to make
our lives as easy as possible. Previously, the orbit was flat on the XY plane,
but now we define the orbit (represented by the blue line) as flat on the XZ
plane, or the reference frame, where $y = 0$ with inclination $i$. The value of
the inclination represents how the orbit is tilted on the y axis.

We also previously defined the origin as the centre of the ellipse, with the
star offset on the x axis by $c$ but now we define the star (represented by the
yellow circle) at the origin, with the ellipse offset on the x axis by $c$. We
place the observer (represented by the black circle) at (0, 0, large positive
Z).

**Nb.** For demonstration purposes, the diagrams below are not to scale, and the
observer has a much smaller Z value than would be realistic.

### Inclination

The inclination is measured in radians within the range $0 \leq i \leq \pi$,
where $i = 0$ represents an orbit flat on the reference frame and $i = \pi$
represents an orbit orthogonal to the reference frame.

<figure>
  <img src="/ellipses/assets/img/orth_side.png" width="700px" height="700px" frameborder="0">
  <figcaption>Figure 1: An orthographic projection of an elliptical orbit in three dimensions from the side, with labeled inclination $i$. In this figure, $i = \frac{\pi}{6}$ radians.</figcaption>
</figure>

### Line of nodes

Consider below a second orthographic projection for the view of the elliptical
orbit from the observer's perspective.

Where the orbiting object crosses where $z=0$ moving towards the observer, so
into positive $z$, is called the **descending node**. Where the orbiting object
crosses where $z=0$ moving away from the observer, so into negative $z$, is
called the **ascending node**.

A straight line connecting these two, passing through the centre of the star, is
called the **line of nodes**, and we define the x axis to align with this line,
so that the descending node is in positive $x$ and the ascending node is in
negative $x$.

<figure>
  <img src="/ellipses/assets/img/orth_observer.png" width="700px" height="700px" frameborder="0">
  <figcaption>Figure 2: An orthographic projection of an elliptical orbit in three dimensions from the observer's perspective, with labeled inclination $i$.</figcaption>
</figure>

### 3D model

To recap our coordinate system: we define the star at the origin, with
ourselves, the observer, at large positive Z. We then observe the line of nodes,
and define the x axis as orthogonal to the z axis but aligned with the line of
nodes. The y axis is then the only possible remaining direction which is
orthogonal to both the z and x axes.

The 3D model below shows an observer (the black sphere), a star (the yellow
sphere) and an elliptical orbit around it (blue curve). The blue plane is the
XY, or sky, plane. It shows the sky, as viewed from the observer, centred around
the star. The orange plane is the orbital plane.

Explore the 3D model by panning and zooming to ensure you understand the
geometry of elliptical orbits in three dimensions.

<figure>
  <iframe src="/ellipses/assets/html/3d_orbit.html" width="100%" height="600px" frameborder="0"></iframe>
  <figcaption>Figure 3: A 3D visualisation of an elliptical orbit, showing the sky plane and orbital plane.</figcaption>
</figure>

## Geometry of eclipses

Consider a planet of radius $R_P$ and mass $M_P$ orbitting a star of radius
$R_\*$ and mass $M_*$. Let's define the ratio of planet-to-star radius as:

$$
k = \frac{R_P}{R_*} \tag{1}
$$

The distance between the star and the planet is given by:

$$
r = \frac{a(1 - e^2)}{1 + e \cos f'} \tag{2}
$$

where $e$ is the elliptical orbit's eccentricity and $f$ is the
[true anomaly](ellipses/2026/05/10/ellipses-and-elliptical-orbits.html#true-anomaly),
an implicit function of orbital eccentricity $e$ and period $P$.

We can resolve this into Cartesian coordinate equations within our defined
coordinate system.

$$
X = -r \cos (w + f) \tag{3}
Y = -r \sin (w + f) \cos i \tag{4}
Z = r \sin (w + f) \sin i \tag{5}
$$

Consider again the orthographic projection of the 3D model from the perspective
of the observer.

The projected distance on this plot is represented by:

$$
r_{sky} \equiv \sqrt{X^2 + Y^2} \tag{6}
$$

by Pythagorean theorem. If an eclipse occurs, it will do so at a local minimum
of $r_{sky}$, as labeled below.

# TODO add new labeled projection

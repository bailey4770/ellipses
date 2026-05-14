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
plane, or the reference frame, where $y = 0$ with inclination $i$.

We also previously defined the origin as the centre of the ellipse, with the
star offset on the x axis by $c$ but now we define the star (represented by the
yellow circle) at the origin, with the ellipse offset on the x axis by $c$. We
place the observer (represented by the black circle) at (0, 0, large positive
Z).

**Nb.** For demonstration purposes, the diagrams below are not to scale, and the
observer has a much smaller Z value than would be realistic.

### Inclination

The value of the inclination represents how much the orbit is tilted on the y
axis. The inclination is measured in radians within the range
$0 \leq i \leq \pi$, where $i = 0$ represents an orbit flat on the reference
frame and $i = \pi$ represents an orbit orthogonal to the reference frame.

# TODO explore other ways of representing observer

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
$$

$$
Y = -r \sin (w + f) \cos i \tag{4}
$$

$$
Z = r \sin (w + f) \sin i \tag{5}
$$

where $w$ represents the **argument of periapsis**.

# TODO labelled diagram with w

Consider again the orthographic projection of the 3D model from the perspective
of the observer.

# TODO add orthographic proj

The projected distance on this plot is represented by:

$$
r_{sky} \equiv \sqrt{X^2 + Y^2} \tag{6}
$$

by Pythagorean theorem. We can substitute in equations 3 and 4 for $X$ and $Y$
to get:

$$
r_{sky} = \frac{a(1-e^2)}{1 + e \cos f} \sqrt{1 - \sin ^2 {(w + f)} \sin^2 {i}} \tag{7}
$$

If an eclipse occurs, it will do so at a local minimum of $r_{sky}$. Minimising
this expression is long and difficult, but we can approximate by stating that
eclipses are centred around conjunctions, which are defined by where $X=0$.
Conjunctions can either be superior, with the planet in front (a transit); or
inferior, with the planet behind (an occultation).

We can find expressions for $f$ for both a transit:

$$
f_{tra} = + \frac{\pi}{2} - w \tag{8}
$$

an an occultation:

$$
f_{occ} = - \frac{\pi}{2} - w \tag{9}
$$

This approximation is normally valid except for extremely eccentric and close-in
orbits, and most importantly for non-grazing orbits. If an orbit is grazing,
then a small error can mean the difference between an eclipse and no eclipse.

The **impact parameter** $b$ is the sky-projected distance at the conjunction,
in units of stellar radius. It ranges $0 \leq b$, where $b = 0$ describes where
the planet appears to the observer to pass through the star's centre; $b = 1$
describes a grazing transit, where the planet passes along the edge of the star;
and $b > 1$ represents no eclipse. It is a function of the inclination and
eccentricity of the orbit, and we can derive the two expressions for it below:

$$
b_{tra} = \frac{a \cos i}{R_{*}} (\frac{1 - e^2}{1 + e \sin w}) \tag{10}
$$

$$
b_{occ} = \frac{a \cos i}{R_{*}} (\frac{1 - e^2}{1 - e \sin w}) \tag{11}
$$

We can simplify this further. For the common case where the stellar radius is
much smaller than the orbits semi-major axis $R_{*} << a$, then the exoplanet's
path across the star can be approximated by a straight line between the two
points:

$$
X = \pm R_{*} \sqrt{1 - b^2} \tag{12}
$$

## Probability of eclipse

The astute reader may have noticed that in the examples given above, the
observer cannot actually observe an eclipse. This is due to the large
inclination of the exoplanet's orbit from the reference plane. As seen in Figure
3, the orbital plane does not intersect the observer. To observe an eclipse, the
inclination of the exoplanet's orbit must be small - the orbit must be close to
edge-on.

Consider the excellent figure below from the Winn 2010 paper.

# TODO check if below image it stretched

<figure>
  <img src="/ellipses/assets/img/winn_eclipse_angle.png" width="700px" height="700px" frameborder="0">
  <figcaption>Figure 4: A 3D image of the shadow band swept by the cone from an obiting exoplanet, next to a side orthgraaphic projection of that cone and the areas where grazing and full eclipses of that exoplanet can be seen (Source: Winn, 2010)</figcaption>
</figure>

The figure shows how an orbiting exoplanet has a shadow cone with angle $\Theta$
which satisfies the conditon:

$$
\sin \Theta = \frac{R_{*} + R_p}{r} \tag{13}
$$

where $r$ is the actual (non-projected) 3D distance. This cone is called the
**penumbra** and is shown by the thick lines on the right in figure 4 above.
Observer's inside this cone will see a full eclipse, so the impact paramter for
them will lie in the range $0 \leq b < 1$. The interior cone described by the
slimmer lines is called the **antumbra** and satisfies the condition:

$$
\sin \Theta = \frac{R_{*} - R_p}{r} \tag{14}
$$

The penumbra sweeps out a shadow band on a celestial sphere around the star, as
seen on the left of figure 4. Any observer must be located inside that shadow
band in order to observe the eclipse.

Other methods of detecting planets, such as the Doppler Method, can reveal an
exoplanet's eccentricity $e$ and argument of periapsis $w$. This works, briefly
explained, by taking advantage of the tiny orbit of the star around the system's
centre of mass. This presents as a tiny wobble, where the star's light will be
slightly blueshifted as the star moves towards the observer, and slightly
redshifted as it moves away.

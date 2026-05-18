---
title: Eclipse Basics
excerpt:
  An explanation of the geometry, probability and duration of eclipses, as well
  as the loss of light and limb darkening we should expect during an eclipse.
toc: true
---

## Geometry of eclipses

Consider a planet of radius $R_P$ and mass $M_P$ orbitting a star of radius
$R_*$ and mass $M_*$. Let's define the ratio of planet-to-star radius for future
reference as:

$$
k = \frac{R_P}{R_*} \tag{1}
$$

The distance between the star and the planet, $r$, is given by:

$$
r = \frac{a(1 - e^2)}{1 + e \cos f'} \tag{2}
$$

where $a$ is the semi-major axis and $f$ is the
[true anomaly](/ellipses/2026/05/10/ellipses-and-elliptical-orbits.html#true-anomaly),
an implicit function of orbital eccentricity $e$ and period $P$.

We can resolve this into Cartesian coordinate equations within our defined
coordinate system.

$$
X = -r \cos (\omega + f) \tag{3}
$$

$$
Y = -r \sin (\omega + f) \cos i \tag{4}
$$

$$
Z = r \sin (\omega + f) \sin i \tag{5}
$$

We can use the Pythagorean theorem to derive the projected distance on the sky
plane as:

$$
r_{sky} \equiv \sqrt{X^2 + Y^2} \tag{6}
$$

We can substitute in equations 3 and 4 for $X$ and $Y$ to get:

$$
r_{sky} = \frac{a(1-e^2)}{1 + e \cos f} \sqrt{1 - \sin ^2 {(\omega + f)} \sin^2 {i}} \tag{7}
$$

If an eclipse occurs, it will do so at a local minimum of $r_{sky}$. Minimising
this expression is long and difficult, but we can approximate by stating that
eclipses are centred around conjunctions, which are defined by $X=0$.
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
b_{tra} = \frac{a \cos i}{R_{*}} (\frac{1 - e^2}{1 + e \sin \omega}) \tag{10}
$$

$$
b_{occ} = \frac{a \cos i}{R_{*}} (\frac{1 - e^2}{1 - e \sin \omega}) \tag{11}
$$

We can simplify this further. For the common case where the stellar radius is
much smaller than the orbits semi-major axis, $R_{*} << a$, then the exoplanet's
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

<figure>
  <img src="/ellipses/assets/img/winn_eclipse_angle.png" width="700px" height="700px" frameborder="0">
  <figcaption>Figure 5: A 3D image of the shadow band swept by the cone from an obiting exoplanet, next to a side orthgraaphic projection of that cone and the areas where grazing and full eclipses of that exoplanet can be seen (Source: Winn, 2010)</figcaption>
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

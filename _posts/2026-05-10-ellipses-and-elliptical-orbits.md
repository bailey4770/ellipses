---
title: 1. Ellipses and elliptical orbits
excerpt: A brief exploration of elliptical orbits and Kepler's Second Law.
toc: true
---

## What is an ellipse?

**Technical definiton of ellipse**: for any point on the ellipse, the sum of
distances to each focus is constant.

See labelled diagram for an ellipse below for the names of the different
components.

<figure>
  <img src="/ellipses/assets/img/labelled_ellipse.png" alt="Labelled ellipse" />
  <figcaption>Figure 1: A labelled ellipse showing the semi-major axis, semi-minor axis, and distance from centre to focus.</figcaption>
</figure>

- Semi-major axis, $a$
- Semi-minor axis, $b$
- Distance from centre to focus, $c$

The distance from centre to focus, $c$ is geometrically related to the
semi-major and -minor axes by the equation:

$$
c^2 = a^2 - b^2 \tag{1}
$$

Here, we can define a new term - the eccentricty $e$ - which is related to $c$
and $a$ by:

$$
c = a e \tag{2}
$$

When $e=0$, then the ellipse is a special case - a circle. Ellipses have
eccentricities $0 \leq e < 1$. Where $e=1$, the ellipse is now unbound and
becomes a parabola, and where $e>1$ the eccentricity is so extreme that we refer
to the generated curve as a hyperbola.

## Elliptical orbits

Planet's have elliptical orbits around their star, which is found at one of the
focus points. Technically, both the star and planet have elliptical orbits
around the system's centre of mass, which is found at the shared focus of every
elliptical orbit of each object in the system. Understanding this is important
for understanding other methods for detecting exoplanets, such as the Doppler
Method. But for our purposes, the star's mass is usually so much greater than
the plantary mass, and the star's orbit so much smaller in comparison to the
planet's orbit, that it is helpful for us to simplify and imagine that the star
is fixed at the focus point of a planet's elliptical orbit around it.

The point on the orbit where the planet is closest to its star is called the
**periapsis**, or when the star is the Sun, it is called the **perihelion**. The
opposite point, where it is furthest from its star, is called the **apoapsis**,
or when the star is the Sun, it is called the **aphelion**.

<figure>
  <img src="/ellipses/assets/img/labelled_static_planet.png" alt="Static planet on an elliptical orbit" />
  <figcaption>Figure 2: A planet on an elliptical orbit, with periapsis and apoapsis labelled.</figcaption>
</figure>

## Anomalies and Kepler's Second Law

Kepler's Second Law states that a line from an object on an elliptical orbit to
the star at one of its focal points will sweep out equal areas during equal
intervals in time. This basically means that an object moves faster when its
closer to its star, and slower when its further away.

In order to accurately animate orbital motion with Kepler's Second Law, we must
understand elliptical anomalies.

Imagine a circle with radius $a$ centred at the origin.

<figure>
  <img src="/ellipses/assets/img/labelled_anomalies.png" alt="Ellipse with hypothetical circle, with eccentric, mean, and true anomaly labelled" />
  <figcaption>Figure 3: An ellipse with its hypothetical circle, showing the eccentric anomaly E, mean anomaly M, and true anomaly ν.</figcaption>
</figure>

### Mean Anomaly

Consider a hypothetical planet completing a full orbit in the same time period
$T$ as our real planet on its elliptical orbit.

This hypothetical planet has constant angular speed, described by:

$$
M(t) = \frac{2 \pi t}{T} \tag{3}
$$

The mean anomaly $M$ is the angle from the origin between the periapsis and the
point $F$ on the imaginary orbit for given $t$, when $t=0$ at the periapsis.

### Eccentric Anomaly

Take the point $P$ on the ellipitcal orbit, where the planet actually is at time
$t$, and project upwards to the imaginary circle at point $Q$.

The eccentric anomaly $E$ is the angle from the origin between the periapsis and
point $Q$.

### True Anomaly

True anomaly $\nu$ is simply the angle from the star between the periapsis and
the planet's real position on the ellipitcal orbit at time $t$.

## Computing eccentric anomaly from mean anomaly

Kepler found the below equation linking the mean and eccentric anomaly:

$$
M = E - e \sin E \tag{4}
$$

So to animate our elliptical orbit with Kepler's Second Law, we can solve for
$E(t)$ to find where the planet should be on the hypotehtical circle, then
project straight down until we meet the ellipse.

However, there is a problem. The above formula cannot be solved for $E$ in
closed form. Enter: Newton's iterative method for finding the root of an
equation.

We can rewrite the above equation to

$$
f(E) = E - e \sin E - M \tag{5}
$$

which turns the problem into a root finding problem - we can find $E$ from $M$
where $f(E) = 0$.

Let's visualise this equation graphically. We can graph $f(E)$ for given values
of $e$ and $M$. Here, $e = 0.7$ and $M=3$:

<figure>
  <img src="/ellipses/assets/img/f_E.png" alt="f(E) graph" />
  <figcaption>Figure 4: Graph of f(E) for e = 0.7 and M = 3, showing the root to be found by Newton's method.</figcaption>
</figure>

Then, we take an initial guess. For us, a reasonable first guess is $E_0 = M$.
Using the below equation, we can refine our guess to find the value of $E$ where
$f(E) = 0$:

$$
E_{n+1} = E_n - \frac{f(E_n)}{f'(E_n)} \tag{6}
$$

Let's understand what we're doing here. The numerator, $f(E_n)$, tells us
whether we're above or below the root, and by how far. The denominator tells us
the gradient of the curve at this value of $E$. Looking at the curve, we know
the gradient will be shallow far from the root and steep close to the root. When
the gradient is shallow, the denominator will be small, so the step from $E_n$
to $E_{n+1}$ will be large, and vice versa when the gradient is steep.

We can substitute $f(E) = E - e \sin E - M$ and $f'(E) = 1 - e \cos E$ (knowing
that the first derivative of $e \sin E$ is $e \cos E$) to write the equation in
terms that we can calculate:

$$
E_{n+1} = E_n - \frac{E_n - e \sin E_n - M}{ 1 - e \cos E_n} \tag{7}
$$

For our purposes, only 5 iterations of the above formula will give a value of
$E$ so that $f(E)$ is extremely close to $0$.

We can then derive cartesian coordinates of the elliptical orbit using the below
equations:

$$
x = a \cos E \tag{8}
$$

$$
y = b \sin E \tag{9}
$$

And drawing these coordinates in discrete time intervals gives the below
animation, showing Kepler's Second Law in action.

<figure>
  <img src="/ellipses/assets/img/elliptical_orbit.gif" alt="Elliptical orbit animation" />
  <figcaption>Figure 5: Animation of a planet on an elliptical orbit, demonstrating Kepler's Second Law.</figcaption>
</figure>

The object has an elliptical orbit around the star, moving quickly near the
periapsis and slowly near the apoapsis.

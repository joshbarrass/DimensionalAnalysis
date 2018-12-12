# Dimensional Analysis #

Simple code for performing dimensional analysis.

This code was written to work with Python 3, but should be equally
compatible with Python 2.7. Only thing that works kind of weirdly is
TEMPERATURE.

## How To Use ##

A lot of simple equations have already been put in as Dimensions
objects. The basic dimensions, length [L], mass [M], current [I],
temperature [θ], time [T], and light intensity [J], are defined as
constants LENGTH, MASS, CURRENT, TEMPERATURE, TIME, LIGHT_INTENSITY.

These have then been used to define dimensions for other quantities,
for example `FORCE` is defined as `MASS * ACCELERATION`, and
`ACCELERATION` as `LENGTH * TIME**-2`. All of these are found at the
bottom of the time. 

If you need to create a new set of dimensions, you can create a
Dimensions object. This is done as:

```
d = Dimensions("[M]^2[L]")
```

This example would create an [M] squared multiplied by [L] dimension,
which can then be used in conjunction with other dimensions. Negative
powers can also be used.

Dimensions can be multiplied, divided, exponentiated, added, etc.. Any
dimensions can be multiplied or divided, yielding a new dimension,
whereas only matching dimensions can be added or subtracted and will
yield the same dimension. Trying to add/subtract mismatched dimensions
will cause an error.

If your equation relies on some sort of function, where the function
must have dimensionless arguments, you can use `function()` in your
equation. This has also been mapped to `sin()`, `cos()`, `tan()`, and
`exp()` for convenience. An error will be raised if the dimensions
passed to function are not dimensionless.

Dimensions can be compared with each other. For example, `FORCE ==
MASS * ACCELERATION` will return `True`. This allows you to confirm
that an equation is dimensionally consistent.



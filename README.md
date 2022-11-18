<h1 align="center">
  Rotation Trigonometry
</h1>

This project is a uses uses a general rotation matrix to calculate the rotation
of a model consisting of [x,y,z] vertices to represent each point in it's shape.
The models consist of a sequence of numpy arrays to represent each vertex and
a sequence of tuples with 2 indexes to represent the edges of the model. The
model of choice is generated at the start and rendered using pygame.

## Demo

<div align="center">
    <img src="/media/demo_cube.gif" height="400">
    <img src="/media/demo_sphere.gif" height="400">
</div>

## Setup

See [main](https://github.com/Serphyus/Rotation-Trigonometry.git) repository.

## Usage

run the main.py located in the src directory

```
py src/main.py
```

choose model to render

```
Available Models:
1  : cube
2  : sphere
3  : function

> _
```

### To change the function

To change the displayed function edit the return value of `f_main` in `src/main.py`

Various functions will provide various shapes

####Linear functions

<div align="center">
    <img src="/media/demo_cone.gif" height="400" alt="Linear function gif">
</div>

####Constants

<div align="center">
    <img src="/media/demo_sylinder.gif" height="400" alt="Constant function gif">
</div>

####Squared functions

<div align="center">
    <img src="/media/demo_dish.gif" height="400" alt="Squared function gif">
</div>

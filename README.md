<h1 align="center">
  Solids of Revolution
</h1>

The motivation for this fork was to create and render three-dimensional solids of revolution. The function of a given interval is broken up, and a circle of points with radius f(x) is calculated using rotation matrices for each of the slices.

## Demo

<div align="center">
    <img src="/media/showcase_cone.gif" height="400">
    <img src="/media/showcase_dish.gif" height="400">
</div>

## Requirements

- Locally installed python 3
- Git

## Setup

Clone repository and execute installation script for required packages

```
git clone https://github.com/Nuddel69/Solids-of-revolution.git
cd Solids-of-revolution
./prerequisites.sh
```

You may need to run `chmod +x prerequisites.sh` in order to execute the shell script. Alternatively you may run the pip install command directly:

```
pip install -r requirements.txt`
```

## Usage

### Basic usage

Run the main.py located in the src directory

```
py src/main.py
```

Choose model to render

```
Available Models:
1  : cube
2  : sphere
3  : function

> _
```

### Configuring the function parameters

All configuration for the Function model can be found in `assets/FunctionConfig.json`.

To change the displayed function edit the `Function` parameter.
The displayed interval is defined by `a` and `b`.

To adjust the accuracy of the displayed model edit `Ring Accuracy` and `Interval Accuracy`. `Ring Accuracy` adjusts the number of points for each slice. `Interval Accuracy` adjusts how many slices is generated between each value `x`. The latter of these takes a number `<0.0, 1.0>` as an argument.

> **Note**  
> Setting either of these accuracies too high will severely affect performance.

<br>
Various functions will provide various shapes

#### Linear functions

<div align="center">
    <img src="/media/demo_cone.gif" height="400" alt="Linear function gif">
</div>

#### Constants

<div align="center">
    <img src="/media/demo_sylinder.gif" height="400" alt="Constant function gif">
</div>

#### Squared functions

<div align="center">
    <img src="/media/demo_dish.gif" height="400" alt="Squared function gif">
</div>

### Demo mode

If you want to render the model **without** the GUI or controls you can use _demo mode_. Simply execute the main.py file with the -d (--demo) flag and choose a model. While the model will now move on it's own, regular controls will still affect it's movement.

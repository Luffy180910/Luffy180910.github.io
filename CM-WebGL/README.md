
Coursework for Module: CM20210: Visual Computing

## Outline of Objectives:
- Render in 3D Cube model & texturize to react with light
- Allow for rotation of cube & camera in all axes
- Render in Bunny OBJ Model & Fit model into cube

Extension: I've imported physics to create a dice-rolling animation which detects the value of the dice

### Overview of Code:

- Written in JavaScript, using the three.js framework
- three.js effectively ports WebGL (based on OpenGL) to JavaScript
- Allows us to construct and manipulate 3D scenes in the browser

Code is based in HTML file, under <script> tags

## How to run:

### Dependencies:
- three.js: Base framework to implement OpenGL in JavaScript
- OBJLoader.js: Module, allows for importing .OBJ files
- dat.min.gui.js: Module, adds integrated GUI support
- Cannon-es: Module, adds physics support for dice rolling

### Assets:
- Dice textures for faces 1-6
- bunny-5000.obj

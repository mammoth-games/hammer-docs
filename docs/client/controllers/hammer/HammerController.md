# HammerController

## Description

Binds winding up and swinging to a context action.

## API

#### :GetWindUpAlpha()
Returns a linear value in [0, 1] for progression through the wind up animation.

#### :GetPowerAlpha()
Returns a nonlinear value in [0, 1] for hammer charge based on progression through wind up.

#### :GetHammerDirection()
Returns the direction of the hammer collider or nil.

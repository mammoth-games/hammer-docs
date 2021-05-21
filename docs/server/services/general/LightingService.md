# LightingService

!!! warning
    This Page needs more info, Contact AstroCode#9853 and bug him to add more info to this page.

## Description

Facilitates applying Lighting, Sky, and PostEffect changes and smoothly tweens properties. It purposefully does not support BlurEffects, as the MVP did not need it. In the future, it would be helpful to be able to individually change PostEffects.

## API

#### ClockService:newTimer(duration: number?, name: string?)
    Documentation Not Found

#### :ResetProperties()

Reset the Lighting, Sky, and PostEffects properties to default
	
#### :ApplyProperties(properties: Dictionary, lightingFolder: Folder?)

`properties` is a string-indexes dictionary of properties for Lighting.
    
`lightingFolder` is a folder containing a Sky object and/or PostEffect objects.
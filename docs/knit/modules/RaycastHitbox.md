# RaycastHitbox

!!! info
    This Page needs more info, Contact AstroCode#9853 and bug him to add more info to this page.

**RaycastHitbox**
**by AstroCode**

## Description

A point caster must be named `"$Caster.Point"`.
A segment caster must have two attachments named
`"$Caster.Segment.UniqueName.0"`  <-- this one is the origin of the raycast
`"$Caster.Segment.UniqueName.1"`  <-- this one is the tip of the raycast

## API

#### RaycastHitbox:Destroy()
    Documentation Not Found

#### RaycastHitbox:Enable()
    Documentation Not Found

#### RaycastHitbox:Disable()
    Documentation Not Found

#### RaycastHitbox:EnableDebug()
    Documentation Not Found

#### RaycastHitbox:DisableDebug()
    Documentation Not Found

#### RaycastHitbox.OnHit:Connect(...)
    Documentation Not Found
    
#### RaycastHitbox.new(object: Instance, whitelistedTags: {string})

The Instance with caster attachments as descendants whitelistedTags: The tags which raycasting will whitelist

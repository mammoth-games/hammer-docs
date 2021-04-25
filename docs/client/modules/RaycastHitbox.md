# RaycastHitbox

	A point caster must be named "$Caster.Point".
	A segment caster must have two attachments named
	"$Caster.Segment.UniqueName.0"  <-- this one is the origin of the raycast
	"$Caster.Segment.UniqueName.1"  <-- this one is the tip of the raycast
	
	RaycastHitbox.new(object: Instance, whitelistedTags: {string})
		object: The Instance with caster attachments as descendants
		whitelistedTags: The tags which raycasting will whitelist
	RaycastHitbox:Destroy()
	RaycastHitbox:Enable()
	RaycastHitbox:Disable()
	RaycastHitbox:EnableDebug()
	RaycastHitbox:DisableDebug()
	RaycastHitbox.OnHit:Connect(...)
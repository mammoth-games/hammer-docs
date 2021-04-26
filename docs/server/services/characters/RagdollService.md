# RagdollService

### Description

    Description Not Found

### API

	Applies and resets player ragdolls. This is done by adding/removing the "Ragdoll" tag from
	a character. The Ragdoll component handles the actual ragdolling implementation. Clients can
	also tell RagdollService to reset their ragdoll by calling Client:GetUp().
	
	:ApplyRagdoll(character)
		Adds the "Ragdoll" tag to the character and fires the Client.IsRagdolledChanged remote.
	:RemoveRagdoll(character)
		Removes the "Ragdoll" tag from the character and fires the Client.IsRagdolledChanged remote.
	Client:GetUp(player: Player)
		Called by clients. Removes their ragdoll.
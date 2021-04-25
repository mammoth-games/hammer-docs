# BuildConstraintsRig

	This module builds the ragdoll. It returns a dictionary of joints and a dictionary of
	NoCollisionConstraints. The joint dictionary is structured like this:

	{
		Head = {
			Attachment0 = [Attachment object],
			Attachment1 = [Attachment object],
			Constraint = [BallSocketConstraint object],
			Motor = [Motor6D object],
			Offset = [CFrame of Attachment0 offset from Motor.C0]
		},
		LeftArm = {...},
		RightArm = {...},
		LeftLeg = {...},
		RightLeg = {...},
	}

	The NoCollisionConstraints dictionary is structured like this:

	{
		Arms = {
			[NoCollisionConstraint],
			[NoCollisionConstraint],
			...
		},
		Legs = {...},
		Hips = {...}
	}

	Each index in the NoCollisionConstraints dictionary has the minimum amount of
	NoCollisionConstraint objects required to connect all of the parts in each index of
	Constants.ANIMATE_COLLISION_FILTERS to every other part in the index.
# RagdollComponent

### Description

	Description Not Found

## API
	
**Ragdoll Component
by Astro and Tomgie**

Ragdoll the tagged character and un-ragdoll when the tag is removed via Janitor.

How to use:
Assign "Ragdoll" tag to the character model.
Unassign the tag to return the character to its normal state.

# RagdollConstants

## Description

    Description Not Found

## API

#### This is a collection of constants that describe the ragdoll.

`JOINT_PROPERTIES:` The properties of each joint in the ragdoll.

`COLLISION_FILTERS:` The ragdoll cannot properly fall if its limbs are colliding. This describes the NoCollisionConstraints to create so that the limbs do not collide with each other.

`PART_TO_JOINT_MAP:` A map between the names of the parts and the names of their respective joints.

# BuildConstraintsRig

## Description

    Description Not Found

## API

#### This module builds the ragdoll. It returns a dictionary of joints and a dictionary of NoCollisionConstraints. The joint dictionary is structured like this:

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


#### The NoCollisionConstraints dictionary is structured like this:

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
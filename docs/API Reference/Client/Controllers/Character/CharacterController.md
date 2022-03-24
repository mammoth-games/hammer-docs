# CharacterController

## Description

Provides character-related fields and signals for client code.

## API

### Fields

#### .Character
The player's character

#### .Humanoid
The player's Humanoid

#### .IsLoaded
Set to true before CharacterLoaded fires. Set to false on cleanup.

#### .RootPart
	
### Signals:

#### .CharacterAdded
Fires immediately when the character is added.

#### .CharacterLoaded
Fires after calling WaitForChild on Humanoid, HumanoidRootPart, and Head.

### Methods

#### :CreateDeathJanitor()
Returns a janitor that will be cleaned up when the character dies.

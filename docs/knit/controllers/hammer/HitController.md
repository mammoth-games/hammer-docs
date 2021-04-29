# HitController

### Description

	HitController
	
	Determines what to do when the hammer hits something.

### API

	:_UpdateDebounceLists()
		Keeps a list of times for when individual objects were hit and a list of times for when
		individual characters were hit. If an object/character is on the list when they are hit,
		the hit does not register. They are removed from the list after a debounce time.
	:ObjectHit()
		Called by HammerController for the RaycastHitbox hits something. Player character hits
		are sent to the server via HitService:CharacterHit(). Object hits have custom logic for
		what to do with them. NPC hits do nothing.

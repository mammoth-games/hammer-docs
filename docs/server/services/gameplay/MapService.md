# MapService

	API:
	:LoadMap(gameModeName: string, mapName: string)
		Yielding method. Loads the terrain/parts for a given map.
	:UnloadMap()
		Clears all terrain and removes all children from Map folder.
	:GetRandomGameModeMap(gameModeName: string)
	:GetGameModeMaps(gameModeName: string)
	:GetMapContainer()
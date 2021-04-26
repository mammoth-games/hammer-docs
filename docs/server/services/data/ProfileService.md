# PlayerCharacterService

	Makes player data accessible for other scripts
	
	Ex.
	local profile = ProfileService:GetProfile(userid)
	profile:AddCurrency("Gold", 5)
	profile:GetCurrencyOfType("Gold")

	API:
	ProfileService:GetProfile(userId: number)
	ProfileService:GetProfiles()
	ProfileService:UpdateTopPlayer()
	
	Profile:GetCurrencyOfType(name: string)
	Profile:GetAllCurrency()
	Profile:AddCurrencyOfType(name: string, amount: number)
	Profile:SubtractCurrencyOfType(name: string, amount: number)
	Profile:GetCosmeticsOfType(cosmeticType: string)
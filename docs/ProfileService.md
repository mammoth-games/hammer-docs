# ProfileService

    {Madwork}

    -ProfileService---------------------------------------
	(STANDALONE VERSION)
	DataStore profiles - universal session-locked savable table API
	
	Official documentation:
		https://madstudioroblox.github.io/ProfileService/

	DevForum discussion:
		https://devforum.roblox.com/t/ProfileService/667805
	
	WARNINGS FOR "Profile.Data" VALUES:
	 	! Do not create numeric tables with gaps - attempting to replicate such tables will result in an error;
		! Do not create mixed tables (some values indexed by number and others by string key), as only
		     the data indexed by number will be replicated.
		! Do not index tables by anything other than numbers and strings.
		! Do not reference Roblox Instances
		! Do not reference userdata (Vector3, Color3, CFrame...) - Serialize userdata before referencing
		! Do not reference functions
		
	WARNING: Calling ProfileStore:LoadProfileAsync() with a "profile_key" which wasn't released in the SAME SESSION will result
		in an error! If you want to "ProfileStore:LoadProfileAsync()" instead of using the already loaded profile, :Release()
		the old Profile object.
		
	Members:
	
		ProfileService.ServiceLocked         [bool]
		
		ProfileService.IssueSignal           [ScriptSignal](error_message, profile_store_name, profile_key)
		ProfileService.CorruptionSignal      [ScriptSignal](profile_store_name, profile_key)
		ProfileService.CriticalStateSignal   [ScriptSignal](is_critical_state)
	
	Functions:
	
		ProfileService.GetProfileStore(profile_store_name, profile_template) --> [ProfileStore]
			-- WARNING: Only one ProfileStore can exist for a given profile_store_name in a game session!
		
		* Parameter description for "ProfileService.GetProfileStore()":
		
			profile_store_name   [string] -- DataStore name
			profile_template     []:
				{}                        [table] -- Profiles will default to given table (hard-copy) when no data was saved previously
				
	Members [ProfileStore]:
	
		ProfileStore.Mock   [ProfileStore] -- Reflection of ProfileStore methods, but the methods will use a mock DataStore
		
	Methods [ProfileStore]:
	
		ProfileStore:LoadProfileAsync(profile_key, not_released_handler) --> [Profile / nil] not_released_handler(place_id, game_job_id)
		ProfileStore:GlobalUpdateProfileAsync(profile_key, update_handler) --> [GlobalUpdates / nil] (update_handler(GlobalUpdates))
			-- Returns GlobalUpdates object if update was successful, otherwise returns nil
		
		ProfileStore:ViewProfileAsync(profile_key) --> [Profile / nil] -- Notice #1: Profile object methods will not be available;
			Notice #2: Profile object members will be nil (Profile.Data = nil, Profile.MetaData = nil) if the profile hasn't
			been created, with the exception of Profile.GlobalUpdates which could be empty or populated by
			ProfileStore:GlobalUpdateProfileAsync()
			
		ProfileStore:WipeProfileAsync(profile_key) --> is_wipe_successful [bool] -- Completely wipes out profile data from the
			DataStore / mock DataStore with no way to recover it.
		
		* Parameter description for "ProfileStore:LoadProfileAsync()":
		
			profile_key            [string] -- DataStore key
			not_released_handler = "ForceLoad" -- Force loads profile on first call
			OR
			not_released_handler = "Steal" -- Steals the profile ignoring it's session lock
			OR
			not_released_handler   [function] (place_id, game_job_id) --> [string] ("Repeat" / "Cancel" / "ForceLoad")
				-- "not_released_handler" will be triggered in cases where the profile is not released by a session. This
				function may yield for as long as desirable and must return one of three string values:
					["Repeat"] - ProfileService will repeat the profile loading proccess and may trigger the release handler again
					["Cancel"] - ProfileStore:LoadProfileAsync() will immediately return nil
					["ForceLoad"] - ProfileService will repeat the profile loading call, but will return Profile object afterwards
						and release the profile for another session that has loaded the profile
					["Steal"] - The profile will usually be loaded immediately, ignoring an existing remote session lock and applying
						a session lock for this session.
						
		* Parameter description for "ProfileStore:GlobalUpdateProfileAsync()":
		
			profile_key      [string] -- DataStore key
			update_handler   [function] (GlobalUpdates) -- This function gains access to GlobalUpdates object methods
				(update_handler can't yield)
		
	Members [Profile]:
	
		Profile.Data            [table] -- Writable table that gets saved automatically and once the profile is released
		Profile.MetaData        [table] (Read-only) -- Information about this profile
		
			Profile.MetaData.ProfileCreateTime   [number] (Read-only) -- os.time() timestamp of profile creation
			Profile.MetaData.SessionLoadCount    [number] (Read-only) -- Amount of times the profile was loaded
			Profile.MetaData.ActiveSession       [table] (Read-only) {place_id, game_job_id} / nil -- Set to a session link if a
				game session is currently having this profile loaded; nil if released
			Profile.MetaData.MetaTags            [table] {["tag_name"] = tag_value, ...} -- Saved and auto-saved just like Profile.Data
			Profile.MetaData.MetaTagsLatest      [table] (Read-only) -- Latest version of MetaData.MetaTags that was definetly saved to DataStore
				(You can use Profile.MetaData.MetaTagsLatest for product purchase save confirmation, but create a system to clear old tags after
				they pile up)
		
		Profile.GlobalUpdates   [GlobalUpdates]
		
	Methods [Profile]:
	
		-- SAFE METHODS - Will not error after profile expires:
		Profile:IsActive() --> [bool] -- Returns true while the profile is active and can be written to
			
		Profile:GetMetaTag(tag_name) --> value
		
		Profile:Reconcile() -- Fills in missing (nil) [string_key] = [value] pairs to the Profile.Data structure
		
		Profile:ListenToRelease(listener) --> [ScriptConnection] (place_id / nil, game_job_id / nil) -- WARNING: Profiles can be released externally if another session
			force-loads this profile - use :ListenToRelease() to handle player leaving cleanup.
			
		Profile:Release() -- Call after the session has finished working with this profile
			e.g., after the player leaves (Profile object will become expired) (Does not yield)

		Profile:ListenToHopReady(listener) --> [ScriptConnection] () -- Passed listener will be executed after the releasing UpdateAsync call finishes;
			--	Wrap universe teleport requests with this method AFTER releasing the profile to improve session lock sharing between universe places;
			--  :ListenToHopReady() will usually call the listener in around a second, but may ocassionally take up to 7 seconds when a release happens
			--	next to an auto-update in regular usage scenarios.
		
		-- DANGEROUS METHODS - Will error if the profile is expired:
		-- MetaTags - Save and read values stored in Profile.MetaData for storing info about the
			profile itself like "Profile:SetMetaTag("FirstTimeLoad", true)"
		Profile:SetMetaTag(tag_name, value)
		
		Profile:Save() -- Call to quickly progress global update state or to speed up save validation processes (Does not yield)

		
	Methods [GlobalUpdates]:
	
	-- ALWAYS PUBLIC:
		GlobalUpdates:GetActiveUpdates() --> [table] {{update_id, update_data}, ...}
		GlobalUpdates:GetLockedUpdates() --> [table] {{update_id, update_data}, ...}
		
	-- ONLY WHEN FROM "Profile.GlobalUpdates":
		GlobalUpdates:ListenToNewActiveUpdate(listener) --> [ScriptConnection] listener(update_id, update_data)
		GlobalUpdates:ListenToNewLockedUpdate(listener) --> [ScriptConnection] listener(update_id, update_data)
		-- WARNING: GlobalUpdates:LockUpdate() and GlobalUpdates:ClearLockedUpdate() will error after profile expires
		GlobalUpdates:LockActiveUpdate(update_id)
		GlobalUpdates:ClearLockedUpdate(update_id)
		
	-- EXPOSED TO "update_handler" DURING ProfileStore:GlobalUpdateProfileAsync() CALL
		GlobalUpdates:AddActiveUpdate(update_data)
		GlobalUpdates:ChangeActiveUpdate(update_id, update_data)
		GlobalUpdates:ClearActiveUpdate(update_id)
		
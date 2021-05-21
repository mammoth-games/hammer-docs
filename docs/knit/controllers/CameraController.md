# CameraController

## Description

Exposes methods for manipulating the camera. Internally, it also assigns the Gameplay camera on spawn.

There are three cameras available: Gameplay, Static, and Interactable. Gameplay is over-the-shoulder with the mouse locked. Static unlocks the mouse and the camera does not follow the character; this is for cutscenes. Interactable unlocks the mouse and does not let you pan, but the camera still follows your character; this is for accessing menus.

For camera modes where the mouse is unlocked, an invisible TextButton with Modal = true is set to visible. This forces the mouse to be moveable.

## API

#### :FollowPath(path: {Vector3})

#### :GetCameraCFrame()

#### :LookAt(from: Vector3, to: Vector3?)
If no to is specific, from will be use as the to and the Camera will stay at its current position.
	
#### :SetCameraMode(cameraMode: CameraModeEnum)

        Documentation Not Found

#### :SetCameraOffset(cameraOffset: Vector3)

    Documentation Not Found

### CameraModule changes:
Set computer camera movement to CameraToggle
, Set touch camera movement to Classic

!!!! note
    Does not work with Follow on mobile

#### CameraUI:
Comment out the implementation for `CameraUI.setCameraModeToastEnabled`
Comment out the implementation for `CameraUI.setCameraModeToastOpen`

#### ClassicCamera:
Comment out the block that calls `self:GetCameraToggleOffset()`
Add a local offset at the end of `ClassicCamera:Update()`

#### CameraInput:
Set holdPan and togglePan to true
Comment out the implementation for `CameraInput.enableCameraToggleInput()`
Comment out the implementation for `CameraInput.disableCameraToggleInput()`

#### CameraModule:
Force return `CameraModule.new()` at the bottom

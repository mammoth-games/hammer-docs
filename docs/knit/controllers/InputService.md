# InputService

### Description

	InputService
	
	Helps with getting the player's input type. It makes an initial guess based on
	UserInputService.TouchEnabled and GuiService:IsTenFootInterface(). The possible input types
	are Gamepad, Keyboard, and Touch.

### API

	.InputTypeEnum
	.InputTypeChanged signal
	:GetInputType()

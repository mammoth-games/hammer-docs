# ClockService

## Description

Create timers that count down from a specified time or stopwatches that count up from 0.
Timers use Signals to be able to fire functions when they complete.
	
#### Example

```lua
local timer = ClockService:newTimer(10)
timer.Completed:Connect(function() end)
timer.Completed:Wait()
```

## API

#### ClockService:newTimer(duration: number?, name: string?)
    Documentation Not Found

#### ClockService:newStopwatch(name: string?)
    Documentation Not Found

#### ClockService:GetTimer(name: string)
    Documentation Not Found

#### ClockService:GetStopwatch(name: string)
    Documentation Not Found

#### Timer:GetTime()
    Documentation Not Found

#### Timer:Destroy()
    Documentation Not Found

	
#### Stopwatch:GetTime()
    Documentation Not Found

#### Stopwatch:Benchmark()
    Documentation Not Found

#### Stopwatch:Destroy()
    Documentation Not Found
	
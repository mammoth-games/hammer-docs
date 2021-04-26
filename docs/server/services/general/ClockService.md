# ClockService

### Description

Create timers that count down from a specified time or stopwatches that count up from 0.
Timers use Signals to be able to fire functions when they complete.
	
	Ex.
	local timer = ClockService:newTimer(10)
	timer.Completed:Connect(function() end)
	timer.Completed:Wait()

### API

	API:
	ClockService:newTimer(duration: number?, name: string?)
	ClockService:newStopwatch(name: string?)
	ClockService:GetTimer(name: string)
	ClockService:GetStopwatch(name: string)
	k
	Timer:GetTime()
	Timer:Destroy()
	
	Stopwatch:GetTime()
	Stopwatch:Benchmark()
	Stopwatch:Destroy()
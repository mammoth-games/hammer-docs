# Knit Modifications

The only modifications we made were to Util.Loader, the rest were done by pobammer. All modules received lints. Modules that only received lints are not listed.

Maid was completely replaced with Janitor.

## Swap Maid with Janitor
* Util.Signal
* Util.Streamable
* Util.StreamableUtil

## Util.Component
Replace Maid with Janitor
A LOT

## Util.Loader
* Add the ability to disable a module with a "Disabled" boolean attribute.
* Warn if a controller or service is disabled.
* Add the ability to make a module as not a service or controller with "IsService" and "IsController" boolean attributes.
* Warn if a module was ignored because it was marked as not a service or controller.

## Util.Maid
Replace with Janitor

## Util.TableUtil
* Add examples
* Swap next for pairs and ipairs
* Alphabetize the functions
# AbelianTable

  

### Description

**Ethan Curtiss (AstroCode)**
**29 April 2021**

Wraps a 2D dictionary such that each node is connected to every other node (and optionally itself) by a value -- and without repeats.

For example, consider the nodes {a, b, c, d, e} with "x" being the connected values.

⠀|A | B | C | D | E | 
-|- |- | - | - | - |
**A**| X |
**B**| X | X |
**C**| X | X | X |
**D**| X | X | X | X |
**E**| X | X | X | X | X |

The key benefit to this module is that two nodes are connected by the same value regardless of retrieval order. That is, `data[a][b] == data[b][a]`.
If you choose for the nodes to not be self-connected, then the diagonal will be empty.

!!! note
    Attempting to set a value between two connected nodes to nil will revert to the userdata `SelfConnectedList.None`. This is because setting the value to nil would lose the connection.


### API

	.new(nodes, defaultValue, connectToSelf)
	:Add(node, value)
	:Remove(node, value)
	:Set(node0, node1, value)
	:Get(node0, node1, value)
	:SetAll(value)


#### .new(nodes: {any}, defaultValue: any, connectToSelf: boolean?)

`nodes` is an array of nodes to connect. Passing duplicate or nil nodes will give unexpected results.

`defaultValue` is what all of the values are initially set to. This defaults to `SelfConnectedList.None`.

`connectToSelf` is if nodes should be connected to themselves. This defaults to true.

Complexity: O(n^2)

#### :Add(node, value)

Adds a node and connects it to the rest. The new node connects to itself if the original data structure had connectToSelf = true.

Complexity: O(n)

#### :Remove(node)
Removes the node.

Complexity: O(n)

#### :Set(node0, node1, value)
Sets the connected value of node0 and node1. The order of the arguments does not matter.

Complexity: O(1)

#### :Get(node0, node1)
Gets the connected value of node0 and node1. The order of the arguments does not matter.

Complexity: O(1)

#### :SetAll(value)
Set every value to `value`.

Complexity: O(n^2)
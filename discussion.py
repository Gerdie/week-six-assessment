"""

1. Runtime

1.1 When calculating the Big O notation for a particular algorithm,
it’s necessary to consider the length of time it takes for the algorithm to run
as the algorithm’s workload approaches infinity. You can think of the workload
as the number of tasks required to complete a job. What determines the workload
of figuring out whether your box of animal crackers contains an elephant?


--The number of crackers in the box --> n. O(n)


1.2 Order the following runtimes in descending order of efficiency (that is,
fastest runtimes first, slowest last) as n approaches infinity:

--O(1)
--O(log n)
--O(n)
--O(n log n)
--O(n2)
--O(2n) (i.e. 2 to the n-th power)


2. Stacks and Queues

2.1 In the following cases, would a stack or queue be a more appropriate data structure?

--The process of loading and unloading pallets onto a flatbed truck. STACK

--Putting bottle caps on bottles of beer as they roll down an assembly line QUEUE

--Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2) STACK

2.2 Describe two more situations where a queue would be an appropriate data structure.

--A game server. The first person in queue should be the first to get into the game.
--The line for the Bank of America chat service. It should automatically connect
    to the person who has been waiting the longest.

2.3 Describe two more situations where a stack would be an appropriate data structure.

--Class inheritance. A script should look at the most recent class first, when looking
    for a class attribute or method.
--Eating pringles. You have to eat the one on top first, which was probably the last to
    go into the box.


3.Linked Lists

3.1 Given the linked list below, which are the nodes? What is the data for each node?
Where is the head? Where is the tail? (Please be as specific as possible — exactly
which parts of the diagram correspond to each part? Arrows? Boxes? Text?)

--The nodes are not named in this diagram. The data for the first node--the head--is "Apple".
    The head node's next attribute points to the second node, with the data of "Berry" and a 
    next attribute pointing to the third node, "Cherry", which has a next attribute of None. That 
    third node would be the tail, if the LLIST class had a tail attribute, which it does not seem
    to have in this diagram.

3.2 What’s the difference between doubly- and singly-linked lists?

--Each node in a singly-linked lists has a "next" attribute. Each node in a doubly-
    linked list has a "previous" attribute in addition to a "next" attribute. 

3.3 Why is it faster to append to a linked list if we keep track of the tail as an attribute?

--Because then we can go straight to the "tail" node to add a new node (and change the current
    tail's "next" attribute to point to the new node), which is a runtime of O(1), instead of having
    to navigate the entire length of the linked-list to get to the tail, which would have a runtime
    of O(n).


4. Trees

4.1 Given the tree above, in what order would a Breadth First Search (BFS) algorithm
visit each node until finding burrito (starting at food)? Just list the order of
nodes visited; no need to recreate the state of the algorithm data in your answer.

--Food, Italian, Indian, Mexican, lasagna, pizza, tikka masala, saag, burrito

4.2 Given the tree above, in what order would a Depth First Search (DFS) algorithm
visit each node until finding Chicago-style (starting at food)? Just list the order
of nodes visited; no need to recreate the state of the algorithm data in your answer.

--Food, Italiam, lasagna, pizza, thin crust, Chicago-style

4.3 How is a binary search tree different from other trees?

--It is structured in an order that makes it easier to navigate. For instance, it would
    be alphabetized. You would know exactly which branch to go down to find a word beginning
    with "g" --> after "f" and before "h".

"""
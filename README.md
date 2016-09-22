# monte_hall
Simulates the classic [Monte Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem), which is summarized as follows:

> There are three doors. Behind one of the doors is a prize, the other two contain nothing. After picking one of the doors, you are shown a prize-less door (so there is still your guessed door plus one other left) and the host asks if you want to switch your pick. The question is 'Is it more advantageous to do so'?

It *is* statistically more beneficial to you to switch. Here is why:

At the start, each door has a 1/3 chance of having the prize. This means that, when you select a door, the other two doors comprise the remaining 2/3 chance. When the host shows you an empty door of the other two you didn't pick, the chance that it is the remaining door holds that full 2/3 chance. The probability distribution does not magically reduce down to a 50-50 chance, the original distributions hold. Thus, since 2/3 > 1/3, it is to your advantage to switch.

# the program
After discussing it with a colleague who didn't believe the analysis, I've written a Python script that simulates the behavior. The basic process is this:

 1. Randomly select a door to hold the prize
 2. Randomly select the guess
 3. Show the bad door
 4. Compare guess to bad door & increment the staying variable if necessary
 5. Change the guess (based on the bad door & the initial guess) & increment the switching variable if necessary
 6. Repeat

At 5000 iterations, we get success rates (successes / trials) of roughly 1/3 for staying and 2/3 for switching, as expected.

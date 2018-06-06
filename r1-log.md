# #100DaysOfCode Log - Round 1 - Jason M. Pittman

The log of my #100DaysOfCode challenge. Started on [April 11th, Wednesday, 2017].

## Log

### D1R1 
Worked on a text-based L-System generator in Python. The rule input, rule processor, and seed input all work. Finish tomorrow with L-System engine. Need to complete the README too.

### D2R1
Continued work on the text-based L-System generator. Got the main generator loop stubbed and the logic of the system engine designed. Finish the generator tonight.

### D3R1
Updated the challenge README and this log markdown. L-System generator main and rule processors completed. Need to revise the system engine.

### D4R1
Completed the text-based L-System generator. Tested with A -> B; B -> ABA ruleset. Learned about the *global* keyword in python. Onto the next ALife programming project!

### D5R1
Started a simple graphical L-System generator in Python. Studied *turtle* drawing and implemented tkinter in local dev environment. Developed generator function outline.

### D6R1
Continued working on simple graphical L-System generator. Expanded on the graphics system using Turtle. Resolved a few bugs in syntax.

### D7R1
More or less completed the simple graphical L-System generator. Faithfully renders a classic l-system example (included rule as a comment). Started looking at the next project in the challenge.

### D8R1
Long travel day. Worked on code outline for the next challenge project which is a simple boolean cellular automata.

### D9R1
Finished boolean CA seed processor function and number of generations to run function. Fixed tab/space indentation issue. Need to get finish the graphical L-System project tomorrow.

### D10R1 - D12R1
Worked on boolean CA code intermittently during conference. Also worked on L-System turtle engine a little. Read about general artificial life algorithms for more advanced cellular automata theory.

### D13R1
Continued working on boolean CA. Built rough outline for rules engine and refined seed and generation inputs functions. Coding on travel is challenging.

### D14R1 
Worked on boolean CA and simple graphical L-system. Boolean ca just needs rules and L-System needs to compute final string for the turtle to eat.

### D15R1
Decided that manually retweeting on the #100DaysOfCode hashtag was an opportunity for automation. Programmed a python retweet bot that catches the hashtag and randomly selects a response. 

###D16-17R1
Finished python-based retweet-bot that searches for #100DaysOfCode hashtag and 'retweets' with a randomly selected comment. Tested and validated execution. Updated README with basic instructions. Now, back to Artificial Life!

###D18R1
Finished simple graphical L-System using python and turtle drawing. Maybe in the future I'll work on an engine that is char agnostic but for now the A, B, -, + drawing system works fine to illustrate the L-System concept.

###D20R1
Redesigned 1d boolean cellular automata and started programming. The previous implementation grew to be clunky. One step back, two forward. Good lesson in avoiding a sunk cost fallacy. 

###D21R1
Finished core 1d boolean cellular automata programming. Need to thoroughly test the computation of neighborhoods and cell state changes tomorrow.

###D22R1
Started programming a simple text-based game agent using a finite state machine with three states (run, patrol, attack). 

###D23R1
Continued work on simple text-based game agent finite state machine. Also started work on a more simple two state FSM as a primitive example.

###D24R1
Worked on two state FSM and the simple game agent FSM today. Two state is finshed but needs testing. The simple game agent needs a few additinal methods programmed.

###D25R1
Quarter of the way done with the challenge! Finished the two state FSM today. Started design for a two agent FSM to display autonomous behavior using state transitions.

###D26R1
Programmed state transition behavior in simple FSM agent relative to enemy presence and state. Worked on a new development environment.

###D27R1
Added more functionality to the simple FSM agent. Read about optimal state machine transition designs. Slow day.

###D28-29R1
Busy days. Worked on simple FSM state transition functionality and started foundation for a two agent flocking behavior demonstration. Read a bunch about #pygame.

###D30R1
Continued building pygame implementation of simple two agent flocking behavior. Have the sprit animated with boundary detection working.

###D31-32R1
Worked on function in flocking behavior demo to generate random number of agents and place each at a random (non-overlapping) location in the field. Also, starting programming simple distance calculation functions so that agents keep an average spacing once they flock.

###D33-D34R1
Can generate random arrangement of 2d agents in x,y space now. Working on agent-to-agent distance caculation function and mult-agent movement function now.

###D35R1
Slow day after travel. Worked on flocking function a little and read some about ant foraging for next project.

###D36R1
Had to regress a bit of the two agent flocking function to diagnose an animation issue. Started programming outline for complex agent flocking, including mouse input for obstacles.

###D37R1
Got two agents with very basic flocking running. Need to refine border detection and add more granular flocking behavior rules.

###D38R1
Started programming a simple agent brain that tells us how it perceives its own flocking behavior. Nice break so far.

###D39R1
Worked on simple agent brain a bit more. The agents output their 2d cartesian position and facing. Next up: finishing the distance calculations and movement

###D40R1 
Added code to differentiate between lead agent and followers in the simple agent brain program. Needed this so that movement can be relative to a fixed, rational point in the grid.

###D41R1
Wanted a break from Artificial Life. Started https://github.com/jasonmpittman/100-days-of-code as a repo to hold general programming. 

###D42R1
Finished essential programming for a visualization of the Pareto principle using simulated exchange of abstract currency. Neat little exercise to practice randomization and historgrams. 

###D43-44R1
Finished histogram creation for Pareto simulation. Worked on a small bug in value distribution in the player class. Read about matplotlib plot functions.

###D45R1
Resolved bug in player class value distribution in the Pareto simulation. Wondering if I should go back to ALife or keep up general programming.

###D46R1
Programmed a two group effect size calculator. The calculator works but has a arithmetic bug in the effect_size function. Small scope projects like this are a great break from larger efforts.

###D47R1
Fixed the arithmetic bug in the two group effect size calculator. Final build is in https://github.com/jasonmpittman/100-days-of-code

###D48R1
Programmed an independent t test calculator. Computes t-ratio and degrees of freedom so you can look up p against alpha. Final build in https://github.com/jasonmpittman/100-days-of-code

###D49R1
Programmed a paired t test calculator as a follow up to D48. Final build available in https://github.com/jasonmpittman/100-days-of-code. Traveling this week so may not update again for a few days.

###D50R1 
From a hotel in AZ...programmed a standard (z) score calculator. These small projects are just plain fun. Final build available in https://github.com/jasonmpittman/100-days-of-code.

###D51R1-D53R1
Two days on the road without internet; coded but not committed until now. Worked on a list of calculators to develop and maybe turn into a robust simulation for teaching stats. Worked on an ANOVA calculator but not finsihed. 

###D54R1
Completed the ANOVA calculator. Worked a bit on larger statistical ed plan. May put that aside for a bit and get back to ALife stuff.

###D55R1
Chill day reading some ALife research and working on plan for the statistics ed program.

###D56R1-D57R1
Worked on a wilcoxon signed rank test calculator. I'm addicted to programming these simple calculators now. 

###D58R1
Worked some more on the wilcoxon signed rank test. Starting thinking about procedural generation and mazes for some reason.
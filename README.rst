=========
solve_led
=========

This package will test the status of lights in a 2-dimensional light grid, which
is represented as a list of lists. 

This package will take a text file of a specific input containing 
the size of the grid and commands to turn on, turn off or switch
the lights. It will then count the amount of light that are on after 
executing the commands. 


Description
===========

Usage: In the command line, you may use the command: solve_led --input followed 
by the path to a text file or a URL with a text file in the required format.
This package will execute the commands and print the number of lights on after execution.

#from assignment specification
The input file has the following format:
999
turn on 0,0 through 999,999
switch 0,0 through 999,0
turn off 499,499 through 500,500
...
where the first line specifies the size of the grid (the length of each row/column) 
and the next lines contain the commands. 



Note
====

This project has been set up using PyScaffold 3.0.1. For details and usage
information on PyScaffold see http://pyscaffold.org/.

# Random-Table-Roller
A program to auto-generate results for arbitrary random tables

## How to use the RTR
Simply import a randomizer and hit the button to generate random results from it.
The RTR will generate one result for every table in the randomizer while ignoring subtables. Subtables will only be rolled on when used by a result.

## What is a randomizer?
A randomizer is a collection of random tables. It can consist of any number of tables which may have any number of entries, subtables or links to 
other tables.
Randomizers need to follow certain rules to be correctly recognized by the RTR.

## How to construct a randomizer
Randomizers can be any file type, although .txt files are recommended.

* Any text up to the first blank line will be recognized as the name of the randomizer
* The name must be separated by at least one blank line. Similarly, every table must be separated by at least one blank line.
* The randomizer must contain at least one table and can contain any number of tables
* The randomizer must not contain anything but its name and tables

### How to construct tables for the randomizer
Just ike the randomizer, so must its tables adhere to a certain set of rules.
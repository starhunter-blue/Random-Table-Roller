# Random-Table-Roller
A program to auto-generate results for arbitrary random tables

## How to use the RTR
Simply import a randomizer and hit the button to generate random results from it.
The RTR will produce results as follows:
* One result for every Table as marked by <> will be generated.
* No results for Subtables as marked by <> will be generated.
* If result contains a subtable ro reference to another table as marked by -->, one result will be generated from that table.
** Additional subresults will be generated until no more are required.
The save button will you to save your generated results to a file.


## What is a randomizer?
A randomizer is a collection of random tables. It can consist of any number of tables which may have any number of entries, subtables or links to 
other tables.
Randomizers need to follow certain rules to be correctly recognized by the RTR.

## How to construct a randomizer
Randomizers can be any file type, although .txt files are recommended.
For an additional guide, see the example randomizer provided.

* Any text up to the first blank line will be recognized as the name of the randomizer.
* The name must be separated by at least one blank line. Similarly, every table must be separated by at least one blank line.
* The randomizer must contain at least one table and can contain any number of tables.
* The randomizer must not contain anything but its name and tables.

### How to construct tables for the randomizer
Just ike the randomizer, so must its tables adhere to a certain set of rules.

* Every table must start with its name, followed by one or more entries.
* Every table is either a table or a subtable, as marked by the name being enclosed by <>/<<>>.
** <TABLE NAME> denotes a regular table. This means the RTR will generate a result from it.
** <<TABLE NAME>> denotes a subtable. The RTR will only roll on it if required by the result of another roll.
*** Example: <Example Table> OR <<Example Subtable>>
* There must be no blank lines within the table
* An entry must always start with a single number or a range of numbers on which the result is produced, followed by a :, followed by the entry's value
*** Example: 1: Example Result OR 1-3: Example Result
* Every entry must be on a new line
* Numbers must be used continuously, no skipping
* Numbers must not be duplicated
* Entries can have a simple result, or a complex result as denoted by -->. Complex results can either be a subtable written after the -->, or a link to another table
** In-Line subtables must be enclosed by []. Instead of being written vertically, they are separated by ,. They must not have a name. Other than that, the same rules apply as for any other table.
*** Example: 1: Result --> [1: Subresult 1, 2: Subresult 2, 3-6: Subresult 3 --> [1: Subsubresult 1, 2: Subsubresult 2]]
** Links to other tables simply refer to the other table by name.
*** Example: 1: Result --> Table 1 OR 2: Result --> Subtable 2
** Complex entries can be nested as deeply as required
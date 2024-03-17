# Selection

## Learning Objectives/Goals
Be able to read, comprehend, trace, adapt and create Python code using selection that:

- Uses Boolean conditions
- Uses simple selection code
- Uses selection using IF for one situation.
- Uses selection using IF and ELSE for two situations

## TEACHER NOTES
### What is Selection?

This week is focused on **selection, **the code that makes the computer perform different tasks in different situations.  Selection is sometimes referred to as a decision, and this often helps when we are explaining the idea to students.  Whenever we make an IF _this_ THEN _that_ type decision we are using selection logic.  There are a lot of concepts to unpack in even a simple selection statement.  I’ve tried to break it down and build up slowly and often find that it takes my students lots of time & practice to truly master them.

For example, real life decisions could be:

_IF it is raining THEN _

_Take your umbrella._

Or:

_IF you haven’t done your homework THEN _

_You get grounded._

In both of these examples, the instruction on the second line is only followed if the scenario on the first line is _true. _Otherwise it is skipped over.  This is an essential part of selection explained in more depth below.


### Boolean Conditions

Whereas in all of the code we have written before the computer runs each line one at a time, selection relies on a **Boolean Condition **to decide whether or not to run the code.

Boolean conditions are true or false checks.  If a condition is checked and comes back as **true**, the code on the line(s) below runs.  If it comes back as **false**, then the computer skips the commands and moves on with the rest of the program.

Let’s put that into practice with the umbrella example above:

IF **it is raining **THEN 

Take your umbrella

The condition is in red.  It is either raining (True) or not (False).  If it is raining (true) then the instruction to take your umbrella is carried out.  If not (false) then we would skip down to the next instruction that wasn’t part of the selection (probably something like ‘leave the house’).


### Boolean Operators

Boolean conditions are written using logical operators.  These are:

==   Equal to/Same as (a single = is used to store data in a variable, so Python uses double = to compare two pieces of data)

!= Not equal to

The above two conditions can be used with integers or strings.  The ones below can only be used with numeric data (integers or floats/decimals)

> Greater than

>= Greater than or equal to

&lt; Less than

&lt;= Less than or equal to

Let’s use the umbrella example again.  We want to compare the weather to rain to see if they are the same, so we would write our condition like this:

IF weather == “rain” THEN

	Take your umbrella

**Case matters **when comparing text using ==.  The match has to be **exact**.  For the example above, if the user inputs ‘rain’ then the condition will be true.  If they input ‘Rain’ then it will be false.  Future units will look at how to get around this issue.

The examples above only refer to selection for one situation.  See the lesson slides and individual task notes for how to develop this for two or more situations.

## CODE examples

### Selection With One Outcome

These selection examples either output a statement (if the condition is true) or they appear to do nothing (if the condition is false). In reality the computer is just skipping the indented line(s) below the ‘if’.  Because there is no more code after this, the computer has no more instructions to execute so completes the program.  Students should only get an output if their condition is true.

To summarise, this code should be written like this:

```
if condition:
  code to run if condition is true
```

### Selection With Two Outcomes

These selection examples output one of two different statements.  The indented code below the ‘if’ runs when the condition is true.  The ‘else’ is used as a catch all - if the condition is false then the computer skips down to the else and runs the indented code there instead.  **Please note - **the else does not have a condition.  It doesn’t need one because it runs every time the condition after the ‘if’ is false.

To summarise, this code should be written like this:

```
if condition:
  code to run if condition is true
else:
  code to run if condition is false.
```

## PRIMM Task - Modify

In the **modify** tasks, students adapt the example code to start to create code of their own.

Make sure that the students add comments to explain what the code does.

## Errors And Misconceptions To Watch Out For

- a colon at the end of each if and else line.
- each branch is indented unsing the TAB key (not just spaces)
- no condition after 'else'
- a **double** equals in the condition when checking that two pieces of data are the same.

# Exercise 3 - `for` loops and conditional statements

The exercise for this week is meant to help you to understand `for` loops and conditional statements in Python.
Below you have a series of problems in which you are asked to create new script files and write the code necessary to produce the desired results.
After making your changes, you will need to upload these files to GitHub.
The answers to the questions in this week's exercise should be given by modifying the end of this document in the [section titled Answers](#answers).

## Problem 1 - Batch processing data files with a `for` loop (**4 Points**)

This problem is meant to simulate a common problem dealing with data files: batch processing.
Batch processing involves using scripts to process many data files, and one common task is generating a list of filenames that will be processed.
For this problem you will need to create a new script file `station_name_generator.py` that does the following:

1. Create a new variable `basename` that contains the text `"Station"`.
2. Create a new variable `filenames` that is an empty list.
3. Iterate over the number range 0-20 and
  1. Create a variable `station` that contains the text from `basename` variable and
  2. Add the content of `station` to `filenames` list which should have following content in the end:

      ```
      ['Station_0.txt', 'Station_1.txt', 'Station_2.txt', 'Station_3.txt',
       'Station_4.txt', 'Station_5.txt', 'Station_6.txt', 'Station_7.txt',
       'Station_8.txt', 'Station_9.txt', 'Station_10.txt', 'Station_11.txt',
       'Station_12.txt', 'Station_13.txt', 'Station_14.txt', 'Station_15.txt',
       'Station_16.txt', 'Station_17.txt', 'Station_18.txt', 'Station_19.txt',
       'Station_20.txt']
      ```


**Your score on this problem will be based on following criteria:**

 - Create and use variables to produce the desired text format
 - Successfully use for loop to iterate over desired set of numbers
 - Successfully produce the desired filename
 - Having your script printing all filenames as shown above
 - Including comments that explain what most lines in the code do
 - Uploading your script to your GitHub repository for this week's lesson with the name `station_name_generator.py`.

## Problem 2 - Classifying temperatures

This problem is meant to introduce you to a very commonly used and useful concept of data classification.
In this problem your aim is to classify daily temperatures stored in `temperatures` list into four different classes:

  1. **Cold** ==> temperatures below -2 degrees (Celsius)
  2. **Slippery** ==> temperatures between -2 and +2 degrees (Celsius)
  3. **Comfortable** ==> temperatures between +2 and +15 degrees (Celsius)
  4. **Warm** ==> temperatures above +15 degrees (Celsius)

Fill in the missing parts in the starter code [classify_temperatures.py](classify_temperatures.py).

**Your score on this problem will be based on following criteria:**

 - Create and use variables to produce the desired text format
 - Successfully use for loop to iterate over desired set of numbers
 - Successfully produce the desired filename
 - Having your script printing all filenames as shown above
 - Including comments that explain what most lines in the code do
 - Uploading your script to your GitHub repository for this week's lesson with the name `station_name_generator.py`.

## Problem 3 - Classifying locations

This problem continues our classification theme from the geographical perspective.

Following map shows the locations of the weather stations (blue points) in Finland that are older than 50 years.
In this problem we are interested to classify those stations

![](img/FMI_stations_50_years_older.png)




## Extra Problem - Nested `for` loops
In addition to having single `for` loops that iterate across some variable range, it is possible to *nest* `for` loops within one another.
Consider the example below:

```python
>>> for char in 'dog':
...     for char2 in 'cat':
...         print (char, char2)
    d c
    d a
    d t
    o c
    o a
    o t
    g c
    g a
    g t
```

Here, you can see that in the first pass through the first `for` loop, the value of `char` is `d`.
Entering the inner (or nested) loop, `char2` is set to `c`.
After this, the output is written to the screen and since there are more letters to loop over in the inner `for` loop, the value of `char2` will be updated upon the next pass.
The second time through the inner loop, `char2` is set to `a` while `char` remains `d`.
Like this, the inner loop will run through all of the letters in `cat` for each time that `char` is updated in the outer loop.
It doesn't take too much imagination to figure out this is a very useful concept.

For this problem you should create a new Python script `make_flag.py` that does the following:

1. Creates a variable `star` with text `"*"` and an empty string variable `text`. Recall, you can created empty string variables by assigning `""` as their value.
2. Uses nested `for` loops and the variables above to produce the text formation below when `print(text)` is run at the end of your script.

    ```
    *******
    *******
    *******
    ```
3. Creates a variable `line` with text `"-"` and an empty string variable `flag`.
4. Uses nested `for` loops and the variables above to produce the text formation below when `print(flag)` is run at the end of your script. **Note**: You will need to use conditional statements to produce the desired output.

    ```
    *******------------
    *******------------
    *******------------
    -------------------
    -------------------
    ```

### Questions for Extra Problem
1. If faced with having to reproduce the character patterns in this exercise with a Python script any way you can, how might you approach this problem differently? For example, let's say you did not need to use the variables `star = "*"` and `line = "-"`.
2. Using nested loops is very common for Python scripts that deal with two-dimensional data such as latitude and longitude, or depth versus distance. Can you think of any cases in which you might use a nested loop in a Python script?

## Problem 3 - Working with projections using conditional statements

In Python there is a handy way of asking input from the user using `input` function such as:

   ```python
   >>> name = input('Please tell me your name:\n')
   Please tell me your name:
   Henrikki
   >>> print("Hello", name)
   Hello Henrikki
   ```

Your job in this problem is to create a new Python script `epsg_finder.py` that:

1. Asks the user for an input value by displaying the text "What is the EPSG value of the input shapefile?"
  - If the user says `4326`, the program prints "EPSG value 4326 corresponds to WGS84" to the screen
  - If the user says `3067`, the program prints “EPSG value 3067 corresponds to ETRS-TM35FIN" to the screen
  - If the user says `2392`, the program prints “EPSG value 2392 corresponds to KKJ / Finland zone2" to the screen
  - If the user enters any other value, the program should print "There are so many spatial references..I don’t know them all, sorry." to the screen

### Questions for Problem 3
1. Did you use any `elif` statements in your Python code? If so, can you think of any way in which you could rewrite you code without using `elif` statements? If not, can you think of any way in which you could rewrite your code to include them?
2. Why did you choose to include or not include `elif` statements in your code? Did it make more sense to use to use them, or was it easier to write your code without?

## General tips
1. Create a general template for your new script files and commit it to GitHub right when you start working on your script(s).
2. Your scripts should also follow the format described earlier in the course with a block comment at the start of the file, inline comments describing how it works and good use of blank lines to make the code easy to read.
3. Look carefully at the requirements for each exercise and be sure to follow them.
4. In case you have forgotten, string variables can be added together. For example,

    ```python
    >>> a = "Taco "
    >>> b = "time"
    >>> c = a + b
    >>> print(c)
    Taco time
    ```
5. The questions after the exercises do not necessarily have correct or incorrect answers, but they are meant to make you think a bit about how you have written your scripts and how they might be applied to your own data/research/studies.

# Answers

## Problem 1

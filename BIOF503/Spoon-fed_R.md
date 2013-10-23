Spoon-Fed R
========================================================
author: Matt Shirley
date: October 24 2013

Overview
========

1. interacting with R
2. using R as a calculator
2. variables
3. data structures
3. summarizing data
3. loops, flow-control
4. apply
5. basic stats in R
6. reading and writing delimited data
8. plotting with base R graphics
2. loading and installing packages
9. plotting with ggplot2

interacting with R
==================
- command-line interpreter
- GUI interpreter: RStudio

command-line interpreter
========================
- everyone has one
- just type `R` at your command-line shell:

```
R version 3.0.2 -- "Frisbee Sailing"
Platform: x86_64-apple-darwin13.0.0 (64-bit)
...

Type 'q()' to quit R.

> 
```
- The carat (`>`) is your prompt for entering commands
- I will omit the carat for the rest of the presentation

GUI interpreter: RStudio
========================
- Download from [http://www.rstudio.com/](http://www.rstudio.com/)
![](http://www.rstudio.com/images/screenshots/rstudio-mac.png)

GUI interpreter: RStudio
========================
RStudio is an integrated development environment including:
- interpreter with code completion
- text editor with syntax highlighting and completion
- file browser
- version control manager
- visual object workspace
- command history

the R interpreter
=================

```r
# This is a comment, which is ignored
```


```r
# functions are applied with ()
print("hello") 
```

```
[1] "hello"
```

- anything in quotes is a "string"
- anything else is either a number or:
  - function
  - class
  - operator (`+-/?%&=<>|!^*`)

using R as a calculator
=======================
Addition

```r
2 + 2
```

```
[1] 4
```

Subtraction

```r
5 - 2
```

```
[1] 3
```


using R as a calculator
=======================
Division

```r
2 * 2
```

```
[1] 4
```

Multiplication

```r
5 / 2
```

```
[1] 2.5
```


using R as a calculator
=======================
Exponents

```r
2^4
```

```
[1] 16
```

Logorithms

```r
log10(100)
```

```
[1] 2
```

```r
log2(4)
```

```
[1] 2
```


using R as a calculator
=======================
Order of operations

```r
10 / 2 - 1
```

```
[1] 4
```

```r
10 - 5 / 5
```

```
[1] 9
```

```r
(10 - 5) / 5
```

```
[1] 1
```

Be careful. Evaluation of operators occurs left to right.

variables
=========

```r
x <- 1
x
```

```
[1] 1
```

Variables can be assigned (`<-`) a value

variables
=========

```r
x <- 1
y <- 2
x <- y
x
```

```
[1] 2
```

```r
y
```

```
[1] 2
```

But be **careful** because they can be re-assigned

data structures: comparisons
===================

```r
x <- 0
```


```r
x > 1 ## x is greater than 1
```

```
[1] FALSE
```

```r
x < 1 ## x is greater than 1
```

```
[1] TRUE
```


data structures: comparisons
===================

```r
x == 1
```

```
[1] FALSE
```

```r
x == 0
```

```
[1] TRUE
```

```r
x != 0
```

```
[1] FALSE
```

Comparisons result in *boolean* values

data structures: vectors
===============

```r
x <- 3
y <- c(1,2,x)
y
```

```
[1] 1 2 3
```

Vectors can hold elements of the *same type*.

data structures: vectors
===============

```r
names(y) <- c("one", "two", "three")
y
```

```
  one   two three 
    1     2     3 
```

Vectors can also have *names* for each element.

data structures: vectors
===============

```r
z <- y * 3
z
```

```
  one   two three 
    3     6     9 
```

```r
sum(z)
```

```
[1] 18
```

Arithmetic can be performed on a vector, which applies that operation to every element and returns a *new vector*.

data structures: vector indexing
===============

```
  one   two three 
    3     6     9 
```


```r
z[1]
```

```
one 
  3 
```

```r
z["one"]
```

```
one 
  3 
```

Vectors can be indexed using a *1-based* position, as well as *name*.

data structures: vector slicing
===============

```r
z
```

```
  one   two three 
    3     6     9 
```

```r
z[2:3]
```

```
  two three 
    6     9 
```

*Slicing* a vector is as easy as specifying `start:end`.

data structures: vector slicing
===============

```r
z[-1]
```

```
  two three 
    6     9 
```

```r
z[-2:-3]
```

```
one 
  3 
```

Remove elements from a vector using negative indices.

data structures: lists
===============

```r
q <- list(y, z)
q
```

```
[[1]]
  one   two three 
    1     2     3 

[[2]]
  one   two three 
    3     6     9 
```

Lists can contain vectors.

data structures: list indexing
===============

```r
q[[1]]
```

```
  one   two three 
    1     2     3 
```

```r
q[[1]][1]
```

```
one 
  1 
```

You can index a list in the same way as a vector.

data structures: sequences
===============

```r
v <- seq(1,9) ## or 1:9
v
```

```
[1] 1 2 3 4 5 6 7 8 9
```

Let's construct a sequence of 9 numbers.

data structures: sequences
===============

```r
c(v,v)
```

```
 [1] 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
```

```r
rep(v, times=3)
```

```
 [1] 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
```

We can *concatonate* or *repeat* a vector as well.

data structures: matrices
===============

```r
mt <- matrix(v, nrow=3)
mt
```

```
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
```

```r
matrix(v, nrow=3, byrow=T)
```

```
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
[3,]    7    8    9
```

Matrices, created from vectors, are row or column oriented.

data structures: matrix indexing
===============

```
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
```


```r
mt[1,1]
```

```
[1] 1
```

```r
mt[3,3]
```

```
[1] 9
```

Matrices are indexed as `[row,col]`

data structures: dimension
===============

```r
dim(mt)
```

```
[1] 3 3
```

```r
nrow(mt)
```

```
[1] 3
```

```r
ncol(mt)
```

```
[1] 3
```

Dimensionality, number of rows and columns can computed using these functions.

data structures: dataframes
===============

```r
df <- data.frame(y, z)
colnames(df) <- c("first","second")
df
```

```
      first second
one       1      3
two       2      6
three     3      9
```

Dataframes are like matrices, but contain more structure.

data structures: dataframe indexing
===============

```
      first second
one       1      3
two       2      6
three     3      9
```


```r
df$first
```

```
[1] 1 2 3
```

Dataframes can be indexed by name to return a vector.

data structures: dataframe indexing
===============

```
      first second
one       1      3
two       2      6
three     3      9
```


```r
df["first"]
```

```
      first
one       1
two       2
three     3
```

Dataframes can be indexed by name to return another dataframe

data structures: dataframe indexing
===============

```
      first second
one       1      3
two       2      6
three     3      9
```


```r
df$first[1]
```

```
[1] 1
```

Dataframes can be further indexed to return individual elements

data structures: logical indexing
===============

```
      first second
one       1      3
two       2      6
three     3      9
```


```r
df > 3
```

```
      first second
one   FALSE  FALSE
two   FALSE   TRUE
three FALSE   TRUE
```

Dataframes, just like other structures, can be compared, resulting a *boolean* values.

data structures: logical indexing
===============

```
      first second
one   FALSE  FALSE
two   FALSE   TRUE
three FALSE   TRUE
```


```r
df[df > 3]
```

```
[1] 6 9
```

Passing the boolean result of comparison as an index returns only elements where the comparison was `TRUE`.

data structures: logical indexing
===============

```
      first second
one   FALSE  FALSE
two   FALSE   TRUE
three FALSE   TRUE
```


```r
which(df > 3)
```

```
[1] 5 6
```

The `which` function converts a boolean index to a numeric index.

data structures: dataframe binding
===============

```
      first second
one       1      3
two       2      6
three     3      9
```


```r
cbind(df, data.frame("third"=c(9,18,27)))
```

```
      first second third
one       1      3     9
two       2      6    18
three     3      9    27
```

Dataframe columns can be bound to form a new dataframe.

data structures: dataframe binding
===============

```
      first second
one       1      3
two       2      6
three     3      9
```


```r
rbind(df, data.frame("first"=4, "second"=12, row.names="four"))
```

```
      first second
one       1      3
two       2      6
three     3      9
four      4     12
```

Dataframe rows can be bound to form a new dataframe.

summarizing data
================

```r
library(datasets)
dim(cars)
```

```
[1] 50  2
```

```r
head(cars)
```

```
  speed dist
1     4    2
2     4   10
3     7    4
4     7   22
5     8   16
6     9   10
```


summarizing data
================

```r
mean(cars$speed)
```

```
[1] 15.4
```

```r
median(cars$speed)
```

```
[1] 15
```

```r
sd(cars$speed)
```

```
[1] 5.288
```

Mean, median and standard deviation.

summarizing data
================

```r
summary(cars)
```

```
     speed           dist    
 Min.   : 4.0   Min.   :  2  
 1st Qu.:12.0   1st Qu.: 26  
 Median :15.0   Median : 36  
 Mean   :15.4   Mean   : 43  
 3rd Qu.:19.0   3rd Qu.: 56  
 Max.   :25.0   Max.   :120  
```

Summarizing a dataframe returns percentiles and mean.

loops, flow-control: for loops
===================

```r
for (x in 1:10){ 
  print(x) 
  }
```

```
[1] 1
[1] 2
[1] 3
[1] 4
[1] 5
[1] 6
[1] 7
[1] 8
[1] 9
[1] 10
```

Use *for loops* to repeat a task a certain number of times.

loops, flow-control: if/else
===================

```r
x <- 0
if (x == 0) { print("yes") }
```

```
[1] "yes"
```

```r
if (x > 1) { print("yes") } else { print("no") }
```

```
[1] "no"
```

- If statements only execute code if the condition evaluates to `TRUE`. 
- Else statements execute when the condition is not satisfied.

loops, flow-control: while loops
===================

```r
x <- 0
while (x < 5){ 
  print(x) 
  x <- x + 1
  }
```

```
[1] 0
[1] 1
[1] 2
[1] 3
[1] 4
```

Use *while loops* to repeat a task *while* a condition (`x<5`) is true.

apply: functional application
=====

```
      first second
one       1      3
two       2      6
three     3      9
```


```r
apply(df, 1, sum)
```

```
  one   two three 
    4     8    12 
```

```r
apply(df, 2, sum)
```

```
 first second 
     6     18 
```

*Apply* a function over array columns (1) or rows (2).

sapply: simpler apply
======

```
      first second
one       1      3
two       2      6
three     3      9
```


```r
sapply(df, sqrt)
```

```
     first second
[1,] 1.000  1.732
[2,] 1.414  2.449
[3,] 1.732  3.000
```

*Simple apply* a function to every element, returning the same type of data structure.

reading and writing delimited data
==================================

```r
write.table(df, file = "example.txt")
write.table(df, file = "example.tsv", sep = "\t")
write.csv(df, file = "example.csv")
```

Write 1) space-delimited, 2) tab-delimited, 3) comma-delimited files containing dataframe `df`.

reading and writing delimited data
==================================

```r
df1 = read.table("example.txt", header=T)
df2 = read.delim("example.tsv", sep = "\t")
df3 = read.csv("example.csv", row.names = 1)
```


```r
identical(df1,df2)
```

```
[1] TRUE
```

```r
identical(df2,df3)
```

```
[1] TRUE
```

All three files result in equivalent dataframes.

reading and writing delimited data
==================================
Issues to consider when reading and writing delimited files:

1. Do I want/have column names (header)?
2. Do I want/have row names?
3. What is my delimiter?
4. Do I want/have quotes surrounding each value?

Check the **default behavior** of the reading/writing function first.

plotting with base R graphics
=============================

```r
head(cars)
```

```
  speed dist
1     4    2
2     4   10
3     7    4
4     7   22
5     8   16
6     9   10
```


plotting with base R graphics: scatterplot
=============================

```r
plot(cars)
```

![plot of chunk unnamed-chunk-61](Spoon-fed_R-figure/unnamed-chunk-61.png) 

***
- `plot` accepts a dataframe with two columns
- column 1 = x axis
- column 2 = y axis

plotting with base R graphics: line plot
=============================

```r
plot(cars, type="l")
```

![plot of chunk unnamed-chunk-62](Spoon-fed_R-figure/unnamed-chunk-62.png) 

***
- valid plot types:
  - "p" for points
  - "l" for lines
  - "b" for both ("o" for overplotted)
  - "h" for ‘histogram’-like lines
  - "s" for stair steps ("S" for other)
  - "n" for no plotting.

plotting with base R graphics: linear regression
=============================

```r
lmcars <- lm(dist ~ speed, cars)
lmcars
```

```

Call:
lm(formula = dist ~ speed, data = cars)

Coefficients:
(Intercept)        speed  
     -17.58         3.93  
```

- `lm` fits a linear model: `response ~ terms`
- in this case the response is distance traveled at speed

plotting with base R graphics: linear regression
=============================

```r
plot(cars)
abline(lmcars)
```

![plot of chunk unnamed-chunk-64](Spoon-fed_R-figure/unnamed-chunk-64.png) 

***
- `abline` draws a line from slope and intercept

plotting with base R graphics: graphics parameters
=============================

```r
plot(cars, title="Speed vs. Distance", xlab="Speed", ylab="Distance", ylim=c(0,100))
abline(lmcars)
```

![plot of chunk unnamed-chunk-65](Spoon-fed_R-figure/unnamed-chunk-65.png) 


plotting with base R graphics: graphics parameters
=============================

```r
plot(cars, col="red", pch=16, cex=2)
abline(lmcars, col="blue")
```

![plot of chunk unnamed-chunk-66](Spoon-fed_R-figure/unnamed-chunk-66.png) 


plotting with base R graphics: histograms
=============================

```r
hist(cars$speed)
```

![plot of chunk unnamed-chunk-67](Spoon-fed_R-figure/unnamed-chunk-67.png) 


plotting with base R graphics: boxplots
=============================

```r
boxplot(cars)
```

![plot of chunk unnamed-chunk-68](Spoon-fed_R-figure/unnamed-chunk-68.png) 

***
- Outliers are defined as outside 1.5*IQR
- IQR = interquartile range

plotting with base R graphics: PCA
=============================

```r
pcars <- prcomp(cars)
biplot(pcars)
```

![plot of chunk unnamed-chunk-69](Spoon-fed_R-figure/unnamed-chunk-69.png) 

***
- principal components analysis of variance
- biplot of the first (and therefore largest) components
- vector arrows represent magnitude of contribution of each variable

loading and installing packages
===============================

```r
library('stats')
```

- `library()` loads an R *package* into your current session
- This will import all *functions* from that package for your use
- If you don't have the package installed, R will complain:

```r
library('foo')
```

```
Error in library("foo") : there is no package called 'foo'
```
So we must install the package...

loading and installing packages
===============================
Install from CRAN (Comprehensive R Archive Network) repositories

```r
install.packages('ggplot2')
```

Install from [Bioconductor](http://www.bioconductor.org/)

```r
source("http://bioconductor.org/biocLite.R")
biocLite('GRanges')
```

Install from GitHub

```r
install.packages('devtools')
library(devtools)
install_github('ballgown')
```


plotting with ggplot2
=====================
- ggplot = *grammar* of *graphics*
- combines statistical and graphical models
- can create very concise, detailed plots using few keystrokes

```r
library("ggplot2")
```


plotting with ggplot2
=====================

```r
head(mtcars[c("wt","mpg","cyl","disp")])
```

```
                     wt  mpg cyl disp
Mazda RX4         2.620 21.0   6  160
Mazda RX4 Wag     2.875 21.0   6  160
Datsun 710        2.320 22.8   4  108
Hornet 4 Drive    3.215 21.4   6  258
Hornet Sportabout 3.440 18.7   8  360
Valiant           3.460 18.1   6  225
```

```r
p <- ggplot(mtcars, aes(wt, mpg))
```

- building a plot starts with a dataframe
- aestetics (aes) are columns of the dataframe
- usually corresponts to x & y axis

plotting with ggplot2: add a geometry
=====================

```r
p + geom_point()
```

![plot of chunk unnamed-chunk-77](Spoon-fed_R-figure/unnamed-chunk-77.png) 

***
- now we add a geometry
- calling the plot produces the graphics

plotting with ggplot2: geometry aes
=====================

```r
p + geom_point(aes(colour = factor(cyl)))
```

![plot of chunk unnamed-chunk-78](Spoon-fed_R-figure/unnamed-chunk-78.png) 

***
- we can add aestetics to the geometry
- in this case, color the points by number of cylinders

plotting with ggplot2: geometry aes
=====================

```r
p + geom_point(aes(shape = factor(cyl)), size=6, alpha=I(0.5))
```

![plot of chunk unnamed-chunk-79](Spoon-fed_R-figure/unnamed-chunk-79.png) 


plotting with ggplot2: boxplots
=====================

```r
p <- ggplot(mtcars, aes(factor(cyl), mpg))
p + geom_boxplot()
```

![plot of chunk unnamed-chunk-80](Spoon-fed_R-figure/unnamed-chunk-80.png) 


plotting with ggplot2: barplots
=====================

```r
ggplot(diamonds, aes(clarity, fill=cut)) + geom_bar()
```

![plot of chunk unnamed-chunk-81](Spoon-fed_R-figure/unnamed-chunk-81.png) 


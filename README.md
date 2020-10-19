# Algorithms For the People Final Project: Atlas of Surveillance

The Atlas of Surveillance (AoS) is an EFF database of the surveillance technology owned and operated by
local law enforcement agencies. The DB can be downloaded as a csv (it’s about 3MB). In this project you
will use the data in AoS to investigate how surveillance equipment is distributed across the US as a function
of the racial and ethnic composition of a county, the median household income of a county, and any other
characteristics you find interesting. To do this you will need other sources of data like the Census.

We are going to use the US Census demographic data in order to make conclusions regarding demographics, gender, and surveillance technologies.

## Schedule
- ~~Oct 12: methods & proposal~~
- Oct 19: have database cleaned and loaded into python (pandas), develop research question/hypothesis and determine which tests will be used
- Oct 26: statistical methods run
- Nov 2: analyze results
- Nov 9: works on data visualization/website (time permitting)
- Nov 16: Have presentation prepared and rehearsed
- Nov 19: Present! :) 

## Data

**us-census-demographic-data**: https://www.kaggle.com/muonneutrino/us-census-demographic-data This dataset includes demographic data from throughout the US from 2015-2017.  This works well with the Atlas of Surveillance dataset because it includes data from before 2015 as recent as 2020.  It contains gender and race for different counties and states.  It is saved as a csv file in the us-census-data directory.

**atlas-of-surveillance**: csv file: https://atlasofsurveillance.org/

## Hypotheses
### Hypothes Test 1 Chi-square test for independence

#### Null Hypothesis:
The type of surveillance technology used does not depend on demographic group (there is no relationship).
(p-value greater than significance level)

#### Alternative Hypothesis:
The type of surveillance technology used does depend on demographic group.
(p-value less than significance level)

### Hypothesis Test 2
#### Null Hypothesis: 
There is no greater number of cameras directed towards members of the Black community.
#### Alternative Hypothesis: 
Based on previous data, members of the Black community have a greater number of cameras directed towards them. 
    
- Try the above hypotheses for different demographics.
#### Significance level: 0.05

### Hypothesis Test 3
- We should run OLS perhaps in multiple states and counties to see if there is a relationship between different demographic groups (being the independent variable) and number of surveillance cameras being the dependent variable.

## Methods
- hypothesis test: using python & pandas
- Machine learning model doesn't look that bad: https://www.geeksforgeeks.org/learning-model-building-scikit-learn-python-machine-learning-library/ knn

## TODO
- [x] clean Atlas csv dataset (turn into .db file), clean census data (all)
- [x] load data into python files (Jupyter notebook setup) (all)
- [x] investigate census data
- [ ] investigate what methods we want to use for analysis
- [x] write more detailed proposal

## Presentation
http://brown.edu/go/atlas-presentation

## Website information (reach goal)
- Have a website that we develop to show how many cameras would be on someone based on their demographic data (backend pulls from hypothesis test)
- something like this as inspiration: https://cs.brown.edu/courses/csci1951-a/projects/project_poster/Cam%20Spotter/poster.pdf

## Environment & Dependencies
* sqlite database 
* Jupyter notebook for analysis
   * Intall Jupyter here: https://jupyter.org/install
   * Tutorial: https://www.dataquest.io/blog/jupyter-notebook-tutorial/
* GitHub commands
    * After making change that you made on your local computer and want everyone else to see
        * git add -A
        * git commit -m “description of what changes you made”
        * git push

    * If someone else makes changes that you want on your local computer
        * git pull
    * If someone else makes a change that you need, but you have local changes
        * git stash
        * git pull
        * git stash pop
    * More detailed tutorial: https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6

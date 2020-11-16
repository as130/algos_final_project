# Algorithms For the People Final Project: Atlas of Surveillance

The Atlas of Surveillance (AoS) is an EFF database of the surveillance technology owned and operated by
local law enforcement agencies. The DB can be downloaded as a csv (it’s about 3MB). In this project you
will use the data in AoS to investigate how surveillance equipment is distributed across the US as a function
of the racial and ethnic composition of a county, the median household income of a county, and any other
characteristics you find interesting. To do this you will need other sources of data like the Census.

We are going to use the US Census demographic data in order to make conclusions regarding demographics, gender, and surveillance technologies.

## Link to CLI (please only use from this link):
https://github.com/as130/algos_final_project_cli

## Report:
https://www.overleaf.com/3262343194kdkyqcnrncwy

## Presentation
http://brown.edu/go/atlas-presentation

## Open Questions
- How do we make sure that we are talking about these numbers/findings in an ethical and respecftul way in our final report/presentation?

## Data
**us-census-demographic-data**: https://www.kaggle.com/muonneutrino/us-census-demographic-data This dataset includes demographic data from throughout the US from 2015-2017.  This works well with the Atlas of Surveillance dataset because it includes data from before 2015 as recent as 2020.  It contains gender and race for different counties and states.  It is saved as a csv file in the us-census-data directory.

**atlas-of-surveillance**: csv file: https://atlasofsurveillance.org/

## Methods for Analysis
- OLS Regression Tests 
- K-Nearest Neighbors Machine Learning Algorithm: https://www.geeksforgeeks.org/learning-model-building-scikit-learn-python-machine-learning-library/ 

## CLI (reach goal)
- Have a python script that runs in the command line that allows people to clone our repo and run our k-nearest neighbors algorithm with their own information and play around with it with different county information. 

## Schedule
- ~~Oct 12: methods & proposal~~
- ~~Oct 19: have database cleaned and loaded into python (pandas), develop research question/hypothesis and determine which tests will be used~~
- ~~- Oct 26: statistical methods run~~
- ~~Nov 2: analyze results~~
- ~~Nov 9: works on data visualization/cli(time permitting)~~
- Nov 16: Have presentation prepared and rehearsed
- Nov 19: Present! :) 


## TODO
- [x] Clean Atlas CSV dataset (turn into .db file), clean census data (all)
- [x] Load data into python files (Jupyter notebook setup) (all)
- [x] Investigate census data
- [x] Investigate what methods we want to use for analysis
- [x] Write more detailed proposal
- [x] Add figure numbers in report

## Environment & Dependencies
* Click API used to created CLI in Python
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

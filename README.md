# Algorithms For the People Final Project

## Schedule



## Notes
- Should we do a prediction test, and then as a reach goal have this website that we develop to predict how many cameras would be on someone based on their demographic data
- something like this as inspiration: https://cs.brown.edu/courses/csci1951-a/projects/project_poster/Cam%20Spotter/poster.pdf
- If we don't have the website we could have a hypothesis test too.  If we do this, should we have some research question?


## TODO
- [ ] clean Atlas csv dataset (turn into .db file)
- [x] investigate census data
- [ ] investigate what methods we want to use for analysis
- [ ] write more detailed proposal

## Atlas of Surveillance
The Atlas of Surveillance (AoS) is an EFF database of the surveillance technology owned and operated by
local law enforcement agencies. The DB can be downloaded as a csv (it’s about 3MB). In this project you
will use the data in AoS to investigate how surveillance equipment is distributed across the US as a function
of the racial and ethnic composition of a county, the median household income of a county, and any other
characteristics you find interesting. To do this you will need other sources of data like the Census.

https://atlasofsurveillance.org/

## Data

**us-census-demographic-data**: https://www.kaggle.com/muonneutrino/us-census-demographic-data This dataset includes demographic data from throughout the US from 2015-2017.  This works well with the Atlas of Surveillance dataset because it includes data from before 2015 as recent as 2020.  It contains gender and race for different counties and states.  It is saved as a csv file in the us-census-data directory.

**atlas-of-surveillance**

## Environment & Dependencies
* sqlite database 
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

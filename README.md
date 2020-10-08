# Algorithms For the People Final Project

## TODO
- [ ] clean Atlas csv dataset (turn into .db file)
- [ ] investigate census data
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

**potential dataset**: https://www.kaggle.com/muonneutrino/us-census-demographic-data

**demographic**: this contains the accumulated populations for 2016, 2017, and
2018 for each region, by age and sex. That is, for one row of the table, this gives
the total number (in 2016, 2017, and 2018) of people of that age and that gender
for the specific region.

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

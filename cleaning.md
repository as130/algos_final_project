## Cleaning

In order to perform cleaning the following SQL queries were run over the Atlas table for each state

```
UPDATE Atlas_of_Surveillance_20201007 SET State = "Wyoming" WHERE State == "WY";
```

so that state names were consistent across all states.

Furthermore, we had to append county to the end of each conuty name as follows in the census datasets:

```
UPDATE acs2017_county_data SET County = County + ' County' WHERE NOT County LIKE '%County%';
```

We also imported the three csv files from our two different datasets and put them into one DB file with three tables.

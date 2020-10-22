ML_DATA_QUERY = '''
                SELECT 
                    (Atlas_of_surveillance_20201007.State || \' \' || Atlas_of_Surveillance_20201007.County),
                    acs2015_county_data.Black, 
                    acs2015_county_data.TotalPop, 
                    acs2015_county_data.Poverty,
                    acs2015_county_data.Men,
                    acs2015_county_data.Women,
                    acs2015_county_data.White,
                    acs2015_county_data.Native,
                    acs2015_county_data.Hispanic,
                    acs2015_county_data.Asian,
                    acs2015_county_data.Pacific,
                    acs2015_county_data.Income,
                    acs2015_county_data.Drive,
                    acs2015_county_data.Walk,
                    acs2015_county_data.Transit,
                    acs2015_county_data.Professional,
                    acs2015_county_data.WorkAtHome,
                    acs2015_county_data.Unemployment,
                    acs2015_county_data.SelfEmployed,
                    acs2015_county_data.Professional,
                    acs2015_county_data.Employed
                FROM Atlas_of_Surveillance_20201007, acs2015_county_data
                WHERE (acs2015_county_data.State || acs2015_county_data.County) = (Atlas_of_Surveillance_20201007.State || Atlas_of_Surveillance_20201007.County);
                '''

JOIN_QUERY = '''SELECT 
                       acs2015_county_data.Black, 
                       acs2015_county_data.TotalPop, 
                       (Atlas_of_surveillance_20201007.State || \' \' || Atlas_of_Surveillance_20201007.County), 
                       acs2015_county_data.Poverty 
                FROM 
                       Atlas_of_Surveillance_20201007, 
                       acs2015_county_data 
                WHERE 
                       (acs2015_county_data.State || acs2015_county_data.County) = (Atlas_of_Surveillance_20201007.State || Atlas_of_Surveillance_20201007.County) 
                           AND 
                        Atlas_of_Surveillance_20201007.Technology = ?;
            '''

DISTINCT_TECH = 'SELECT DISTINCT Technology FROM Atlas_of_Surveillance_20201007;'

COUNT_QUERY = 'SELECT * FROM acs2015_county_data INNER JOIN Atlas_of_Surveillance_20201007 ON acs2015_county_data.County = Atlas_of_Surveillance_20201007.County'

LIST_TABLES_CMD = "SELECT name FROM sqlite_master WHERE type='table';"

LIST_COLUMNS_CMD_ATLAS = "PRAGMA table_info('Atlas_of_Surveillance_20201007');"

LIST_COLUMNS_CMD_2015 = "PRAGMA table_info('acs2015_county_data');"

LIST_COLUMNS_CMD_2017 = "PRAGMA table_info('acs2017_county_data');"

SELECT_TOTAL_POP_2015 = "SELECT TotalPop from acs2015_county_data"


SELECT_BLACK_2015 = "SELECT Black from acs2015_county_data"

SELECT_STATE_2015 = "SELECT State from acs2015_county_data"

CLEAN_STATES = "UPDATE Atlas_of_Surveillance_20201007 SET State = \'%s\' WHERE State = \'%s\';"

UPDATE_COUNTIES_2015 = "UPDATE acs2015_county_data SET County = County + ' County' WHERE NOT County LIKE '%County%';"

UPDATE_COUNTIES_2017 = "UPDATE acs2017_county_data SET County = County + ' County' WHERE NOT County LIKE '%County%';"


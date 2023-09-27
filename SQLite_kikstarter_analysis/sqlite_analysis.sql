
-- Get almost successful projects
SELECT main_category, goal, backers, pledged, pledged / goal AS pct_pledged,
	   CASE
	   WHEN pledged / goal >= 1 THEN "Fully funded"
	   WHEN pledged / goal BETWEEN 0.75 AND 1 THEN "Nearly funded"
	   ELSE "Not nearly funded"
	   END AS funding_status
  FROM ksprojects
-- Filter out really small projects
 WHERE state IN ('failed') AND backers >= 10 AND pledged >= 10000 AND pct_pledged >= 0.95
 ORDER BY pct_pledged DESC;
-- There is a total of 34 projects which got almost funded (at least 95%)

-- Get the distribution of main_category of almost successful projects
SELECT main_category, COUNT(main_category)
  FROM ksprojects
 WHERE state IN ('failed') AND backers >= 10 AND pledged >= 10000 AND pledged / goal >= 0.95
 GROUP BY main_category
 ORDER BY COUNT(main_category) DESC;

-- Distribution of main_category's 26 at least 95% funded projects is:
Technology	    7
Design	        7
Music	        4
Film & Video	4
Games	        3
Theater	        2
Food	        2
Fashion	        2
Publishing	    1
Crafts	        1
Art	            1

-- Get some of the most successful projects
SELECT main_category, goal, backers, pledged, pledged / goal AS pct_pledged
  FROM ksprojects
-- Filter out really small projects
 WHERE state in ('successful') AND backers >= 10 AND pledged >= 10000 AND goal >= 10000 AND pct_pledged >= 50
 ORDER BY pct_pledged DESC;

-- Get the distribution of main_category of the most successful projects
SELECT main_category, COUNT(main_category)
  FROM ksprojects
 WHERE state IN('successful') AND backers >= 10 AND pledged >= 10000 AND goal >= 10000 AND pledged / goal >= 50
 GROUP BY main_category
 ORDER BY COUNT(main_category) DESC;

-- Distribution of main_category's 79 successful projects which got more the 50 times their goal is:
Design	    37
Technology	20
Games	    18
Food	    2
Fashion	    2


-- Get some of the worst performing projects except those where no one wanted to contribute
SELECT main_category, goal, backers, pledged, pledged / goal AS pct_pledged
  FROM ksprojects
-- Filter out really small projects
 WHERE state IN ('failed', 'canceled') AND goal >= 10000 AND pledged / goal >= 0.01 AND pledged / goal <= 0.05
 ORDER BY pct_pledged;
-- There is total of 19624 projects that recieved from 1 - 5% of the amout they were asking

-- Get distribution of main_category of 1 - 5% least successful projects
SELECT main_category, COUNT(main_category)
  FROM ksprojects
 WHERE state IN ('failed', 'canceled') AND goal >= 10000 AND pledged / goal >= 0.01 AND pledged / goal <= 0.05
 GROUP BY main_category
 ORDER BY COUNT(main_category) DESC;

-- Distribution of main_category's 19624 worst projects is:
Film & Video	3538
Technology	    3063
Design	        2636
Games	        2468
Food	        1775
Publishing	    1491
Fashion	        1279
Music	        1146
Art	            788
Photography	    349
Theater	        287
Comics	        286
Crafts	        240
Journalism	    209
Dance	        69
*/
-- Last but not least lets look at what type of projects are most and least common on kikstarter
SELECT main_category, COUNT(main_category)
  FROM ksprojects
 GROUP BY main_category
 ORDER BY COUNT(main_category) DESC;

-- Distribution of main_category on kikstarter is:
Film & Video	63585
Music	        51918
Publishing	    39874
Games	        35231
Technology	    32569
Design	        30070
Art	            28153
Food	        24602
Fashion	        22816
Theater	        10913
Comics	        10819
Photography	    10779
Crafts	        8809
Journalism	    4755
Dance	        3768
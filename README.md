# FInal
Final for Advanced Database


# Neo4j link to Game Database
http://35.160.116.116:7474/browser/   
Username: neo4j
Password: neo4j
Query to see all nodes/relationships: MATCH (n) RETURN n

# The basic use of my Python Script
I import the needed libraries, and connect to my neo4j instance. 
I loop through 1-500 (the db I used is missing some data, so 500 is a good amount) and set gid to i
Using json, I ping the api to get the results, and every loop I add gid to get a new game
Parsing the json I get the title, platform, publisher, developer, rating, genre, and amount of players 
Using session.run I make my cypher statement, creating the nodes and relationships systematically
I print to make sure it's running correctly
Using a continue to bypass the id's with no data

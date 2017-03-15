from request import *
import json
from neo4j.v1 import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://35.160.116.116:7687", auth=basic_auth("neo4j", "neo4j"))
session = driver.session()
for i in range(1,500):
	gid = str(i)
	try:
		gdata = json.load(urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20xml%20where%20url%20%3D%20%27http%3A%2F%2Fthegamesdb.net%2Fapi%2FGetGame.php%3Fid%3D' + gid + '%27&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'))
		gtitle = gdata["query"]['results']['Data']['Game']['GameTitle']
		gplatform = gdata['query']['results']['Data']['Game']['Platform'] + " is the Platform"
		gpublisher = gdata['query']['results']['Data']['Game']['Publisher'] + " is the Producer"
		gdeveloper = gdata['query']['results']['Data']['Game']['Developer'] + " is the Developer"
		grating = gdata['query']['results']['Data']['Game']['ESRB'] + " Rated"
		ggenre = gdata['query']['results']['Data']['Game']['Genres']['genre'] + " Genre(s)"
		gplayers = gdata['query']['results']['Data']['Game']['Players'] + " Player(s)"
		
		
		#session.run("CREATE (a:Person {name: {name}, title: {title}})",
              #{"name": "Arthur", "title": "King"})
		session.run("MERGE (g:GameTitle {name: {Title}}) MERGE (p:Platform {name: {Platform}}) MERGE (pub:Publisher {name: {Publisher}}) MERGE (dev:Developer {name: {Developer}}) MERGE (rate:Rating {name: {Rating}}) MERGE (gen:Genre {name: {Genre}}) MERGE (play:Players {name: {Players}}) MERGE (g) -[:PLATFORM]-> (p) MERGE (g) -[:PUBLISHED_BY]-> (pub) MERGE (g) -[:DEVELOPED_BY]-> (dev) MERGE (g) -[:RATING]-> (rate) MERGE (g) -[:GENRE]-> (gen) MERGE (g) -[:NUM_OF_PLAYERS]-> (play)",
			{"Title": gtitle, "Platform": gplatform, "Publisher": gpublisher, "Developer": gdeveloper, "Rating": grating, "Genre": ggenre, "Players": gplayers})
		print (gtitle, gplatform, gpublisher, gdeveloper, grating, ggenre, gplayers)
		
	except:
		continue
session.close()
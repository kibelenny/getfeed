# getfeed
This is a script that gets feeds links from websites. It consists of a main class Feed and three functions within the class.  
**Feed.get_feed()** returns the feeds link, both Atom and RSS (if present). If either is missing it is replaced by None.  
**Feed.get_rss()** will return the RSS link or none if missing.  
**Feed.get_atom()** will return the Atom link or none if missing.  
  
```py
from getfeed.feed import Feed

feed = Feed('https://gizmodo.com/tech')  
feed.get_feed()  

#Output
#('https://gizmodo.com/rss', None)

#Recoomended way to use it
rss, atom = feed.get_feed()

rss
#Output
#'https://gizmodo.com/rss'

atom
#Output is None

rss = feed.get_rss()
#Output
#'https://gizmodo.com/rss'

atom = feed.get_atom()
#Output will return None as this site does not contain atom feeds
```

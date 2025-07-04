# Beautiful soup - python library for pulling data out of HTML and XML files 
# HTML and XML are structure languages 

# html parser - parses through the file 

# 🥣 Beautiful Soup – Core Concepts

# find(tag) → returns the first matching tag.
# soup.find('a')         # First <a> tag

# find_all(tag) → returns a list of all matching tags.
# soup.find_all('a')     # All <a> tags

# 📝 Extracting Content

# Get text from tag:
   # for tag in soup.find_all('a'):
   #     print(tag.getText())
   
# Get attributes from tag:
   # for tag in soup.find_all('a'):
   #     print(tag.get('href'))  # or tag['href']
   
# 🎯 Finding by Attributes

# By ID:
  # soup.find(name='h1', id='name')
  
# By class (⚠️ class is reserved in Python):
  # soup.find(name='h3', class_='heading')  # use `class_`, not `class`

# 🧱 CSS Selector Reference 
# Selector          	Meaning
# tag               	All <tag> elements
# .class            	All elements with that class
# #id               	Element with that ID
# tag.class	            Specific tag & class
# tag1 tag2	            Nested (descendant) tag2 inside tag1
# div > p           	Direct child p of div

# beautiful soup 
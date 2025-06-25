# CSS _ Cascading STyle Sheets 

# type of langauge - to specify how things should look for the website
# there are other tyoes od STyle sheet languages Sass- Syntax awesome Style sheet 
#                                                Less - Leaner Css 

# in line CSS  -- not very much recommended 

# internal CSS - not suitable for Multi page website 

# external css - we write this in a seperate file 


# CSS SELECTOR --  1. element selector , 2. Class Selector , 3. ID Selector , 4.Attribute Selector, 5. Universal Selector 


#  ********************ELEMENT SELCTOR*********************** 
# Targets all elements of a specific HTML tag.
#✅Use when styling all tags like p, h1, a
# h2 {
#   color: red;
# }



# *******************CLASS SECTOR*********************** 
#  Syntax: .className { property: value; }
# Targets all elements with the given class attribute.
# Can apply to multiple, different HTML tags.
#  Example:
# .red-text {
#   color: red;
# }
# ✅ Use for reusable styling across elements.


# ********************ID Selector******************
# Syntax: #idName { property: value; }
# Targets a single, unique element with the given id.
# Should only be used once per HTML file.
# Example:
# #main {
#   color: green;
# }
# ⚠️ IDs must be unique in each HTML file.


# *************** Attribute Selector*****************
# Syntax (basic): element[attribute] { ... }
# Syntax (value-specific): element[attribute="value"] { ... }
# Targets elements with a specific attribute or attribute-value pair.
# Example:
# p[draggable] {
#   color: red;
# }

# p[draggable="false"] {
#   color: blue;
# }
# ✅ Great for targeting elements with attributes like draggable, value, src, etc.


#  *************** Universal Selector*************** 
# Syntax: * { ... }
# Targets all elements in the document.
# Example:
# * {
#   text-align: center;
# }
# ⚠️ Use with caution; affects every element.



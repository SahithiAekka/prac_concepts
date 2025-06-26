# font-size

# font-weight

# font-family -- types like sans, sans srif 

# text-align-- right left center top bottom 

# ****************** FONT SIZE ************************
# Unit    	    Description	                            Relative?	        Equivalent
# px      	        Pixels — fixed size	                ❌	           1px = ~0.26mm
# pt      	        Points — used in print (Word, etc.)	❌	           1pt = 1/72 inch (~0.35mm)
# em      	        Relative to parent font size	    ✅	           2em = 2× parent size
# rem     	        Relative to root (html) font size	✅	           1rem = 1× root font size
# large, x-large	    Named sizes	                    ✅	            Browser-dependent

# rem > em for maintainable, predictable design
# Always provide fallback fonts



# Use text-align for layout control

# *********************** Font Weight ******************
# Keywords: normal, bold, lighter, bolder
# Numeric scale: 100 (thin) → 900 (extra bold)
# Use numeric font-weights for fine control
# 🎯 font-weight: 900; is very bold
# 🎯 lighter makes font weight 100 less than the parent
# Adjust html font-size to scale entire UI


# Every HTML element is treated as a box. The box model defines how its layout is calculated using:
# Content-  actual text or image.
# Padding - space inside the border, around the content.
# Border - wraps the padding and content.
# Margin - space outside the border, separating elements.


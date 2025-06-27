from bs4 import BeautifulSoup

# Load and parse the HTML
with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# 1. Get the <title> text
print("Page Title:", soup.title.string)

# 2. Get the <h1> with id="name"
name_tag = soup.find("h1", id="name")
print("Name:", name_tag.getText())

# 3. Get the first paragraph
first_paragraph = soup.find("p")
print("First Paragraph:", first_paragraph.getText())

# 4. Get the link inside the <strong> inside the <em>
aws_link = soup.select_one("p em strong a")
print("AWS Topic Link:", aws_link.get("href"))

# 5. Get the list of certifications from <ul>
certifications = soup.select("ul li")
print("Certifications:")
for cert in certifications:
    print("-", cert.getText())

# 6. Get all external links under "Other pages" section
other_links = soup.select("body > a")
print("Other Links:")
for link in other_links:
    print("-", link.get("href"))

from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.p) # finds the first p tag
print(soup.p.getText()) # gets the inner text
print(soup.find_all(name="p"))  # finds all p tags

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href")) # to get attributes

heading = soup.find(name="h1", id="name")

print(heading)

# class is a reserved keyword
section_heading = soup.find(name="h3", class_="heading") 
print(section_heading)

# using CSS selectors
company_url = soup.select_one(selector="p a")
print(company_url)

headings = soup.select(".heading")
print(headings)
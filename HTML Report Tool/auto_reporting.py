from jinja2 import FileSystemLoader, Environment


# Content to be published
content = "Hello World"

# locate template
env = Environment(
	loader=FileSystemLoader(searchpath="template")
)

base_template = env.get_template("report.html")
table_section_template = env.get_template("table_section.html")

# Content
title = "Test Report"
sections = list()
sections.append(table_section_template.render(
    model="VGG19",
    dataset="VGG19_results.csv",
    table="Table goes here."
))
sections.append(table_section_template.render(
    model="MobileNet",
    dataset="MobileNet_results.csv",
    table="Table goes here."
))

def main():
	with open("output/report.html", "w") as f:
		f.write(base_template.render(            
			title=title,
            sections=sections
		))
		
if __name__ == "__main__":
	main()
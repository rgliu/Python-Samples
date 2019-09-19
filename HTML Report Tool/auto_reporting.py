from jinja2 import FileSystemLoader, Environment


# Content to be published
content = "Hello World"

# locate template
env = Environment(
	loader=FileSystemLoader(searchpath="template")
)

template = env.get_template("report.html")

def main():
	with open("output/report.html", "w") as f:
		f.write(template.render(content=content))
		
if __name__ == "__main__":
	main()
from pylatex import Document, Section
doc = Document()

with doc.create(Section("Our section title")):
    doc.append("Simple example")
doc.generate_pdf('pylatex_example_output')
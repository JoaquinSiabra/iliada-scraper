import xmltodict, json

#o = xmltodict.parse('<e> <a>text</a> <a>text</a> </e>')
with open('salida.xml', encoding="utf8") as fd:
	o = xmltodict.parse(fd.read())
	#o = xmltodict.parse('salida.xml')
	j=json.dumps(o) # '{"e": {"a": ["text", "text"]}}'
	print(j)
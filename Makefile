RESOURCE_FILE = resources.qrc
RESOURCE = resources.py

resources: $(RESOURCE_FILE)
	pyrcc5 -o $(RESOURCE) $(RESOURCE_FILE)

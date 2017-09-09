RESOURCE_FILE = resources.qrc
RESOURCE = pythot/resources_rc.py
UI_FILES = window.ui operation.ui about.ui
UI = $(UI_FILES:%.ui=pythot/%.py)

test:
	python -m pythot.tests

run: all
	python -m pythot

all: ui resources

ui: $(UI)

resources: $(RESOURCE)

pythot/%.py: %.ui
	pyuic5 --from-imports -o $@ $<

$(RESOURCE): $(RESOURCE_FILE)
	pyrcc5  -o $(RESOURCE) $(RESOURCE_FILE)

clean:
	rm -f $(RESOURCE) $(UI)

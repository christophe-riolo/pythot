RESOURCE_FILE = resources.qrc
RESOURCE = pythot/resources_rc.py
UI_FILE = pythot.ui
UI = pythot/window.py

all: ui resources

ui: $(UI_FILE)
	pyuic5 --from-imports -o $(UI) $(UI_FILE)

resources: $(RESOURCE_FILE)
	pyrcc5  -o $(RESOURCE) $(RESOURCE_FILE)

test:
	python -m pythot.tests.test_equations

clean:
	rm -f $(RESOURCE) $(UI)

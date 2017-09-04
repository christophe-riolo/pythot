RESOURCE_FILE = resources.qrc
RESOURCE = pythot/resources_rc.py
UI_FILES = window.ui value_decimal.ui value_fraction.ui operation.ui
UI = $(foreach file, $(UI_FILES), pythot/$(file:.ui=.py))

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

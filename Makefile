RESOURCE_FILE = resources.qrc
RESOURCE = pythot/resources_rc.py
UI = pythot/window.py pythot/value_decimal.py pythot/value_fraction.py

all: ui resources

ui: $(UI)

resources: $(RESOURCE)

pythot/window.py:
	pyuic5 --from-imports -o pythot/window.py pythot.ui

pythot/value_decimal.py:
	pyuic5 --from-imports -o pythot/value_decimal.py value_decimal.ui

pythot/value_fraction.py:
	pyuic5 --from-imports -o pythot/value_fraction.py value_fraction.ui

$(RESOURCE): $(RESOURCE_FILE)
	pyrcc5  -o $(RESOURCE) $(RESOURCE_FILE)

test:
	python -m pythot.tests.test_equations

clean:
	rm -f $(RESOURCE) $(UI)

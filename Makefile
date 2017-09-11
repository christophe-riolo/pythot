VERSION = 0.7
RESOURCE_FILE = resources.qrc
RESOURCE = pythot/resources_rc.py
UI_FILES = window.ui operation.ui about.ui
UI = $(UI_FILES:%.ui=pythot/%.py)
HELP = help/aide.html help/doc.qch help/doc.qhc help/doc.qhp help/project.qhp help/doc.qhcp

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

help: help/doc.qhc

help/doc.qhc: help/doc.qhcp help/doc.qch
	qcollectiongenerator -o $@ $<

help/doc.qch: help/doc.qhp
	qhelpgenerator -o $@ $<

help/doc.qhcp help/doc.qhp: aide.rst
	mkdir -p help
	python2 rst2qhc.py $< -o help \
	    --namespace math.pythot \
	    --customfilter "Pythot $(VERSION)"\
	    --create-qhcp\
	    --filterattributes pythot:0.7
	mv help/project.qhp help/doc.qhp
	mv help/project.qhcp help/doc.qhcp

clean:
	rm -f $(RESOURCE) $(UI) $(HELP)

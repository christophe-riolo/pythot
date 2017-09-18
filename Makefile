VERSION = 1.0.1b
DATE = 17/09/2017
RESOURCE_FILE = resources.qrc
RESOURCE = pythot/resources_rc.py
UI_FILES = window.ui operation.ui about.ui help.ui new_eq.ui
UI = $(UI_FILES:%.ui=pythot/%.py)
README = README.rst
HELP_FILES = pythot/doc/doc.qch pythot/doc/doc.qhc

test:
	python -m pythot.tests

run: all
	python -m pythot

all: version ui resources help

ui: $(UI)

resources: $(RESOURCE)

help: $(HELP_FILES)

# version updating -------------------------------
version:
	if test -z "$$(sed -n '/Pythot v$(VERSION)/p;' about.ui)";\
	    then sed -E -i 's/Pythot v[[:digit:]]+(.[[:digit:]ab]+)*/Pythot v$(VERSION)/' about.ui;\
	fi
	if test -z "$$(sed -n '\#$(DATE)#p;' about.ui)";\
	    then sed -E -i 's#[[:digit:]]{2}/[[:digit:]]{2}/[[:digit:]ab]{4}#$(DATE)#' about.ui;\
	fi
	if test -z "$$(sed -n '/version $(VERSION)/p;' README.rst)";\
	    then sed -E -i 's/version [[:digit:]]+(.[[:digit:]ab]+)*/version $(VERSION)/' README.rst;\
	fi
	if test -z "$$(sed -n '/version=\"$(VERSION)\"/p;' setup.py)";\
	    then sed -E -i 's/version=\"[[:digit:]]+(.[[:digit:]ab]+)*\"/version=\"$(VERSION)\"/' setup.py;\
	fi

# UI compiling -----------------------------------
pythot/%.py: %.ui
	pyuic5 --from-imports -o $@ $<

# Resources compiling ----------------------------
$(RESOURCE): $(RESOURCE_FILE)
	pyrcc5  -o $(RESOURCE) $(RESOURCE_FILE)

# Help files compiling ---------------------------
pythot/doc/doc.qhc: pythot/doc/doc.qhcp pythot/doc/doc.qch
	qcollectiongenerator -o $@ $<

pythot/doc/doc.qch: pythot/doc/doc.qhp
	qhelpgenerator -o $@ $<

pythot/doc/doc.qhcp pythot/doc/doc.qhp: $(README)
	mkdir -p pythot/doc
	python rst2qhc.py $< -o pythot/doc \
	    --namespace math.pythot \
	    --customfilter "Pythot $(VERSION)"\
	    --create-qhcp\
	    --filterattributes pythot:0.7

# Cleaning ---------------------------------------
clean:
	rm -f $(RESOURCE) $(UI)
	rm -R pythot/doc

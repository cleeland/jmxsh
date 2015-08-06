# Simple "adapter" makefile that delegates to ant for build activities.

CASCADED_TARGETS = rpm publish clean

.PHONY:	all $(CASCADED_TARGETS)

all:	build.xml
	ant

$(CASCADED_TARGETS):	build.xml
	ant $@

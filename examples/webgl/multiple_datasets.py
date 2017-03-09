"""
===============================================
Create a 3D WebGL Viewer with Multiple Datasets
===============================================

A webgl viewer displays a 3D view of brain data in a web browser

Multiple datasets can be loaded into the same viewer

In the browser you can switch between datasets with the + and - keys

"""

import cortex

# gather multiple datasets
# the priority kwarg will determine the relative order of the datasets
volume1 = cortex.Volume.random(subject='S1', xfmname='fullhead', priority=1)
volume2 = cortex.Volume.random(subject='S1', xfmname='fullhead', priority=2)
volume3 = cortex.Volume.random(subject='S1', xfmname='fullhead', priority=3)
volumes = {
	'First Dataset': volume1,
	'Second Dataset': volume2,
	'Third Dataset': volume3,
}

# create viewer
cortex.webgl.show(data=volumes)
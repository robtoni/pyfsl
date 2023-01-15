## Python Fault Scaling Laws (pyfsl)

The module implements several fault scaling laws published in literature and 
here adapted using a mathematical coherent formulation.

The module consists of two main functions:
* **get_fault_size**: to get the dimension of interest of the fault among 
length (L), width (W) or area (A) from the magnitude.

* **get_magnitude**: to get the magnitude from one of the quantities L, W or A:



### Requirements:
Standard Python (https://www.python.org/) and Numpy (http://www.numpy.org/)


### Installation

Clone the repository or download the master branch folder (you need to create
a ssh key to pair your device with the repository).

```
git clone git@gitlab.rm.ingv.it:roberto.tonini/pyfsl.git
```

or just download it directly from this gitlab web page and unzip the pyfsl 
folder wherever you prefer.


### Usage:

Add the path of pysfl folder (PYFSL_PATH) to your Python sys.path and 
import the fsl module as follows:

```
import sys
sys.path.insert(0, PYFSL_PATH)

import fault_scaling_laws as fsl

# get length and width for a magnitude 7.0 using Wells & Coppersmith (WC94)
# scaling laws: L stands for Length, W stands for Width, 1 is a special code 
# depending on tectonic (always 1 for WC94) and AA stands for "All faults"
# (see Wells & Coppersmith, 1994, for more details on "All faults" meaning).
#
mag = 7.0    # magnitude
length = fsl.get_fault_size("WC94", "L", "AA", 1, mag)
width = fsl.get_fault_size("WC94", "W", "AA", 1, mag)

print(length, width)
48.97788193684461 16.98243652461745

```

See some examples in the tests/ directory




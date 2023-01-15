import os
import sys
# get the absolute path of the library with respect the local install
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fault_scaling_laws as fsl


# strasser 
print("\n##############\nSTRASSER")
print("\nGet Size from magnitude")
magnitudes = [4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
for mw in magnitudes:

    l_st = fsl.get_fault_size("ST10", "L", "UN", "3", mw, True) # length
    w_st = fsl.get_fault_size("ST10", "W", "UN", "3", mw) # width
    a_st = fsl.get_fault_size("ST10", "A", "UN", "3", mw) # area
    
    print("M = {:.1f} L = {:.3f} km W = {:.3f} km A/L = {:.3f} km".format(mw, \
          l_st, w_st, a_st/l_st))



print("\nGet Magnitude from Length")
lenghts = [20, 50, 100, 150, 200, 300]
for ll in lenghts:

    mw_st = fsl.get_magnitude("ST10", "L", "UN", "3", ll) 
    
    print("L = {:.3f} km M = {:.1f}".format(ll, mw_st))


print("\nGet Magnitude from Width")
widths = [20, 40, 60, 80, 100, 150]
for ww in widths:

    mw_st = fsl.get_magnitude("ST10", "L", "UN", "3", ww) 
    
    print("W = {:.3f} km M = {:.1f}".format(ww, mw_st))



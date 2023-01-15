#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
# get the absolute path of the library with respect the local install
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fault_scaling_laws as fsl

def slip(magnitude,area):
    m0 = np.power(10, (1.5*(magnitude+10.7333)))*1e-7
    mu = 3.0e10   # 30 GPa
    s = m0/(mu*area*1e6)
    return s 
  


magnitudes = np.arange(6.0, 8.2, 0.1)
n_magnitudes = len(magnitudes)


laws = ["Wells & Coppersmith", "Strasser interface",
        "Strasser intraslab", "Murotani"]

length = [ ["WC94", "L", "AA", "1"], ["ST10", "L", "UN", "3"],  
           ["ST10", "L", "UN", "4"] ]

width = [ ["WC94", "W", "AA", "1"], ["ST10", "W", "UN", "3"], 
          ["ST10", "W", "UN", "4"] ]

area = [ ["ST10", "A", "UN", "3"], ["ST10", "A", "UN", "4"], 
         ["MU13", "A", "RR", "3"] ]


le14_gar_l_nn = np.zeros((n_magnitudes))
le14_gar_w_ss = np.zeros((n_magnitudes))
le14_gar_a_nn = np.zeros((n_magnitudes))
le14_gar_l_ss = np.zeros((n_magnitudes))
le14_gar_w_nn = np.zeros((n_magnitudes))
le14_gar_a_ss = np.zeros((n_magnitudes))

le14_scr_l_nn = np.zeros((n_magnitudes))
le14_scr_w_ss = np.zeros((n_magnitudes))
le14_scr_a_nn = np.zeros((n_magnitudes))
le14_scr_l_ss = np.zeros((n_magnitudes))
le14_scr_w_nn = np.zeros((n_magnitudes))
le14_scr_a_ss = np.zeros((n_magnitudes))

le14_fss_l_ss = np.zeros((n_magnitudes))
le14_fss_w_ss = np.zeros((n_magnitudes))
le14_fss_a_ss = np.zeros((n_magnitudes))

for im, m in enumerate(magnitudes):
    if im == 0:
        prt = True
    else:
        prt = False

    le14_gar_l_nn[im] = fsl.get_fault_size("LE14", "L", "NN", "1", m, prt)
    le14_gar_l_ss[im] = fsl.get_fault_size("LE14", "L", "SS", "1", m, prt)
    le14_gar_w_nn[im] = fsl.get_fault_size("LE14", "W", "NN", "1", m, prt)
    le14_gar_w_ss[im] = fsl.get_fault_size("LE14", "W", "SS", "1", m, prt)
    le14_gar_a_nn[im] = fsl.get_fault_size("LE14", "A", "NN", "1", m, prt)
    le14_gar_a_ss[im] = fsl.get_fault_size("LE14", "A", "SS", "1", m, prt)

    le14_scr_l_nn[im] = fsl.get_fault_size("LE14", "L", "NN", "5", m, prt)
    le14_scr_l_ss[im] = fsl.get_fault_size("LE14", "L", "SS", "5", m, prt)
    le14_scr_w_nn[im] = fsl.get_fault_size("LE14", "W", "NN", "5", m, prt)
    le14_scr_w_ss[im] = fsl.get_fault_size("LE14", "W", "SS", "5", m, prt)
    le14_scr_a_nn[im] = fsl.get_fault_size("LE14", "A", "NN", "5", m, prt)
    le14_scr_a_ss[im] = fsl.get_fault_size("LE14", "A", "SS", "5", m, prt)

    le14_fss_l_ss[im] = fsl.get_fault_size("LE14", "L", "SS", "2", m, prt)
    le14_fss_w_ss[im] = fsl.get_fault_size("LE14", "W", "SS", "2", m, prt)
    le14_fss_a_ss[im] = fsl.get_fault_size("LE14", "A", "SS", "2", m, prt)



plt.figure(figsize=(8, 8))
plt.subplots_adjust(wspace=0.4)
#var1 = [le14_gar_a_nn, le14_gar_a_ss, le14_gar_l_nn*le14_gar_w_nn, le14_gar_l_ss*le14_gar_w_ss]
#var2 = [le14_scr_a_nn, le14_scr_a_ss, le14_scr_l_nn*le14_scr_w_nn, le14_scr_l_ss*le14_scr_w_ss]
#var3 = [le14_fss_a_ss, le14_fss_l_ss*le14_fss_w_ss]
#lbl1 = ['Area NN GAR', 'Area SS GAR', 'L*W NN GAR', 'L*W SS GAR']
#lbl2 = ['Area NN SCR', 'Area SS SCR', 'L*W NN SCR', 'L*W SS SCR']
#lbl3 = ['Area SS FSS', 'L*W SS FSS']
var1 = [le14_gar_l_nn, le14_scr_l_nn, le14_gar_l_ss, le14_scr_l_ss, le14_fss_l_ss]
var2 = [le14_gar_w_nn, le14_scr_w_nn, le14_gar_w_ss, le14_scr_w_ss, le14_fss_w_ss]
lbl1 = ['GAR NR', 'SCR NR', 'GAR SS', 'SCR SS', 'FSS SS']
lbl2 = ['GAR NR', 'SCR NR', 'GAR SS', 'SCR SS', 'FSS SS']
colors = ['#000000', '#ff0000', '#00ff00', '#0000ff', '#ff00ff']

plt.subplot(1, 2, 1)
plt.grid(True)
ax = plt.gca()
txt = ("Leonard 2014\n" 
       "GAR: Generic Active Region\n"
       "SCR: Stable Continental Region\n"
       "NR: Normal/Reverse\n"
       "SS: Strike-Slip")
plt.text(0.02, 1.02, txt, fontsize=10, transform=ax.transAxes)

for i in range(len(var1)):
    print(i, lbl1[i])
    plt.plot(magnitudes, var1[i], linewidth=1, color=colors[i], 
             markerfacecolor=colors[i], marker='o', 
             markersize=6, markeredgewidth=0, label=lbl1[i])

plt.legend(loc='upper left')
plt.xlabel("Magnitude")
plt.ylabel("Length (km)")

plt.subplot(1, 2, 2)
plt.grid(True)
for i in range(len(var2)):
    print(i, lbl2[i])
    plt.plot(magnitudes, var2[i], linewidth=1, color=colors[i],
             markerfacecolor=colors[i], marker='o', 
             markersize=6, markeredgewidth=0, label=lbl2[i])

plt.legend(loc='upper left')
plt.xlabel("Magnitude")
plt.ylabel("Width (km)")


plt.savefig("leonard.png", format="png")
sys.exit()

# wells coppersmith aa
l_wc, sl_wc = fsl.get_fault_size("WC94", "L", "AA", "1", mw)
w_wc, sw_wc = fsl.get_fault_size("WC94", "W", "AA", "1", mw)
s_wc = slip(mw,l_wc*w_wc) 

# strasser interface
l_st, sl_st = fsl.get_fault_size("ST10", "L", "UN", "3", mw)
w_st, sw_st = fsl.get_fault_size("ST10", "W", "UN", "3", mw)
a_st, sa_st = fsl.get_fault_size("ST10", "A", "UN", "3", mw)
s_st_lw = slip(mw,l_st*w_st)
s_st_a = slip(mw,a_st) 

# strasser intraslab
l_st_is, sl_st1 = fsl.get_fault_size("ST10", "L", "UN", "4", mw)
w_st_is, sw_st1 = fsl.get_fault_size("ST10", "W", "UN", "4", mw)
a_st_is, sa_st1 = fsl.get_fault_size("ST10", "A", "UN", "4", mw)
s_st_lw_is = slip(mw,l_st*w_st)
s_st_a_is = slip(mw,a_st) 

# murotani 2013
a_mu, sa_mu = fsl.get_fault_size("MU13", "A", "RR", "3", mw)
s_mu, sa_mu = fsl.get_fault_size("MU13", "S", "RR", "3", mw)



plt.figure(figsize=(14,10))
plt.hold(True)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                      wspace=0.3, hspace=0.3)

plt.subplot(2,1,1)
plt.plot(mw, mu, marker="o", markersize=5, label=key + " " + val[0])
plt.grid(b=True, which='major', color='#333333', linestyle='-')
plt.grid(b=True, which='minor', color='#999999', linestyle='--')

#plt.title("All Regions", fontsize=10)
plt.yscale("log")
plt.xlabel(r'Magnitude')
plt.ylabel(r'Slip (m)')
plt.legend(loc="upper left")
plt.savefig("scaling_laws.png", format="png", bbox_inches="tight")
plt.close()


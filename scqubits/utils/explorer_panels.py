# explorer_panels.py
#
# This file is part of scqubits.
#
#    Copyright (c) 2019, Jens Koch and Peter Groszkowski
#    All rights reserved.
#
#    This source code is licensed under the BSD-style license found in the
#    LICENSE file in the root directory of this source tree.
############################################################################

import scqubits.utils.sweep_plotting as splot
from scqubits.settings import DEFAULT_ENERGY_UNITS


def display_bare_spectrum(sweep, subsys, param_val, fig_ax):
    title = 'bare spectrum: subsystem {} ({})'.format(sweep.hilbertspace.index(subsys), subsys._sys_type)
    __ = splot.bare_spectrum(sweep, subsys, title=title, fig_ax=fig_ax)
    _, axes = fig_ax
    axes.axvline(param_val, color='gray', linestyle=':')


def display_bare_wavefunctions(sweep, subsys, param_val, fig_ax):
    title = 'wavefunctions: subsystem {} ({})'.format(sweep.hilbertspace.index(subsys), subsys._sys_type)
    __ = splot.bare_wavefunction(sweep, param_val, subsys, title=title, fig_ax=fig_ax)


def display_dressed_spectrum(sweep, initial_bare, final_bare, energy_initial, energy_final, param_val, fig_ax):
    energy_difference = energy_final - energy_initial
    title = r'{} $\rightarrow$ {}: {:.4f} {}'.format(initial_bare, final_bare, energy_difference, DEFAULT_ENERGY_UNITS)
    __ = splot.dressed_spectrum(sweep, title=title, fig_ax=fig_ax)
    _, axes = fig_ax
    axes.axvline(param_val, color='gray', linestyle=':')
    axes.scatter([param_val] * 2, [energy_initial, energy_final], s=40, c='gray')


def display_n_photon_qubit_transitions(sweep, photonnumber, initial_bare, param_val, fig_ax):
    title = r'{}-photon qubit transitions, {} $\rightarrow$'.format(photonnumber, initial_bare)
    __ = splot.n_photon_qubit_spectrum(sweep, photonnumber, initial_state_labels=initial_bare,
                                       title=title, fig_ax=fig_ax)
    _, axes = fig_ax
    axes.axvline(param_val, color='gray', linestyle=':')


def display_chi_01(sweep, qbt_index, osc_index, param_index, fig_ax):
    __ = splot.chi_01(sweep, qbt_index, osc_index, param_index=param_index, fig_ax=fig_ax)
    _, axes = fig_ax
    axes.axvline(sweep.param_vals[param_index], color='gray', linestyle=':')


def display_charge_matrixelems(sweep, initial_bare, qbt_subsys, param_val, fig_ax):
    qbt_index = sweep.hilbertspace.index(qbt_subsys)
    bare_qbt_initial = initial_bare[qbt_index]
    title = r'charge matrix elements for {} [{}]'.format(type(qbt_subsys).__name__, qbt_index)
    __ = splot.charge_matrixelem(sweep, qbt_index, bare_qbt_initial, title=title, fig_ax=fig_ax)
    _, axes = fig_ax
    axes.axvline(param_val, color='gray', linestyle=':')

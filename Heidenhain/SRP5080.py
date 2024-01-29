#
# Copyright (c) 2024 Gonzalo J. Carracedo <BatchDrake@gmail.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import RZLink as link
import numpy  as np

SRP5080_WOBBLE_PHASE        = 0   # deg
SRP5080_AXIAL_RUNOUT_PHASE  = 90  # deg
SRP5080_RADIAL_RUNOUT_PHASE = 0   # deg
SRP5080_PERIODICITY         = 20  # dimensionless

def SRP5080_wobble(theta):
    return np.cos(np.deg2rad(SRP5080_PERIODICITY * theta + SRP5080_WOBBLE_PHASE))

def SRP5080_axial_runout(theta):
    return np.cos(np.deg2rad(SRP5080_PERIODICITY * theta + SRP5080_AXIAL_RUNOUT_PHASE))

def SRP5080_radial_runout(theta):
    return np.cos(np.deg2rad(SRP5080_PERIODICITY * theta + SRP5080_RADIAL_RUNOUT_PHASE))

link.register("SRP5080_wobble",        1, SRP5080_wobble)
link.register("SRP5080_axial_runout",  1, SRP5080_axial_runout)
link.register("SRP5080_radial_runout", 1, SRP5080_radial_runout)

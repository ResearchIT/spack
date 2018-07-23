##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import glob

class Wrf(AutotoolsPackage):
    """The Weather Research and Forecasting (WRF) Model
    is a next-generation mesoscale numerical weather prediction system designed
    for both atmospheric research and operational forecasting applications"""

    homepage = "https://www.mmm.ucar.edu/weather-research-and-forecasting-model"
    url      = "http://www2.mmm.ucar.edu/wrf/src/WRFV3.9.1.TAR.gz"

    version('4.0',     'f506a2ebfe3eed87d0f97927b22574a2')
    version('3.9.1.1', '11b19933a3b1fee2d91b8d19c0893958')

    depends_on('mpi')
    depends_on('netcdf')
    depends_on('netcdf-fortran')
    depends_on('jasper')
    depends_on('libpng')
    depends_on('zlib')
    depends_on('perl')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('m4', type='build')
    depends_on('libtool', type='build')

    def setup_environment(self, spack_env, run_env):
        spack_env.set('NETCDF', self.spec['netcdf-fortran'].prefix)

    def patch(self):
        # Make configure scripts use Spack's tcsh
        files = glob.glob('*.csh')

        filter_file('^#!/bin/csh -f', '#!/usr/bin/env csh', *files)
        filter_file('^#!/bin/csh', '#!/usr/bin/env csh', *files)

    def configure(self, spec, prefix):
        install_answer = ['35\n', '3\n']
        install_answer_input = 'spack-config.in'
        with open(install_answer_input, 'w') as f:
            f.writelines(install_answer)
        with open(install_answer_input, 'r') as f:
            bash = which('bash')
            bash('./configure', input=f)


    def build(self, spec, prefix):
        sh = which('sh')
        sh('./compile', 'em_real')

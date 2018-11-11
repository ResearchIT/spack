# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import glob

class Wrf(AutotoolsPackage):
    """The Weather Research and Forecasting (WRF) Model
    is a next-generation mesoscale numerical weather prediction system designed
    for both atmospheric research and operational forecasting applications"""

    homepage = "https://www.mmm.ucar.edu/weather-research-and-forecasting-model"
    url      = "http://www2.mmm.ucar.edu/wrf/src/WRFV3.9.1.TAR.gz"

    version('4.0', sha256='a5b072492746f96a926badda7e6b44cb0af26695afdd6c029a94de5e1e5eec73')
    version('3.9.1.1', sha256='e2c503c1b5adc2d3409b39d37df29d60188ff1de8c870eca15197a86d3538299')

    #phases= ['autoreconf', 'patch', 'configure', 'build']

    depends_on('mpi')
    depends_on('netcdf')
    depends_on('netcdf-fortran')
    depends_on('jasper')
    depends_on('libpng')
    depends_on('zlib')
    depends_on('perl')
    depends_on('hdf5')
    depends_on('tcsh', type=('build'))

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('m4', type='build')
    depends_on('libtool', type='build')

    def setup_environment(self, spack_env, run_env):
        spack_env.set('NETCDF', self.spec['netcdf'].prefix)
        spack_env.set('NETCDFF', self.spec['netcdf-fortran'].prefix)

    @run_after('autoreconf')
    def patch2(self):
        # Make configure scripts use Spack's tcsh
        files = glob.glob('*.csh')

        filter_file('^#!/bin/csh -f', '#!/usr/bin/env csh', *files)
        filter_file('^#!/bin/csh', '#!/usr/bin/env csh', *files)

    patch('Config.pl.patch')
    patch('configure.defaults.patch')
    patch('conf_tokens.patch')
    patch('postamble.patch')
    patch('configure.patch')
    patch('makefile.patch')
    patch('Makefile.patch')

    def configure(self, spec, prefix):
        install_answer = ['35\n', '3\n']
        install_answer_input = 'spack-config.in'
        with open(install_answer_input, 'w') as f:
            f.writelines(install_answer)
        with open(install_answer_input, 'r') as f:
            bash = which('bash')
            bash('./configure', input=f)


    def build(self, spec, prefix):
        sh = which('csh')
        sh('./compile', 'em_real')

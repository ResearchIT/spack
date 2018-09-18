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
import os
import glob


class Simnibs(PythonPackage):
    """SimNIBS 2.1 is a free software package for the Simulation of
       Non-invasive Brain Stimulation. It allows for realistic calculations
       of the electric field induced by transcranial magnetic stimulation (TMS)
       and transcranial direct current stimulation (tDCS).

       Downloading SimNIBS requires registering an account so Spack will
       search the current working directory for the source package. """

    homepage = "http://simnibs.de"
    url      = "file://{0}/simnibs-2.1.1-Linux64.tar.gz".format(os.getcwd())

    version('2.1.1', sha256='1200d5ba52a3982785a6f7292136e740cdbf627bc8e1d44f84f0c5afc97c84e0')

    depends_on('python+ucs4@2.7.14', type=('build', 'run'))
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-h5py@2.7.1:', type=('build', 'run'))
    depends_on('py-numpy@1.13.3:', type=('build', 'run'))
    depends_on('py-pytest@3.3.2:', type=('build', 'run'))
    #depends_on('py-pyqt', type=('build', 'run'))
    depends_on('qt@5.6.2:', type=('build', 'run'))
    depends_on('py-scipy@1.0.0:', type=('build', 'run'))
    depends_on('py-babel@2.2.1:', type=('build', 'run'))

    def build(self, spec, prefix):
        with working_dir('Python_modules/src'):
            python('setup.py', 'develop', '--prefix={0}'.format(prefix))

    def install(self, spec, prefix):
        # there is an interactive installer but it is not very configurable.
        # we manually perform most of the steps that the installer would
        # SimNIBS manages python dependencies by setting up miniconda,
        # but we'll avoid that and use our own python

        files = glob.glob('Python_modules/*.py')

        for f in files:
            # ensure that each python start file has a shebang
            filter_file('# -*- coding: utf-8 -*-', '#/usr/bin/python2 -u',
                        f, string=True)
            set_executable(f)
            install(f, prefix.bin)

    def url_for_version(self, version):
        url = "file://{0}/simnibs-{1}-Linux64.tar.gz"
        return url.format(os.getcwd(), version.dotted)

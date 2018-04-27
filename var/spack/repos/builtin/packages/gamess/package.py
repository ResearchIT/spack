##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
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
from distutils.dir_util import copy_tree
import os
import subprocess
import sys

class Gamess(Package):
    """The General Atomic and Molecular Electronic Structure System (GAMESS) is a general ab initio quantum chemistry package."""

    homepage = "http://www.msg.ameslab.gov/gamess"

    version('development', '7bee8588b399f265976228cde8f75515', url="file://%s/gamess.tar.gz" % os.getcwd())

    depends_on('atlas')
    depends_on('mpi')

#   parallel = False

    def install(self, spec, prefix):
        # Maybe allow users to control the versioning name?
        gamess_version_name='00'
        #
        atlas = spec['atlas'].libs
        mpi = spec['mpi'].libs

        # We start in $GMS_DIR

        # Compile actvte
        #
        # Copy $GMS_DIR/tools/actvte.code to $GMS_DIR/actvte.f
        install('tools/actvte.code','actvte.f')
        # sed hack actvte.f
        if sys.platform == "darwin" or sys.platform == "linux":
            filter_file(r'\*UNX','    ','actvte.f')
            # compile actvte.x
            subprocess.call([spack_fc,'-o',join_path(os.getcwd(),'tools/actvte.x'),'actvte.f'])

        # Build GAMESS
        subprocess.call(['./bin/create-install-info.py', \
            '--target','linux64', \
            '--fortran',os.path.basename(spack_fc), \
            '--fortran_version',spec.format('${COMPILERVER}'), \
            '--math','atlas', \
            '--mathlib_path',''.join(atlas.directories), \
            '--ddi_comm','mpi', \
            '--mpi_lib','openmpi', \
            '--mpi_path',ancestor(''.join(mpi.directories),n=1), \
            '--version',gamess_version_name, \
            '--rungms'
            ])

        # Create object directory
        mkdirp('object')

        # Build DDI first
        make('ddi')

        try:
            make()
        except:
            pass

        make()

        # Copy directory structure at the build location
        #
        # $GMS_BUILD_DIR/auxdata
        copy_tree('auxdata',join_path(prefix,'auxdata'))
        # $GMS_BUILD_DIR/tests
        copy_tree('tests',join_path(prefix,'tests'))

        # Copy compiled contents over to the build directory
        #
        # Copy $GMS_DIR/gamess.*.x
        install('gamess.{0}.x'.format(gamess_version_name),prefix)
        # Copy $GMS_DIR/libddi.a
        if os.path.isfile('libddi.a'):
            install('libddi.a',prefix)
        # Copy $GMS_DIR/ddikick.x
        if os.path.isfile('ddikick.x'):
            install('ddikick.x',prefix)

        # Copy necessary files to permit the execution of GAMESS
        #
        # Copy $GMS_DIR/gms-files.csh
        install('gms-files.csh',prefix)
        # Copy $GMS_DIR/install.info
        install('install.info',prefix)
        # Copy $GMS_DIR/rungms
        install('rungms',prefix)

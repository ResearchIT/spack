##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
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
from spack.environment import EnvironmentModifications
import distutils.dir_util
import os


class Freesurfer(Package):
    """An open source software suite for processing and analyzing (human)
       brain MRI images."""

    homepage = "https://surfer.nmr.mgh.harvard.edu/"
    url      = "ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz"

    version('6.0.0', 'd49e9dd61d6467f65b9582bddec653a4')

    depends_on('mesa-glu')
    depends_on('libpng@1.2.57')
    depends_on('libxscrnsaver')
    depends_on('libxft')
    depends_on('tk')
    depends_on('qt')

    # Licensing
    license_required = True
    license_comment  = '#'
    license_files    = ['license.txt']
    license_url      = 'https://surfer.nmr.mgh.harvard.edu/registration.html'

    def install(self, spec, prefix):
        distutils.dir_util.copy_tree(".", prefix)

    # This isn't working right now
    def setup_enivronment(self, spack_env, run_env):
        run_env.set('FREESURFER_HOME', self.prefix)
        spack_env.set('FREESURFER_HOME', self.prefix)

        if not self.stage.source_path:
            self.stage.fetch()
            self.stage.expand_archive()

        freevars = join_path(self.stage.source_path, 'SetUpFreeSurfer.sh')
        spack_env.extend(EnvironmentModifications.from_sourcing_file(freevars))
        freerun = join_path(self.prefix, 'SetUpFreeSurfer.sh')
        run_env.extend(EnvironmentModifications.from_sourcing_file(freerun))

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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install karma
#
# You can edit this file again by typing:
#
#     spack edit karma
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Karma(Package):
    """Karma is a toolkit for interprocess communications, authentication,
    encryption, graphics display, user interface and manipulating the Karma
    network data structure. It contains KarmaLib (the structured libraries
    and API) and a large number of modules (applications)
    to perform many standard tasks. """

    homepage = "https://www.atnf.csiro.au/computing/software/karma/"
    url      = "ftp://ftp.atnf.csiro.au/pub/software/karma/karma-1.7.25-common.tar.bz2"

    version('1.7.25-common', sha256='afda682d79c0923df5a6c447a32b09294da1582933abae3205c008104da54fbd')

    depends_on('libx11', type=('build', 'run'))
    depends_on('libxaw', type=('build', 'run'))

    phases = ['install']

    resource(
                name='karma-linux',
                url='ftp://ftp.atnf.csiro.au/pub/software/karma/karma-1.7.25-amd64_Linux_libc6.3.tar.bz2',
                sha256='effc3ed61c28b966b357147d90357d03c22d743c6af6edb49a863c6eb625a441',
                destination='./'
               )

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('LIBRARY_PATH', self.prefix.lib)
        run_env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)

    def install(self, spec, prefix):
        install_tree('./karma-1.7.25/amd64_Linux_libc6.3/bin', prefix.bin)
        install_tree('./karma-1.7.25/amd64_Linux_libc6.3/lib', prefix.lib)

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

class Migrate(AutotoolsPackage):
    """Migrate estimates population parameters, effective population sizes
       and migration rates of n populations, using genetic data.  It
       uses a coalescent theory approach taking into account history of
       mutations and uncertainty of the genealogy."""

    homepage = "http://popgen.sc.fsu.edu/Migrate/Migrate-n.html"
    url      = "http://popgen.sc.fsu.edu/currentversions/migrate-3.6.11.src.tar.gz"

    version('3.6.11', 'acefb8539ec3e1be01213cef21035b045dc3adbf')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')
    depends_on('mpi')

    def install(self, spec, prefix):
        configure()
        make('mpis')
        make('install')

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
#     spack install py-pycogent
#
# You can edit this file again by typing:
#
#     spack edit py-pycogent
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyPycogent(PythonPackage):

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://pycogent.org/"
    url      = "https://github.com/pycogent/pycogent/archive/1.9.tar.gz"

    version('1.9', sha256='c9f56d21d764aa62e3e8a9df5a300eb7fb59e502572bec41894d21df19aeceb5')

    variant('matplotlib', default=False, description="graphs related to codon usage") 
    variant('cython', default=False, description="This module is only necessary .pyx files.")
    variant('mpi', default=False, description='MPI required for parallel computation.')
    variant('SQLAlchemy', default=False, description='Required for the Ensembl querying code.')
    
    depends_on('python@2.7.15')
    depends_on('py-numpy')
    depends_on('zlib')
    depends_on('matplotlib', when='+matplotlib')
    depends_on('cython', when='+cython')
    depends_on('mpi', when='+mpi')
    depends_on('sqlalchemy', when='+sqlalchemy')


#    def build_args(self, spec, prefix):
#        args = []
#        return args

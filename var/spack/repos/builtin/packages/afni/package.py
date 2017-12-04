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


class Afni(MakefilePackage):
    """AFNI (Analysis of Functional NeuroImages) is a set of C programs for
       processing, analyzing, and displaying functional MRI (FMRI) data - a
       technique for mapping human brain activity."""

    homepage = "https://afni.nimh.nih.gov/"
    url      = "https://afni.nimh.nih.gov/pub/dist/tgz/afni_src.tgz"

    version('2017-9-27', '0123456789abcdef0123456789abcdef')

    depends_on('motif')
    depends_on('tcsh')
    depends_on('libxp')
    depends_on('gsl')
    depends_on('py-pyqt')
    depends_on('r', type=('build', 'run'))
    depends_on('libpng')
    depends_on('xorg-server')

    def build(self, spec, prefix):
        make('-f', 'Makefile_linux_g++')

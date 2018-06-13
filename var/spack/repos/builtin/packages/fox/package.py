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
#import glob


class Fox(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://www.example.com"
    url      = "https://sourceforge.net/projects/objcryst/files/Fox%20%28Linux%2C%20source%20code%29/1.9.8.0/Fox-1.9.8-R1352.tar.bz2"

    version('1.9.8-R1352', '058d57754145902bfb725f98aafb011e')

    depends_on('gl')
    depends_on('wx')
    depends_on('newmat')
    depends_on('freeglut')
    depends_on('fftw')
    depends_on('mariadb')

    def build(self, spec, prefix):
        with working_dir('Fox'):
            make('shared=1')

    def setup_environment(self, spack_env, run_env):
        spack_env.prepend_path('CPATH', join_path(self.spec['wx'].prefix.include, 'wx-3.1'))
        spack_env.prepend_path('CPATH', join_path(self.spec['wx'].prefix.lib.wx.include, 'gtk3-unicode-3.1'))

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


class PyPyqt(Package):
    """PyQt is a set of Python v2 and v3 bindings for Digia's Qt
       application framework and runs on all platforms supported by Qt
       including Windows, MacOS/X and Linux."""

    homepage = "http://www.riverbankcomputing.com/software/pyqt/intro"
    url      = "http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.3/PyQt-x11-gpl-4.11.3.tar.gz"

    version('4.11.3', '997c3e443165a89a559e0d96b061bf70')
    version('5.10.1', '9932e971e825ece4ea08f84ad95017837fa8f3f29c6b0496985fa1093661e9ef', 
            url = 'https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.10.1/PyQt5_gpl-5.10.1.tar.gz')
    version('5.10', '4874c5985246fdeb4c3c7843a3e6ef53', url = 'https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.10/PyQt5_gpl-5.10.tar.gz')

    extends('python')
    depends_on('python@3:')
    depends_on('py-sip@4.19.8', type=('build', 'run'))
    # TODO: allow qt5 when conditional deps are supported.
    # TODO: Fix version matching so that @4 works like @:4
    depends_on('qt@:4+phonon+dbus', when='@:4')
    depends_on('qt@:5+dbus+phonon', when='@5.10.1')

    def install(self, spec, prefix):
        python('configure.py',
               '--sip-incdir={0}'.format(join_path(self.spec['py-sip'].prefix.include, 'python3.6')),
               '--qmake={0}'.format(join_path(self.spec['qt'].prefix.bin, 'qmake')),
               '--qt={0}'.format(self.spec['qt'].prefix),
               '--confirm-license',
               '--destdir=%s' % site_packages_dir,
               '--allow-sip-warnings', '--verbose')
        make()
        make('install')

#    def setup_environment(self, spack_env, run_env):
#        spack_env.prepend_path('CPATH', join_path(self.spec[
#                               'py-sip'].prefix.include, 'python2.7'))

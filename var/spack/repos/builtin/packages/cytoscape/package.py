##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
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
import inspect


class Cytoscape(Package):
    """Cytoscape is an open source software platform for visualizing complex
       networks and integrating these with any type of attribute data."""

    homepage = "http://www.cytoscape.org/"
    url      = "https://github.com/cytoscape/cytoscape/archive/3.5.0.tar.gz"

    version('3.5.0', '4b368f91b4c8bbd62aa6d19a4572e528')

    depends_on('jdk', type=('build', 'run'))
    depends_on('maven', type='build')
    depends_on('git', type='build')

    phases = ['build', 'install']

    def build(self, spec, prefix):
        build = Executable('./cy.sh')
        build('init-all', prefix)

#    def install(self, spec, prefix):
#        with working_dir('cytoscape'):
#            mvn = which('mvn')
#            mvn('install')

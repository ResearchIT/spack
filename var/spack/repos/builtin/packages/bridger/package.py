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


class Bridger(AutotoolsPackage):
    """Bridger takes advantage of techniques employed in Cufflinks to overcome
       limitations of the existing de novo assemblers"""

    homepage = "https://genomebiology.biomedcentral.com/articles/10.1186/s13059-015-0596-2"
    url      = "https://downloads.sourceforge.net/project/rnaseqassembly/Bridger_r2014-12-01.tar.gz"

    version('2014-12-01', '4f4a8a00363df197463259a7eef906b2')

    depends_on('boost@1.47.0:')
    depends_on('perl', type=('build', 'run'))

    conflicts('boost@1.62.0')
    conflicts('%gcc@6:')

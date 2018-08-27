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
#     spack install py-pymysql
#
# You can edit this file again by typing:
#
#     spack edit py-pymysql
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyPymysql(PythonPackage):
    """Pure-Python MySQL client library"""

    homepage = "https://github.com/PyMySQL/PyMySQL/"
    url      = "https://files.pythonhosted.org/packages/d9/ab/bc9be64876fc9b1590d8ae62b471981b4489c23d6c3f0319af570748d408/PyMySQL-0.9.2.tar.gz"

    version('0.9.2', sha256='9ec760cbb251c158c19d6c88c17ca00a8632bac713890e465b2be01fdc30713f')

    depends_on('mysql@5.5:')
    depends_on('py-cython@2.7:,3.4:')

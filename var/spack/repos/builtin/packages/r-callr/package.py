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


class RCallr(RPackage):
    """It is sometimes useful to perform a computation in a separate R
       process, without affecting the current R process at all. This packages
       does exactly that."""

    homepage = "https://github.com/MangoTheCat/callr"
    url      = "https://cran.r-project.org/src/contrib/callr_3.0.0.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/callr/callr_2.0.4.tar.gz"

    version('3.0.0', sha256='e36361086c65660a6ecbbc09b5ecfcddee6b59caf75e983e48b21d3b8defabe7')
    version('2.0.4', sha256='0e3fa4e047f61f4e29ab2dee8f585861fb77a5f5ad6c81f125e98b6130c6a380')
    version('2.0.3', sha256='f1f7d511b215eb88d8680edef09d31eb93b3ef8beb124f8edf0c82601f7575cc')
    version('2.0.2', sha256='778595e3f0b08f4e33a3103bd8e84a183945074f9e7404cdee8d72b7d3b8a154')
    version('2.0.1', sha256='067bb1cda50a63df626a23128d1e32eb20a2ed3ea6cae0937bef97ce6dc6c3e6')
    version('2.0.0', sha256='b89482fa11c02058e636a19e9286a30f4e2c299a7b1aa52d87cd839520b2a4bb')
    version('1.0.0', sha256='2c56808c723aba2ea8a8b6bbdc9b8332c96f59b119079861dd52f5988c27f715')

    depends_on('r-base64enc', type=('build', 'run'))
    depends_on('r-processx', type=('build', 'run'))
    depends_on('r-r6', type=('build', 'run'))
    depends_on('r-utils', type=('build', 'run'))

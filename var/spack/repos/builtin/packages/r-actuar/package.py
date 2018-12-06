# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RActuar(RPackage):
    """actuar: Actuarial Functions and Heavy Tailed Distributions"""

    homepage = "https://cran.r-project.org/package=actuar"
    url      = "https://cran.r-project.org/src/contrib/actuar_2.3-1.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/actuar"

    version('2.3-1', sha256='730d1bf279db4d5d2e484f538c1f3c775535fb027be5c5c81544d5b7802f1c44')

    depends_on('r@3.3.0:', type=('build', 'run'))
    depends_on('r-expint', type=('build', 'run'))
    depends_on('r-mass', type=('build', 'run'))

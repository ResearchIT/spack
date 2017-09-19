##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
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
#
#
from spack import *


class RMpm(RPackage):
    """Exploratory graphical analysis of multivariate data, specifically 
    gene expression data with different projection methods: principal 
    component analysis, correspondence analysis, spectral map analysis."""

    homepage = "https://cran.rstudio.com/web/packages/mpm/index.html"
    url      = "https://cran.rstudio.com/src/contrib/mpm_1.0-22.tar.gz"
    list_url = homepage
    version('1.0-22', '91885c421cafd89ce8893ccf827165a2')

    depends_on('r-kernsmooth', type=('build', 'run'))


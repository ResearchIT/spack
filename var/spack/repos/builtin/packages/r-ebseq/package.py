# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class REbseq(RPackage):
    """An R package for gene and isoform differential expression analysis of
       RNA-seq data"""

    homepage = "https://www.bioconductor.org/packages/EBSeq/"
    url      = "https://www.bioconductor.org/packages/release/bioc/src/contrib/EBSeq_1.22.0.tar.gz"

    version('1.22.0', sha256='768f7bf9574101ec4f71e9fc31fd07e5cc6d460ea58a21fa8d0d8c0566cd0afd')

    depends_on('r@3.0.0:', type=('build', 'run'))
    depends_on('r-blockmodeling', type=('build', 'run'))
    depends_on('r-gplots', type=('build', 'run'))
    depends_on('r-testthat', type=('build', 'run'))

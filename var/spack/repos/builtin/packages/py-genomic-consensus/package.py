# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGenomicConsensus(PythonPackage):
    """The GenomicConsensus package provides the variantCaller tool, which
    allows you to apply the Quiver or Arrow algorithm to mapped PacBio
    reads to get consensus and variant calls."""

    homepage = "https://github.com/PacificBiosciences/GenomicConsensus"
    url      = "https://github.com/PacificBiosciences/GenomicConsensus/releases/download/2.3.3/GenomicConsensus-2.3.3.tar.gz"

    version('2.3.3', sha256='6623ada5adaeca8fbf31e6c2c7e483a2eabe717307f86a6b04cb1ac8fbeed9d4')
    version('2.3.2', sha256='de31420e2026b91b85d0a451afe924a0f20faeb3aad5517bdc9f40a9f4c6c80f')
    version('2.3.1', sha256='9f58825b4a799aa9da1294920cafe725b733376d17aecbb5f526c4b8d5663e42')
    version('2.3.0', sha256='a8c5c384dabdfed851e48d9b8deaa8580df27bb5746b62c5b86599aed9ce44ed')

    depends_on('py-setuptools',    type='build')
    depends_on('python@2.7:+ucs4', type=('build', 'run'))

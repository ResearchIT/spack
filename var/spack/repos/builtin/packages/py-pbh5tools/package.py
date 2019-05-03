# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPbh5tools(PythonPackage):
    """pbh5tools: tools for manipulating HDF5 files produced
    by Pacific Biosciences """

    homepage = "https://github.com/PacificBiosciences/pbh5tools/"
    url      = "https://github.com/PacificBiosciences/pbh5tools/archive/smrtanalysis-2.3.0p4.tar.gz"

    version('2.3.0p4', sha256='6fc54021bbdf4bab5dba6056e01e0a46f4a18f71f6eccd6f6e8fbae2477f8f4c')

    depends_on('py-setuptools',      type=('build'))
    depends_on('python@2.7: +ucs4',  type=('build', 'run'))

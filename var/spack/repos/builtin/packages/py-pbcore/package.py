# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPbcore(PythonPackage):
    """The pbcore package provides Python APIs for interacting with
    PacBio data files and writing bioinformatics applications."""

    homepage = "https://github.com/PacificBiosciences/pbcore"
    url      = "https://github.com/PacificBiosciences/pbcore/releases/download/1.7.1/pbcore-1.7.1.tar.gz"

    version('1.7.1', sha256='f3174b23de810aa9b10d7dd17f767aa9f91ddc34d789736b383e7369e32a5397')
    version('1.6.5', sha256='c99e4f1b5caf721e3379f8f45c44f22dd006be396e986f1fda7b67bc61f7c1cc')
    version('1.5.1', sha256='716a428088cf4215ff6f4e5ca05b499031cdd203cb22c712f3fd11ff3b31c170')

    depends_on('py-setuptools',      type='build')
    depends_on('python@2.7:+ucs4',   type=('build', 'run'))

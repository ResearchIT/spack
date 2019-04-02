# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Swift(Package):
    """Swift Parallel Scripting Language"""

    homepage = "http://swift-lang.org/"
    url      = "https://github.com/swift-lang/swift-k/archive/release-0.96.2p1.tar.gz"

    version('0.96.2p1', sha256='c5bdb645976c63b7813f28fff53eaecab3c1c07382e6d0d9b84649772fc3e548')

    depends_on('ant', type='build')
    depends_on('jdk@:1.8.0_202', type=('build', 'run'))

    def install(self, spec, prefix):
        ant = which('ant')
        ant('redist')
        install_tree('dist/swift-svn', prefix)

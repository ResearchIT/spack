# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Elfx86exts(Package):
    """Disassemble a binary containing x86 instructions and
       print out which extensions it uses. Despite the utterly
       misleading name, this tool supports ELF and MachO
       binaries, and perhaps PE-format ones as well."""

    homepage = "https://github.com/pkgw/elfx86exts"
    url      = "https://github.com/pkgw/elfx86exts/archive/v0.3.0.tar.gz"

    version('0.3.0', sha256='a1d9e7adda242dd52d2e3e6f72cf129254e9a2adc5534f7aa221a41f9e1571c0')

    depends_on('rust')
    depends_on('capstone')

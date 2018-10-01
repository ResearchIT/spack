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


class Newlib(AutotoolsPackage):
    """Newlib is a C library intended for use on embedded systems. It is a
       conglomeration of several library parts, all under free software
       licenses that make them easily usable on embedded products. """

    homepage = "https://sourceware.org/newlib/"
    url      = "ftp://sourceware.org/pub/newlib/newlib-3.0.0.20180831.tar.gz"

    version('3.0.0.20180831', sha256='3ad3664f227357df15ff34e954bfd9f501009a647667cd307bf0658aefd6eb5b')

    variant('nvptx',
            default=False,
            description='Configure for cross compiling to nvptx')

    depends_on('nvptx-tools')

    def configure_args(self):
        spec = self.spec

        args = [
            '--with-newlib',
        ]

        if '+nvptx' in spec:
            args.append('--target=nvptx-none')
            # I don't think host is required
            args.append('--host=x86_64-pc-linux-gnu')

            # these args required per:
            # https://sourceware.org/ml/newlib/2018/msg00315.html
            args.append('--enable-newlib-elix-level=1')
            args.append('--enable-newlib-global-stdio-streams')

        return args

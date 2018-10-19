# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install ds
#
# You can edit this file again by typing:
#
#     spack edit ds
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ds(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://ds9.si.edu/download/source/ds9.8.0rc6.tar.gz"

    version('9.8.0rc6', sha256='9c926dbe5475529b4de456058605e61e523f442993a3aa188f5d3fbd59a9af7a')
    version('9.8.0rc5', sha256='3ff95fa4550fbcdad0f2a064773ce232526bd24875b40f81e0b9e734aca516ad')
    version('9.7.6',    sha256='07c7396e220d9763d4a9edd18f5ba0edf8030a1bddbf1c65b33b962d37a97677')

    depends_on('tk')
    depends_on('libx11')
    depends_on('openssl')
    
    phases = ['configure', 'install']

    def configure(self, spec, prefix):
        configure = Executable(join_path(self.stage.source_path, 'unix/configure'))
        configure()

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    def install(self, spec, prefix):
        make()

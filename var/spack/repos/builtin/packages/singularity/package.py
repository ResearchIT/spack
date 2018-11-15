# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Singularity(AutotoolsPackage):
    """Singularity is a container platform focused on supporting 'Mobility of
       Compute'. Note: you will need to set FORCE_UNSAFE_CONFIGURE=1 to
       correctly generate the setuid binaries"""

    homepage = "https://www.sylabs.io/singularity/"
    url      = "https://github.com/singularityware/singularity/releases/download/2.5.2/singularity-2.5.2.tar.gz"
    git      = "https://github.com/singularityware/singularity.git"

    # Versions before 2.5.2 suffer from a serious security problem.
    # https://nvd.nist.gov/vuln/detail/CVE-2018-12021
    version('develop', branch='master')
    version('3.0.1', sha256='61baa5af4ab9c0beb6353e605bcffd568813e388fdd3775cb60e50ee33da1d3a',
            url='https://github.com/sylabs/singularity/archive/v3.0.1.tar.gz')
    version('2.6.0', sha256='7c425211a099f6fa6f74037e6e17be58fb5923b0bd11aea745e48ef83c488b49')
    version('2.5.2', '2edc1a8ac9a4d7d26fba6244f1c5fd95')

    force_autoreconf = True

    depends_on('libarchive', when='@2.5.2:')
    # these are only needed if we're grabbing the unreleased tree
    depends_on('m4',       type='build')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')

    # When installing as root, the copy has to run before chmod runs
    def install(self, spec, prefix):
        make('install', parallel=False)

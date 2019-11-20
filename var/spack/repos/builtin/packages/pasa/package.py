# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pasa(MakefilePackage):
    """Gene Structure Annotation and Analysis Using PASA"""

    homepage = "https://github.com/PASApipeline/PASApipeline"
    url      = "https://github.com/PASApipeline/PASApipeline/releases/download/pasa-v2.4.1/PASApipeline.v2.4.1.FULL.tar.gz"

    version('2.4.1.FULL', sha256='aa6a71e104b30fa8ef96217452f8d34fbb4713103318bd62369fcf26e08c4970')

    depends_on('perl', type='run')
    depends_on('perl-db-file', type='run')
    depends_on('perl-dbd-mysql', type='run')
    depends_on('perl-dbd-sqlite', type='run')
    depends_on('gmap-gsnap', type='run')
    depends_on('blat', type='run')
    depends_on('fasta', type='run')

    def setup_environment(self, spack_env, run_env):
        run_env.set('PASAHOME', self.prefix)

    def install(self, spec, prefix):
        install_tree('.', prefix)

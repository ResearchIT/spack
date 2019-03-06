# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Repet(Package):
    """The REPET package integrates bioinformatics programs in order to tackle
       biological issues at the genomic scale."""

    homepage = "https://urgi.versailles.inra.fr/Tools/REPET/"
    url      = "https://urgi.versailles.inra.fr/download/repet/REPET_linux-x64-2.5.tar.gz"

    version('2.5', sha256='383451fb00152b79c10d97e3e02c789adf2ff349ac7c3656e035b8a595964080')

    depends_on('python@2.6:3.0', type='run')
    depends_on('blast-plus', type='run')

    def setup_environment(self, spack_env, run_env):
        # repet requires several environment variables to be set by the user
        # we handle python/prefix paths etc but the user must still set the
        # following variables on their own:
        #
        #   REPET_HOST: database host
        #   REPET_USER: db user
        #   REPET_PW:  db pw
        #   REPET_DB: db name
        #   REPET_PORT: db port
        #   REPET_JOB_MANAGER: cluster manager
        #   REPET_QUEUE: cluster queue

        run_env.set('REPET_PATH', self.prefix)
        run_env.set('REPET_JOBS', 'MySQL')
        run_env.prepend_path('PYTHONPATH', self.prefix)

    def install(self, spec, prefix):
        install_tree('.', prefix)

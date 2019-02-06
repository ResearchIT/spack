# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import glob


class Braker(Package):
    """BRAKER is a pipeline for unsupervised RNA-Seq-based genome annotation
       that combines the advantages of GeneMark-ET and AUGUSTUS"""

    homepage = "http://exon.gatech.edu/braker1.html"
    url      = "https://github.com/Gaius-Augustus/BRAKER/archive/v2.1.2.tar.gz"
    # Releases have moved to github

    version('develop', git='https://github.com/Gaius-Augustus/BRAKER.git', tag='master')
    version('2.1.2', sha256='9f178c5fe64ae358dcba9936802d24e330312e698a3f7930d1f91e58974129d3')
    version('2.1.1', sha256='10674382431975928217875df7c6953f841c69934057137c0d177c9dbfad18af',
            url='https://github.com/Gaius-Augustus/BRAKER/archive/v2.1.1-tag1.tar.gz')
    version('2.1.0', '5f974abcceb9f96a11668fa20a6f6a56',
            url='http://bioinf.uni-greifswald.de/augustus/binaries/old/BRAKER_v2.1.0.tar.gz')
    version('1.11', '297efe4cabdd239b710ac2c45d81f6a5',
            url='http://bioinf.uni-greifswald.de/augustus/binaries/old/BRAKER1_v1.11.tar.gz')

    depends_on('perl', type=('build', 'run'))
    depends_on('perl-scalar-util-numeric', type=('build', 'run'))
    depends_on('perl-parallel-forkmanager', type=('build', 'run'))
    depends_on('perl-file-which', type=('build', 'run'))
    depends_on('augustus@3.2.3:')
    depends_on('genemark-et')
    depends_on('bamtools')
    depends_on('samtools')
    depends_on('perl-yaml-libyaml', type=('build', 'run'), when='@2.1.1:')
    depends_on('perl-hash-merge', type=('build', 'run'), when='@2.1.1:')
    depends_on('ncbi-rmblastn', type='run', when='@2.1.1:')
    depends_on('perl-logger-simple', type=('build', 'run'), when='@2.1.1:')
    depends_on('perl-yaml', type=('build', 'run'), when='@2.1.1:')
    depends_on('py-biopython', type=('build', 'run'), when='@2.1.1:')
    depends_on('perl-file-homedir', type=('build', 'run'), when='@develop')

    @when('@:2.1.0')
    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.lib)
        install('braker.pl', prefix.bin)
        install('filterGenemark.pl', prefix.bin)
        install('filterIntronsFindStrand.pl', prefix.bin)
        install('helpMod.pm', prefix.lib)

    @when('@2.1.1:')
    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.lib)
        mkdirp(prefix.cfg)

        with working_dir('scripts'):
            bin_files = glob.iglob("*.pl")
            for bin_file in bin_files:
                install(bin_file, prefix.bin)

            lib_files = glob.iglob("*.pm")
            for lib_file in lib_files:
                install(lib_file, prefix.lib)

            install_tree('cfg', prefix.cfg)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PERL5LIB', prefix.lib)

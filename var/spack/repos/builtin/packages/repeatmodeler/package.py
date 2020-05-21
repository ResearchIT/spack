# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Repeatmodeler(Package):
    """RepeatModeler is a de-novo repeat family identification and modeling
       package."""

    homepage = "http://www.repeatmasker.org/RepeatModeler/"
    url      = "http://www.repeatmasker.org/RepeatModeler/RepeatModeler-open-1.0.11.tar.gz"

    version('2.0.1', sha256='628e7e1556865a86ed9d6a644c0c5487454c99fbcac21b68eae302fae7abb7ac',
            url='http://www.repeatmasker.org/RepeatModeler/RepeatModeler-2.0.1.tar.gz')
    version('1.0.11', sha256='7ff0d588b40f9ad5ce78876f3ab8d2332a20f5128f6357413f741bb7fa172193')

    depends_on('perl', type=('build', 'run'))
    depends_on('perl-json', type=('build', 'run'))
    depends_on('perl-uri', type=('build', 'run'))
    depends_on('perl-libwww-perl', type=('build', 'run'))

    depends_on('perl-file-which', type=('build', 'run'), when='@2.0.1:')

    depends_on('repeatmasker', type='run')
    depends_on('recon+repeatmasker', type='run')
    depends_on('repeatscout', type='run')
    depends_on('trf', type='run')
    depends_on('nseg', type='run')
    depends_on('ncbi-rmblastn', type='run')

    depends_on('ninja', type='run', when='@2.0.1:')
    depends_on('mafft', type='run', when='@2.0.1:')
    depends_on('cdhit', type='run', when='@2.0.1:')
    depends_on('genometools', type='run', when='@2.0.1:')
    depends_on('ltr-retriever', type='run', when='@2.0.1:')

    def install(self, spec, prefix):
        perl = which('perl')

        if spec.satisfies('@2.0.1:'):
            # newer repeatmodeler, configure is semi-interactive

            config_answers = [
                '', '', '', '', 'y',
            ]

            config_filename = 'spack-config.in'

            with open(config_filename, 'w') as f:
                f.write('\n'.join(config_answers))

            with open(config_filename, 'r') as f:
                perl('configure',
                     '-rscout_dir', spec['repeatscout'].prefix.bin,
                     '-genometools_dir', spec['genometools'].prefix.bin,
                     '-recon_dir', spec['recon'].prefix.bin,
                     '-cdhit_dir', spec['cdhit'].prefix.bin,
                     '-trf_prgm', spec['trf'].prefix.bin.trf,
                     '-rmblast_dir', spec['ncbi-rmblastn'].prefix.bin,
                     '-mafft_dir', spec['mafft'].prefix.bin,
                     '-ninja_dir', spec['ninja'].prefix.bin,
                     '-ltr_retriever_dir', spec['ltr-retriever'].prefix.bin,
                     input=f)
        else:
            # older repeatmodeler, interactive configure only
            # questions:
            #   1. <enter to continue>
            #   2. <perl path, default is OK>
            #   3. <source path, default is OK>
            #   4. RepeatMasker bin path
            #   5. RECON bin path
            #   6. RepeatScout bin path
            #   7. Nseg bin path
            #   8. trf bin path
            #   9. Add a search engine:
            #        1. RMBlast -> Path, Default? (Y/N)
            #        2. WUBlast/ABBlast -> Path, Default? (Y/N)
            #        3. Done

            config_answers = [
                '', '', '',
                spec['repeatmasker'].prefix.bin,
                spec['recon'].prefix.bin,
                spec['repeatscout'].prefix.bin,
                spec['nseg'].prefix.bin,
                spec['trf'].prefix.bin,
                '1', spec['ncbi-rmblastn'].prefix.bin, 'Y',
                '3',
            ]

            config_filename = 'spack-config.in'

            with open(config_filename, 'w') as f:
                f.write('\n'.join(config_answers))

            with open(config_filename, 'r') as f:
                perl('configure', input=f)

        # configure done, finally install
        install_tree('.', prefix.bin)

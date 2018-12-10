# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RepeatmaskerRecon(MakefilePackage):
    """RECON: a package for automated de novo identification of repeat
       families from genomic sequences

       RepeatMasker fork, original at http://eddylab.org/software/recon/"""

    homepage = "http://www.repeatmasker.org/"
    url      = "http://www.repeatmasker.org/RepeatModeler/RECON-1.08.tar.gz"

    version('1.08', sha256='699765fa49d18dbfac9f7a82ecd054464b468cb7521abe9c2bd8caccf08ee7d8')

    depends_on('perl', type='run')

    def build(self, spec, prefix):
        with working_dir('src'):
            make()
            make('install')

    def install(self, spec, prefix):
        filter_file('$path = ""', '$path = "{0}"'.format(prefix.bin),
                    'scripts/recon.pl', string=True)

        install_tree('bin', prefix.bin)
        install_tree('scripts', prefix.bin)

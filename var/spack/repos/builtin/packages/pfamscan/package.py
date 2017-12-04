##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
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


class Pfamscan(Package):
    """PfamScan is used to search a FASTA sequence against a library of Pfam
       HMM"""

    homepage = "http://www.ebi.ac.uk/Tools/pfa/pfamscan/"
    url      = "http://ftp.ebi.ac.uk/pub/databases/Pfam/Tools/OldPfamScan/PfamScan1.5/PfamScan.tar.gz"

    version('1.5', '42b2d4dead971f030d5e4bf12105a8bd')

    depends_on('perl', type=('build', 'run'))
    depends_on('perl-bio-perl', type=('build', 'run'))
    depends_on('perl-moose', type=('build', 'run'))
    depends_on('hmmer')

    resource(
        name='Pfam-A.hmm',
        url='ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz',
        sha256='33f2dfab4d695fc3d2337119debbfcd8c801aaf8e2c312bd738c105a84007973',
    )

    resource(
        name='Pfam-A.hmm.dat',
        url='ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.dat.gz',
        sha256='512b96c6e3c95cdd78776d8524be888f44199533361348e11330e4718c9e500b',
    )

    resource(
        name='active_site.dat',
        url='ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/active_site.dat.gz',
        sha256='fe6ebb90a0c3f5fb6e92b566d2e3e2f59f5eba5aaf96d4e4db8047e54f4da1b2',
    )

    def url_for_version(self, version):
        url = 'http://ftp.ebi.ac.uk/pub/databases/Pfam/Tools/OldPfamScan/PfamScan{0}/PfamScan.tar.gz'
        return url.format(version)

    @run_before('install')
    def pre_install(self, spec, prefix):
        with working_dir('data'):
            hmmpress = which('hmmpress')
            hmmpress('Pfam-A.hmm')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree(self.stage.source_path, prefix.bin)

    def setup_environment(self, spack_env, run_env):
        run_env.set('PFAM_DIR_PATH', prefix.data)
        run_env.prepend_path('PERL5LIB', prefix.bin)

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
#     spack install bambam
#
# You can edit this file again by typing:
#
#     spack edit bambam
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Bambam(MakefilePackage):
    """Bambam is a tool used to facilitate NGS analysis."""

    homepage = "http://udall-lab.byu.edu/Research/Software/BamBam"
    url      = "https://downloads.sourceforge.net/project/bambam/bambam-1.4.tgz"

    version('1.4', '4a8a70bd26a68170a97e32bbca15a89f')

    depends_on('perl', type=('build', 'run'))
    depends_on('samtools')
    depends_on('bamtools')
    depends_on('htslib')
    depends_on('zlib')

    def edit(self, spec, prefix):
        makefile = FileFilter('makefile')
        makefile.filter('INC = *', 'INC = -I%s ' %
                        self.spec['bamtools'].prefix.include)

    def install(self, spec, prefix):
        install_tree('bin', prefix.bin)
        install_tree('lib', prefix.lib)
        install_tree('scripts', prefix.scripts)

    def setup_environment(self, spack_env, run_env):
        spack_env.prepend_path('LIBRARY_PATH',
                               self.spec['samtools'].prefix.lib)
        spack_env.prepend_path('LIBRARY_PATH',
                               self.spec['bamtools'].prefix.lib.bamtools)
        run_env.prepend_path('PATH', prefix.scripts)

# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mothur(MakefilePackage):
    """This project seeks to develop a single piece of open-source, expandable
       software to fill the bioinformatics needs of the microbial ecology
       community."""

    homepage = "https://github.com/mothur/mothur"
    url      = "https://github.com/mothur/mothur/archive/v1.39.5.tar.gz"

    version('1.43.0', sha256='12ccd95a85bec3bb1564b8feabd244ea85413973740754803d01fc71ecb0a2c1')
    version('1.42.1', sha256='6b61591dda289ac2d8361f9c1547ffbeeba3b9fbdff877dd286bad850bbd5539')
    version('1.40.5', 'd57847849fdb961c3f66c9b9fdf3057b')
    version('1.39.5', '1f826ea4420e6822fc0db002c5940b92')

    variant('vsearch', default=False,  description='Use vsearch')

    depends_on('boost')
    depends_on('readline')
    depends_on('vsearch',  when='+vsearch', type='run')

    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        makefile.filter('BOOST_LIBRARY_DIR=\"\\\"Enter_your_boost_library_path'
                        '_here\\\"\"', 'BOOST_LIBRARY_DIR=%s' %
                        self.spec['boost'].prefix.lib)
        makefile.filter('BOOST_INCLUDE_DIR=\"\\\"Enter_your_boost_include_path'
                        '_here\\\"\"', 'BOOST_INCLUDE_DIR=%s' %
                        self.spec['boost'].prefix.include)
        makefile.filter('MOTHUR_FILES=\"\\\"Enter_your_default_path_'
                        'here\\\"\"', 'MOTHUR_FILES=%s' % prefix)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('mothur', prefix.bin)
        install('uchime', prefix.bin)
        install_tree('source', prefix.include)

# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Dock(Package):
    homepage = "http://dock.compbio.ucsf.edu/DOCK_6/index.htm"
    url      = "file://{0}/dock.6.9_source.tar.gz".format(os.getcwd())

    version('6.9', sha256='c2caef9b4bb47bb0cb437f6dc21f4c605fd3d0d9cc817fa13748c050dc87a5a8')

    variant('mpi', default=True, description='Enable mpi')

    depends_on('bison', type='build')
    depends_on('mpi', when='+mpi')

    def setup_build_environment(self, env):
        if '+mpi' in self.spec:
            env.set('MPICH_HOME', self.spec['mpi'].prefix)

    def install(self, spec, prefix):
        compiler_targets = {
            'gcc': 'gnu',
            'intel': 'intel',
            'pgi': 'pgi',
            'sgi': 'sgi',
        }

        if not self.compiler.name in compiler_targets:
            template = 'Unsupported compiler {0}! Supported compilers: {1}'
            err = template.format(self.compiler.name,
                                  ', '.join(list(compiler_targets.keys())))

            raise InstallError(err)

        if self.compiler.name == 'pgi' and '+mpi' in spec:
            raise InstallError('Parallel output is not supported with pgi.')

        with working_dir('install'):
            if '+mpi' in spec:
                which('sh')('./configure', compiler_targets[self.compiler.name], 'parallel')
            else:
                which('sh')('./configure', compiler_targets[self.compiler.name])

            which('make')('YACC=bison -o y.tab.c')

        mkdirp(prefix.bin)
        install_tree('bin', prefix.bin)

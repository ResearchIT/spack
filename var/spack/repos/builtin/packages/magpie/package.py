##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
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
import glob
import os


class Magpie(Package):
    """Magpie contains a number of scripts for running Big Data software in
       HPC environments. Thus far, Hadoop, Spark, Hbase, Storm, Pig, Mahout,
       Phoenix, Kafka, Zeppelin, and Zookeeper are supported. It currently
       supports running over the parallel file system Lustre and running over
       any generic network filesytem. There is scheduler/resource manager
       support for Slurm, Moab, Torque, and LSF."""

    homepage = "https://github.com/LLNL/magpie"
    url      = "https://github.com/LLNL/magpie/archive/1.85.tar.gz"

    version('1.85', sha256='e04db023b8436ba02121274e6bd397c03943fe4188d34869d65bae888e719f00')
    version('1.84', sha256='587d2fb5b21696c3d6aa90149d3249311099b2b5eac1cdc26b747cd94dbe9b67')
    version('1.83', sha256='80ca5d00313fb42709007daead886b315e13efac5bfc433bfffecc0649a32bc9')

    def setup_environment(self, spack_env, run_env):
        run_env.set('MAGPIE_SCRIPTS_HOME',
                    join_path(self.spec.prefix.lib, 'magpie'))

    def install(self, spec, prefix):
        # install everything to a lib directory, magpie depends
        # on pretty much everything during runtime
        mkdirp(prefix.lib)
        mkdirp(prefix.bin)

        iroot = join_path(prefix.lib, 'magpie')
        install_tree('.', iroot)

        # link the important scripts in /bin
        with working_dir(iroot):
            bins = glob.glob('magpie-*')
            for f in bins:
                os.symlink(join_path(iroot, f), join_path(prefix.bin, f))

# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gapc(Package):
    """The Bellman's GAP Compiler (GAP-C) is the novel ADP
       compiler which translates GAP-L programs into efficient
       C++ code. It implements several semantic analyses for
       optimization purposes, error reporting, type checking
       and automatic table design."""

    homepage = "https://bibiserv.cebitec.uni-bielefeld.de/gapc?id=gapc_compiler"
    hg = "ssh://hganon@hg.cebitec.uni-bielefeld.de:/pi/software/gapc"

    version('develop')

    depends_on('flex')
    depends_on('bison')

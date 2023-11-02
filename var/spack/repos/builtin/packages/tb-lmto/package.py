# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class TbLmto(MakefilePackage):
    """
    The STUTTGART TB-LMTO program. The linear muffin-tin orbital (LMTO) method has been described in numerous publications.
    Use of this software is subject to the license at
    https://www2.fkf.mpg.de/andersen/LMTODOC/node180.html#SECTION000130000000000000000
    """

    homepage = "https://www2.fkf.mpg.de/andersen/LMTODOC/LMTODOC.html"
    manual_download = True

    maintainers("snehring")

    version("47u.1d", sha256="bbcc1c57005f33749f8ee6d33be3490071704bce11214544cc4f9c13c28a126e")
    version("47c2.1d", sha256="c80ef9b4aa725ad75ae07b0215671b3674a8f5dced9e87202dd0d486ffe1cb10")
    version("47.1d", sha256="5b24f2917cef85fe49d3a4ff6403294a44a9cf7c003234a0fd96d626c316bda0")

    depends_on("gnuplot", type="run")

    parallel = False

    def url_for_version(self, version):
        return "file://{0}/lmto{1}.tar.gz".format(os.getcwd(), version)

    def flag_handler(self, name, flags):
        if name.lower() == "fflags":
            flags.append("-fallow-argument-mismatch")
        return (flags, None, None)

    def edit(self, spec, prefix):
        makefile = FileFilter("makefile")

        makefile.filter("LMPATH = .*", "LMPATH = ./")
        makefile.filter("FFLAGS =.*", "")
        makefile.filter("CCFLAGS =.*", "")
        makefile.filter("CC=.*", "")
        makefile.filter("FC=.*", "")

    def install(self, spec, prefix):
        mkdirp(prefix)
        install_tree(".", prefix)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix)

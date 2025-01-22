# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Gamess(MakefilePackage, CudaPackage):
    """The General Atomic and Molecular Electronic Structure System (GAMESS)
    is a general ab initio quantum chemistry package.
    """

    homepage = "https://www.msg.chem.iastate.edu/GAMESS/"
    url = "file://{0}/gamess-current.tar.gz".format(os.getcwd())

    manual_download = True
    maintainers = ["snehring"]

    version(
        "20220731R1", sha256="d54b6150d46057bb2334b07d49230c11e82209fcc56d0331e99b4155506797d8"
    )
    version(
        "20210930R2", sha256="9afe67a8ffad93d03b19caa9e5af8240c2c8c20031e2a72e0e0d9ad7da3bec03"
    )

    @property
    def download_instr(self):
        instr = (
            "Follow the directions at "
            "https://www.msg.chem.iastate.edu/GAMESS/"
            "License_Agreement.html "
            "to obtain a copy of GAMESS."
        )
        return instr

    variant(
        "cuda_arch",
        description="CUDA architecture",
        when="+cuda",
        values=("none",) + CudaPackage.cuda_arch_values,
        multi=False,
        sticky=True,
        default="none",
    )
    variant("libcchem", default=False, description="Build with libcchem.")
    variant("libxc", default=False, description="Build with libxc support.")
    variant("mpi", default=True, description="Build with mpi support.")
    variant("msucc", default=False, description="Build Michigan State University code.")
    variant("neo", default=False, description="Build NEO plugin.")
    variant("openmp", default=False, when="+mpi", description="Use OpenMP for threading.")
    variant("tests", default=False, description="Copy tests to install location.")
    variant("vb2000", default=False, description="Build VB200 plugin.")

    # build deps
    # needed for the configure script
    depends_on("python@3:", type="build")
    depends_on("py-jinja2", type="build")
    # needed for makefile
    depends_on("tcsh", type=("build", "run"))
    # needed to build libcchem and dep
    depends_on("cmake@3.12:", type="build", when="+libcchem")

    # mandatory deps
    depends_on("blas")
    depends_on("lapack", when="@20220731R1:")
    depends_on("openblas+ilp64", when="^[virtuals=blas,lapack] openblas")
    depends_on("flexiblas+ilp64", when="^[virtuals=blas,lapack] flexiblas")
    depends_on("intel-mkl+ilp64", when="^[virtuals=blas,lapack] intel-mkl")
    depends_on("intel-oneapi-mkl+ilp64", when="^[virtuals=blas,lapack] intel-oneapi-mkl")
    depends_on("netlib-lapack+ilp64", when="^[virtuals=blas,lapack] netlib-lapack")

    # conditional deps
    depends_on("boost+thread+system", when="+libcchem")
    depends_on("cuda", when="+cuda+libcchem")
    depends_on("eigen", when="+libcchem")
    depends_on("globalarrays armci=mpi-pr", when="+libcchem")
    depends_on("hdf5", when="+libcchem")
    depends_on("libxc", when="+libxc")
    depends_on("mpi", when="+mpi")
    depends_on("openmpi+cxx", when="^[virtuals=mpi] openmpi")
    depends_on("mpi", when="+libcchem")

    # conflicts
    conflicts("~mpi", when="+libcchem", msg="libcchem requires mpi")
    conflicts("+openmp", when="libcchem", msg="OpenMP cannot be used with libcchem.")
    conflicts("cuda_arch=none", when="+cuda", msg="CUDA arch is required")
    conflicts("+cuda", when="~libcchem", msg="CUDA support requires libcchem")
    unsupported_cuda_archs = [
        "10",
        "11",
        "12",
        "13",
        "21",
        "30",
        "32",
        "37",
        "50",
        "52",
        "53",
        "61",
        "62",
        "72",
        "75",
        "86",
    ]
    for a in unsupported_cuda_archs:
        conflicts("cuda_arch=" + a, when="+cuda", msg="CUDA arch " + a + " is not supported")

    def patch(self):
        # lots of hard coded /bin/csh
        dirs = [
            ".",
            "misc",
            "libcchem/tools",
            "machines/unix",
            "ddi",
            "vb2000",
            "vb2000/TOOLS",
            "vb2000/checktst",
            "tools",
            "tools/crepes",
            "tools/efp",
            "tools/elg/checkelg",
        ]
        for d in dirs:
            for f in next(os.walk(d))[2]:
                self._filter_tcsh_shbang(join_path(d, f))
        csh = join_path(self.spec["tcsh"].prefix.bin, "csh")
        filter_file("/bin/csh", csh, "Makefile.in")
        if "+libxc" in self.spec:
            filter_file(
                "LIBXC_INSTALL=.*$", "LIBXC_INSTALL=" + self.spec["libxc"].prefix, "Makefile.in"
            )
            filter_file(r"\./libxc_lib", self.spec["libxc"].prefix, "Makefile.in")
            filter_file(r"\$GMS_PATH/libxc_lib", self.spec["libxc"].prefix, "lked")

    def edit(self, spec, prefix):
        fortran = self.compiler.fc_names[0]
        blas = self._get_blas_name()

        args = [
            "--mathlib_path=" + spec["blas"].prefix.lib,
            "--math=" + blas,
            "--fortran_version=" + str(spec.compiler.version.up_to(2)),
            "--fortran=" + fortran,
            "--build_path=" + prefix,
            "--fpe",
            "--rungms",
            "--scratch=`pwd`/gamess-run",
            "--restart=`pwd`/gamess-run",
        ]

        if "+libcchem" in spec:
            libcchem_args = [
                "--libcchem",
                "--hdf5_path=" + spec["hdf5"].prefix,
                "--eigen_path=" + spec["eigen"].prefix.include.eigen3,
                "--boost_path=" + spec["boost"].prefix,
                "--ga_path=" + spec["globalarrays"].prefix,
            ]
            libcchem_link_args = "-lga"
            if "+cuda" in spec:
                cuda_args = [
                    "--libcchem_gpu_support",
                    "--cuda_path=" + spec["cuda"].prefix,
                    "--" + self._get_arch_gen(),
                ]
                libcchem_args.extend(cuda_args)
            if "+libxc" in spec:
                libcchem_link_args += " -lxc"

            libcchem_args.append("--libcchem_libs=" + libcchem_link_args)
            args.extend(libcchem_args)

        if "+mpi" in spec:
            name = spec["mpi"].name
            if name == "intel-mpi" or name == "intel-oneapi-mpi":
                name = "impi"
            elif name == "spectrum-mpi":
                name = "spectrum"
            mpi_args = ["--mpi", "--mpi_path=" + spec["mpi"].prefix, "--mpi_lib=" + name]
            args.extend(mpi_args)
        # else:
        #    args.append("--sockets")

        if "+libxc" in spec:
            args.append("--libxc")

        if "+msucc" in spec:
            args.append("--msucc")

        if "+openmp" in spec:
            args.append("--openmp")

        # run the install.info generator
        python = Executable("python")
        python.add_default_arg("bin/create-install-info.py")
        for arg in args:
            python.add_default_arg(arg)
        python()

    def flag_handler(self, name, flags):
        if name.lower() == "fflags":
            flags.append("-std=legacy")
        if (
            "%gcc@11:" in self.spec
            and "os=rhel7" in self.spec
            and (name.lower() == "cflags" or name.lower() == "fflags")
        ):
            flags.append("-gdwarf-4")
        return (flags, None, None)

    def build(self, spec, prefix):
        # build process puts some things in final location
        mkdirp(prefix.ddi)
        make("-j1", "ddi")
        make("-j1", "modules")
        if "+libcchem" in spec:
            self._build_rysq_lib()
            self._build_libcchem()
        make()

    def install(self, spec, prefix):
        self._filter_tcsh_shbang("rungms")
        self._filter_tcsh_shbang("runall")
        self._filter_tcsh_shbang("gms-files.csh")
        install_tree("tools", prefix.tools)
        install_tree("auxdata", prefix.auxdata)
        install("rungms", prefix)
        filter_file(r"^setenv GMS_PATH.*$", "setenv GMS_PATH " + prefix, "install.info")
        install("install.info", prefix)
        install("gms-files.csh", prefix)
        if "+tests" in spec:
            install_tree("tests", prefix.tests)
        if "+vb2000" in spec:
            install_tree("vb2000", prefix.vb2000)

    def setup_run_environment(self, env):
        env.set("GMSPATH", self.prefix)
        env.append_path("PATH", self.prefix)
        env.append_path("PATH", self.prefix.tools)

    def _get_arch_gen(self):
        arch = self.spec.variants["cuda_arch"].value
        if arch == "20":
            return "fermi"
        if arch == "35":
            return "kepler"
        if arch == "60":
            return "pascal"
        if arch == "70":
            return "volta"
        if arch == "80":
            return "ampere"
        # we shouldn't ever get here if everything else is working
        return "NOTSUPPORTED"

    def _get_blas_name(self):
        blas = self.spec["blas"].name
        if blas == "intel-mkl" or blas == "intel-oneapi-mkl" or blas == "intel-parallel-studio":
            blas = "mkl"
        elif blas == "nvhpc":
            blas = "nvblas"
        elif blas == "netlib-lapack" or blas == "netlib-xblas":
            blas = "netlib"
        return blas

    def _build_libcchem(self):
        args = [
            "-DBOOST_ROOT=" + self.spec["boost"].prefix,
            "-DEIGEN_ROOT=" + self.spec["eigen"].prefix.include.eigen3,
            "-DGA_ROOT=" + self.spec["globalarrays"].prefix,
            "-DHDF5_ROOT=" + self.spec["hdf5"].prefix,
            "-DMATHLIB=" + self._get_blas_name(),
            "-DMATHLIB_ROOT=" + self.spec["blas"].prefix,
            "-DMPI_ROOT=" + self.spec["mpi"].prefix,
            "-DBUILD_HF=1",
            "-DBUILD_MP2=1",
            "-DBUILD_RI=1",
            "-DBUILD_CC=1",
        ]
        if "+cuda" in self.spec:
            cuda_arch = self._get_arch_gen().upper()
            args.extend(["-DBUILD_AHFOCK=1", "-DGPU_BOARD=" + cuda_arch])

        with working_dir("libcchem_build", create=True):
            cmake(*args, join_path(self.stage.source_path, "libcchem"))
            make()
            make("install")

    def _build_rysq_lib(self):
        args = ["-DBOOST_ROOT=" + self.spec["boost"].prefix, "-DBUILD_HF=1", "-DBUILD_RI=1"]
        if "+cuda" in self.spec:
            cuda_arch = self.spec.variants["cuda_arch"].value
            if cuda_arch == 80:
                # this sub library doesn't support ampere yet
                cuda_arch = 70
            args.append("-DGPU_BOARD=" + self._get_arch_gen().upper())
        with working_dir("rysq_build", create=True):
            cmake(*args, join_path(self.stage.source_path, "libcchem", "rysq"))
            make()
            make("install")

    def _filter_tcsh_shbang(self, file):
        csh = join_path(self.spec["tcsh"].prefix.bin, "csh")
        tcsh = join_path(self.spec["tcsh"].prefix.bin, "tcsh")
        filter_file("^#!/bin/csh", "#!{0}".format(csh), file)
        filter_file("^#!/bin/tcsh", "#!{0}".format(tcsh), file)

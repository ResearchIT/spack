# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cryodrgn(PythonPackage):
    """CryoDRGN: Reconstruction of heterogeneous cryo-EM structures using neural networks."""

    homepage = "https://cryodrgn.cs.princeton.edu/"

    pypi = "cryodrgn/cryodrgn-3.0.0b0.tar.gz"

    maintainers("snehring")

    version("3.0.0b0", sha256="c2f49a1947fdb693303551840ce4f5354af436a58c0ecf62ab39e0ab632a1033")

    depends_on("python@3:", type=("build", "run"))

    depends_on("py-setuptools@61:", type="build")
    depends_on("py-setuptools-scm@6.2:", type="build")

    depends_on("py-torch@1:", type=("build", "run"))
    depends_on("py-pandas@2:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-scipy@1.3.1:", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-seaborn@:0.12", type=("build", "run"))
    depends_on("py-cufflinks", type=("build", "run"))
    depends_on("py-jupyterlab", type=("build", "run"))
    depends_on("py-umap-learn", type=("build", "run"))
    depends_on("py-ipywidgets@:8", type=("build", "run"))
    depends_on("py-healpy", type=("build", "run"))

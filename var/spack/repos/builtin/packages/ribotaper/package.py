# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ribotaper(Package):
    """RiboTaper is a new analysis pipeline for Ribosome Profiling (Ribo-seq)
       experiments, which exploits the triplet periodicity of ribosomal
       footprints to call translated regions."""

    homepage = "https://ohlerlab.mdc-berlin.de/software/RiboTaper_126/"
    url      = "https://ohlerlab.mdc-berlin.de/files/RiboTaper/RiboTaper_v1.3.tar.gz"

    version('1.3', sha256='54a09552bb79d14ca8005aa198ccba03b46443ecf12202bc15f732905e84c95c')

    depends_on('bedtools2@2.17.0:', type='run')
    depends_on('r@3.0.1:', type='run')
    depends_on('r-seqinr@3.1-3:', type='run')
    depends_on('r-ade4@1.7-2:', type='run')
    depends_on('r-multitaper@1.0-11:', type='run')
    depends_on('r-domc@1.3.3:', type='run')
    depends_on('r-iterators@1.0.7:', type='run')
    depends_on('r-foreach@1.4.2', type='run')
    depends_on('r-xnomial@1.0.1:', type='run')
    depends_on('samtools@0.1.19:', type='run')

    def install(self, spec, prefix):
        install_tree('scripts', prefix.bin)

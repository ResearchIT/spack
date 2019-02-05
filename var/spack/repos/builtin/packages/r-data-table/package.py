# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RDataTable(RPackage):
    """Fast aggregation of large data (e.g. 100GB in RAM), fast ordered joins,
    fast add/modify/delete of columns by group using no copies at all, list
    columns and a fast file reader (fread). Offers a natural and flexible
    syntax, for faster development."""

    homepage = "https://github.com/Rdatatable/data.table/wiki"
    url      = "https://cran.r-project.org/src/contrib/data.table_1.10.0.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/data.table"

    version('1.11.8',   sha256='dc427465599cadd848b28a78e2fce3362867847b44148252054385999fe566d9')
    version('1.11.6',   sha256='ac6783c18e94d1bc05702ddec9fd87c542c744f640132f5ffc373348be84d9e9')
    version('1.11.4',   sha256='fdccf1dec3f38bb344163163decf3ffa0c0f8e2c70daa1bec8aac422716e81d5')
    version('1.11.2',   sha256='44f548517426c0444f7ce993bf93350be9f31e214d3dad39f9a680a53f9e6e64')
    version('1.11.0',   sha256='ae81e07a39ef0cb65751c8987df21246d57ebc5e4ef7e9c511225a9d58193758')
    version('1.10.4-3', sha256='ba8b4f1b96b16e7f9765fc49c5028f21ef2210fc46cf962f4f7ea7901f9d8a89')
    version('1.10.4-2', sha256='27d703e0746b25cab0229285013e955f676ab9d8460d7f7c3c01df4c257b2d95')
    version('1.10.4-1', sha256='1ea6f9d45c94974f69b6918a248853ba24cbd80cdd1309b1be43eca65d6e7a75')
    version('1.10.4',   sha256='865fdf6aad389071ad063ec1c75a78ffc86eeb88bba011f3ea5281d243966b7a')
    version('1.10.2',   sha256='95a3ae6b273910571e25400a5cab1f7542cf589272c012c268f4b4724216f658')
    version('1.10.0',   sha256='cf61732ef9b38ecb6579055d1cd145198ad23a5a9ae4378f94a1494e6c56c884')
    version('1.9.8',    sha256='dadb21a14a7f4d60955cdd8fb9779136833498be97b1625914e9a6b580646f4d')
    version('1.9.6',    sha256='6f74c349c1731823aef6899edcf18418454167d04eba983e3a6fe17ee9fd236e')

    depends_on('r@3.1.0:', type=('build', 'run'))

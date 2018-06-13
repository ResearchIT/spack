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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install gtkplus3
#
# You can edit this file again by typing:
#
#     spack edit gtkplus3
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Gtkplus3(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://ftp.gnome.org/pub/gnome/sources/gtk+/3.0/gtk+-3.0.10.tar.gz"

    version('3.0.10', '6471f8ef87d6e166766e78696dc26a42')

    depends_on('glib')
    depends_on('gobject-introspection')
    depends_on('libxi')
    depends_on('xinput')
    depends_on('fixesproto')
    depends_on('inputproto')
    depends_on('pkgconfig', type='build')
#    depends_on('libepoxy')
    depends_on('atk')
    depends_on('gdk-pixbuf')
    depends_on('shared-mime-info')
    # Hardcode X11 support (former +X variant),
    # see #6940 for rationale:
    depends_on('pango+X')

    def patch(self):
        # remove disable deprecated flag.
        filter_file(r'CFLAGS="-DGDK_PIXBUF_DISABLE_DEPRECATED $CFLAGS"',
                    '', 'configure', string=True)

    def build(self, spec, prefix):
        filter_file(r'old_width: location to store previous forced minumum height',
                    'old_height: location to store previous forced minumum height',
                    'gtk/gtkwidget.c', string=True)
        filter_file(r'/* _gtk_load_custom_papers() only on Unix so far  */', '',
                    'gtk/gtkpapersize.c', string=True)
        filter_file(r'defined', '', 'demos/gtk-demo/geninclude.pl', string=True)
        make()

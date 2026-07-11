%global tl_name tex-gyre
%global tl_revision 68624

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.501
Release:	%{tl_revision}.1
Summary:	TeX Fonts extending freely available URW fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/tex-gyre
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The TeX-GYRE bundle consists of six font families: TeX Gyre Adventor is
based on the URW Gothic L family of fonts (which is derived from ITC
Avant Garde Gothic, designed by Herb Lubalin and Tom Carnase). TeX Gyre
Bonum is based on the URW Bookman L family (from Bookman Old Style,
designed by Alexander Phemister). TeX Gyre Chorus is based on URW
Chancery L Medium Italic (from ITC Zapf Chancery, designed by Hermann
Zapf in 1979). TeX-Gyre Cursor is based on URW Nimbus Mono L (based on
Courier, designed by Howard G. Kettler in 1955, for IBM). TeX Gyre Heros
is based on URW Nimbus Sans L (from Helvetica, prepared by Max
Miedinger, with Eduard Hoffmann in 1957). TeX Gyre Pagella is based on
URW Palladio L (from Palatino, designed by Hermann Zapf in the 1940s).
TeX Gyre Schola is based on the URW Century Schoolbook L family (from
Century Schoolbook, designed by Morris Fuller Benton for the American
Type Founders). TeX Gyre Termes is based on the URW Nimbus Roman No9 L
family of fonts (from Times New Roman, designed by Stanley Morison
together with Starling Burgess and Victor Lardent and first offered by
Monotype). The constituent standard faces of each family have been
greatly extended (though Chorus omits Greek support and has no small-
caps family). Each family is available in Adobe Type 1 and Open Type
formats, and LaTeX support (for use with a variety of encodings) is
provided. Vietnamese characters were added by Han The Thanh. There are
companion maths fonts for several of these designs, listed in the TeX
Gyre Math package.


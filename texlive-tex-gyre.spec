Name:		texlive-tex-gyre
Version:	68624
Release:	1
Summary:	TeX Fonts extending freely available URW fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/tex-gyre
License:	GFSL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
The TeX-GYRE bundle consists of six font families: TeX Gyre
Adventor is based on the URW Gothic L family of fonts (which is
derived from ITC Avant Garde Gothic, designed by Herb Lubalin
and Tom Carnase). TeX Gyre Bonum is based on the URW Bookman L
family (from Bookman Old Style, designed by Alexander
Phemister). TeX Gyre Chorus is based on URW Chancery L Medium
Italic (from ITC Zapf Chancery, designed by Hermann Zapf in
1979). TeX-Gyre Cursor is based on URW Nimbus Mono L (based on
Courier, designed by Howard G. Kettler in 1955, for IBM). TeX
Gyre Heros is based on URW Nimbus Sans L (from Helvetica,
prepared by Max Miedinger, with Eduard Hoffmann in 1957). TeX
Gyre Pagella is based on URW Palladio L (from Palation,
designed by Hermann Zapf in the 1940s). TeX Gyre Schola is
based on the URW Century Schoolbook L family (which was
designed by Morris Fuller Benton for the American Type
Founders). TeX Gyre Termes is based on the URW Nimbus Roman No9
L family of fonts (whose original, Times, was designed by
Stanley Morison together with Starling Burgess and Victor
Lardent and first offered by Monotype). The constituent
standard faces of each family have been greatly extended, and
contain nearly 1200 glyphs each (though Chorus omits Greek
support, has no small-caps family and has approximately 900
glyphs). Each family is available in Adobe Type 1 and Open Type
formats, and LaTeX support (for use with a variety of
encodings) is provided. Vietnamese and Cyrillic characters were
added by Han The Thanh and Valek Filippov, respectively.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/tex-gyre
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre
%{_texmfdistdir}/fonts/map/dvips/tex-gyre
%{_texmfdistdir}/fonts/opentype/public/tex-gyre
%{_texmfdistdir}/fonts/tfm/public/tex-gyre
%{_texmfdistdir}/fonts/type1/public/tex-gyre
%{_texmfdistdir}/tex/latex/tex-gyre
%_texmf_updmap_d/tex-gyre
%doc %{_texmfdistdir}/doc/fonts/tex-gyre

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/tex-gyre <<EOF
Map qag.map
Map qbk.map
Map qcr.map
Map qcs.map
Map qhv.map
Map qpl.map
Map qtm.map
Map qzc.map
EOF

# revision 18651
# category Package
# catalog-ctan /fonts/tex-gyre
# catalog-date 2009-11-12 13:33:47 +0100
# catalog-license gfsl
# catalog-version 2.004
Name:		texlive-tex-gyre
Version:	2.501
Release:	1
Summary:	TeX Fonts extending freely available URW fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/tex-gyre
License:	GFSL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-gyre.doc.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qagb.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qagbi.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qagr.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qagri.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qbkb.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qbkbi.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qbkr.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qbkri.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qcrb.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qcrbi.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qcrr.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qcrri.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qcsb.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qcsbi.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qcsr.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qcsri.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qhvb.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qhvbi.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qhvcb.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qhvcbi.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qhvcr.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qhvcri.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qhvr.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qhvri.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qplb.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qplbi.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qplr.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qplri.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qtmb.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qtmbi.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qtmr.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qtmri.afm
%{_texmfdistdir}/fonts/afm/public/tex-gyre/qzcmi.afm
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-cs-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-cs.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-csm-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-csm.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-cszc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-ec-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-l7x-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-l7x.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-l7xzc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-qx-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-qx.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-qxm-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-qxm.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-qxzc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-rm-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-rm.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-rmm-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-rmm.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-rmzc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-t5-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-t5.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-texnansi-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-texnansi.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-texnansizc.enc
%{_texmfdistdir}/fonts/enc/dvips/tex-gyre/q-ts1.enc
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qag-cs.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qag-ec.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qag-l7x.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qag-qx.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qag-rm.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qag-t5.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qag-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qag-ts1.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qag.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qbk-cs.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qbk-ec.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qbk-l7x.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qbk-qx.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qbk-rm.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qbk-t5.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qbk-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qbk-ts1.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qbk.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcr-cs.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcr-ec.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcr-l7x.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcr-qx.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcr-rm.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcr-t5.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcr-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcr-ts1.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcr.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcs-cs.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcs-ec.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcs-l7x.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcs-qx.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcs-rm.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcs-t5.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcs-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcs-ts1.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qcs.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qhv-cs.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qhv-ec.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qhv-l7x.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qhv-qx.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qhv-rm.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qhv-t5.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qhv-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qhv-ts1.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qhv.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qpl-cs.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qpl-ec.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qpl-l7x.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qpl-qx.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qpl-rm.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qpl-t5.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qpl-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qpl-ts1.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qpl.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qtm-cs.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qtm-ec.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qtm-l7x.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qtm-qx.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qtm-rm.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qtm-t5.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qtm-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qtm-ts1.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qtm.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qzc-cs.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qzc-ec.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qzc-l7x.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qzc-qx.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qzc-rm.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qzc-t5.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qzc-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qzc-ts1.map
%{_texmfdistdir}/fonts/map/dvips/tex-gyre/qzc.map
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreadventor-bold.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreadventor-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreadventor-italic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreadventor-regular.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrebonum-bold.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrebonum-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrebonum-italic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrebonum-regular.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrechorus-mediumitalic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrecursor-bold.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrecursor-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrecursor-italic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrecursor-regular.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreheros-bold.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreheros-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreheros-italic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreheros-regular.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreheroscn-bold.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreheroscn-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreheroscn-italic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreheroscn-regular.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrepagella-bold.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrepagella-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrepagella-italic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyrepagella-regular.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreschola-bold.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreschola-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreschola-italic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyreschola-regular.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyretermes-bold.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyretermes-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyretermes-italic.otf
%{_texmfdistdir}/fonts/opentype/public/tex-gyre/texgyretermes-regular.otf
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qagb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qagb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qagbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qagbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qagr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qagr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qagri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qagri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qbkb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qbkb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qbkbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qbkbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qbkr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qbkr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qbkri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qbkri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcrb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcrb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcrbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcrbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcrr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcrr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcrri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcrri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcsb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcsb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcsbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcsbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcsr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcsr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcsri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qcsri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvcb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvcb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvcbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvcr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvcr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvcri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvcri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qhvri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qplb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qplb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qplbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qplr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qplr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qplri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qplri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qtmb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qtmb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qtmbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qtmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qtmr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qtmr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qtmri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qtmri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/cs-qzcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qagb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qagb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qagbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qagbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qagr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qagr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qagri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qagri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qbkb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qbkb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qbkbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qbkbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qbkr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qbkr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qbkri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qbkri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcrb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcrb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcrbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcrbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcrr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcrr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcrri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcrri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcsb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcsb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcsbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcsbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcsr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcsr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcsri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qcsri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvcb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvcb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvcbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvcr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvcr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvcri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvcri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qhvri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qplb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qplb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qplbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qplr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qplr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qplri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qplri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qtmb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qtmb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qtmbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qtmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qtmr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qtmr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qtmri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qtmri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ec-qzcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qagb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qagb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qagbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qagbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qagr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qagr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qagri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qagri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qbkb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qbkb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qbkbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qbkbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qbkr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qbkr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qbkri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qbkri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcrb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcrb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcrbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcrbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcrr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcrr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcrri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcrri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcsb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcsb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcsbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcsbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcsr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcsr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcsri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qcsri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvcb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvcb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvcbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvcr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvcr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvcri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvcri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qhvri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qplb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qplb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qplbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qplr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qplr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qplri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qplri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qtmb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qtmb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qtmbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qtmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qtmr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qtmr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qtmri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qtmri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/l7x-qzcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qagb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qagb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qagbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qagbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qagr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qagr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qagri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qagri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qbkb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qbkb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qbkbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qbkbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qbkr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qbkr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qbkri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qbkri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcrb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcrb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcrbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcrbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcrr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcrr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcrri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcrri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcsb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcsb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcsbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcsbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcsr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcsr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcsri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qcsri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvcb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvcb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvcbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvcr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvcr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvcri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvcri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qhvri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qplb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qplb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qplbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qplr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qplr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qplri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qplri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qtmb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qtmb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qtmbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qtmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qtmr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qtmr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qtmri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qtmri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/qx-qzcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qagb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qagb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qagbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qagbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qagr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qagr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qagri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qagri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qbkb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qbkb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qbkbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qbkbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qbkr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qbkr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qbkri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qbkri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcrb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcrb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcrbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcrbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcrr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcrr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcrri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcrri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcsb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcsb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcsbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcsbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcsr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcsr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcsri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qcsri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvcb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvcb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvcbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvcr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvcr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvcri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvcri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qhvri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qplb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qplb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qplbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qplr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qplr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qplri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qplri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qtmb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qtmb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qtmbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qtmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qtmr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qtmr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qtmri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qtmri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/rm-qzcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qagb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qagb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qagbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qagbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qagr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qagr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qagri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qagri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qbkb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qbkb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qbkbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qbkbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qbkr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qbkr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qbkri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qbkri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcrb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcrb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcrbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcrbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcrr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcrr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcrri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcrri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcsb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcsb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcsbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcsbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcsr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcsr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcsri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qcsri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvcb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvcb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvcbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvcr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvcr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvcri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvcri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qhvri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qplb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qplb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qplbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qplr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qplr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qplri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qplri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qtmb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qtmb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qtmbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qtmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qtmr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qtmr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qtmri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qtmri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/t5-qzcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qagb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qagb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qagbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qagbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qagr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qagr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qagri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qagri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qbkb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qbkb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qbkbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qbkbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qbkr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qbkr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qbkri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qbkri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcrb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcrb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcrbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcrbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcrr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcrr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcrri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcrri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcsb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcsb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcsbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcsbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcsr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcsr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcsri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qcsri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvcb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvcb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvcbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvcr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvcr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvcri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvcri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qhvri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qplb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qplb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qplbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qplr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qplr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qplri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qplri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qtmb-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qtmb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qtmbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qtmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qtmr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qtmr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qtmri-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qtmri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/texnansi-qzcmi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qagb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qagbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qagr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qagri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qbkb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qbkbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qbkr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qbkri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qcrb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qcrbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qcrr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qcrri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qcsb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qcsbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qcsr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qcsri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qhvb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qhvbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qhvcb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qhvcbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qhvcr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qhvcri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qhvr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qhvri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qplb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qplbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qplr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qplri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qtmb.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qtmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qtmr.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qtmri.tfm
%{_texmfdistdir}/fonts/tfm/public/tex-gyre/ts1-qzcmi.tfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qagb.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qagb.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qagbi.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qagbi.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qagr.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qagr.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qagri.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qagri.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qbkb.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qbkb.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qbkbi.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qbkbi.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qbkr.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qbkr.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qbkri.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qbkri.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcrb.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcrb.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcrbi.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcrbi.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcrr.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcrr.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcrri.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcrri.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcsb.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcsb.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcsbi.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcsbi.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcsr.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcsr.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcsri.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qcsri.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvb.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvb.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvbi.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvbi.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvcb.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvcb.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvcbi.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvcbi.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvcr.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvcr.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvcri.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvcri.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvr.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvr.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvri.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qhvri.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qplb.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qplb.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qplbi.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qplbi.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qplr.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qplr.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qplri.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qplri.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qtmb.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qtmb.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qtmbi.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qtmbi.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qtmr.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qtmr.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qtmri.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qtmri.pfm
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qzcmi.pfb
%{_texmfdistdir}/fonts/type1/public/tex-gyre/qzcmi.pfm
%{_texmfdistdir}/tex/latex/tex-gyre/il2qag.fd
%{_texmfdistdir}/tex/latex/tex-gyre/il2qbk.fd
%{_texmfdistdir}/tex/latex/tex-gyre/il2qcr.fd
%{_texmfdistdir}/tex/latex/tex-gyre/il2qcs.fd
%{_texmfdistdir}/tex/latex/tex-gyre/il2qhv.fd
%{_texmfdistdir}/tex/latex/tex-gyre/il2qhvc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/il2qpl.fd
%{_texmfdistdir}/tex/latex/tex-gyre/il2qtm.fd
%{_texmfdistdir}/tex/latex/tex-gyre/il2qzc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/l7xqag.fd
%{_texmfdistdir}/tex/latex/tex-gyre/l7xqbk.fd
%{_texmfdistdir}/tex/latex/tex-gyre/l7xqcr.fd
%{_texmfdistdir}/tex/latex/tex-gyre/l7xqcs.fd
%{_texmfdistdir}/tex/latex/tex-gyre/l7xqhv.fd
%{_texmfdistdir}/tex/latex/tex-gyre/l7xqhvc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/l7xqpl.fd
%{_texmfdistdir}/tex/latex/tex-gyre/l7xqtm.fd
%{_texmfdistdir}/tex/latex/tex-gyre/l7xqzc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ly1qag.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ly1qbk.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ly1qcr.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ly1qcs.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ly1qhv.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ly1qhvc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ly1qpl.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ly1qtm.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ly1qzc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot1qag.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot1qbk.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot1qcr.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot1qcs.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot1qhv.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot1qhvc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot1qpl.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot1qtm.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot1qzc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot4qag.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot4qbk.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot4qcr.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot4qcs.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot4qhv.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot4qhvc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot4qpl.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot4qtm.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ot4qzc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qbookman.sty
%{_texmfdistdir}/tex/latex/tex-gyre/qcourier.sty
%{_texmfdistdir}/tex/latex/tex-gyre/qpalatin.sty
%{_texmfdistdir}/tex/latex/tex-gyre/qswiss.sty
%{_texmfdistdir}/tex/latex/tex-gyre/qtimes.sty
%{_texmfdistdir}/tex/latex/tex-gyre/qxqag.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qxqbk.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qxqcr.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qxqcs.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qxqhv.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qxqhvc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qxqpl.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qxqtm.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qxqzc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/qzapfcha.sty
%{_texmfdistdir}/tex/latex/tex-gyre/t1qag.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t1qbk.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t1qcr.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t1qcs.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t1qhv.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t1qhvc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t1qpl.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t1qtm.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t1qzc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t5qag.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t5qbk.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t5qcr.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t5qcs.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t5qhv.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t5qhvc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t5qpl.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t5qtm.fd
%{_texmfdistdir}/tex/latex/tex-gyre/t5qzc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/tgadventor.sty
%{_texmfdistdir}/tex/latex/tex-gyre/tgbonum.sty
%{_texmfdistdir}/tex/latex/tex-gyre/tgchorus.sty
%{_texmfdistdir}/tex/latex/tex-gyre/tgcursor.sty
%{_texmfdistdir}/tex/latex/tex-gyre/tgheros.sty
%{_texmfdistdir}/tex/latex/tex-gyre/tgpagella.sty
%{_texmfdistdir}/tex/latex/tex-gyre/tgschola.sty
%{_texmfdistdir}/tex/latex/tex-gyre/tgtermes.sty
%{_texmfdistdir}/tex/latex/tex-gyre/ts1qag.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ts1qbk.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ts1qcr.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ts1qcs.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ts1qhv.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ts1qhvc.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ts1qpl.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ts1qtm.fd
%{_texmfdistdir}/tex/latex/tex-gyre/ts1qzc.fd
%_texmf_updmap_d/tex-gyre
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/GUST-FONT-LICENSE.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Adventor.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Bonum.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Chorus.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Cursor.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Heros.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Pagella.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Schola.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Termes.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/README-TeX-Gyre-Adventor.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/README-TeX-Gyre-Bonum.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/README-TeX-Gyre-Chorus.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/README-TeX-Gyre-Cursor.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/README-TeX-Gyre-Heros.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/README-TeX-Gyre-Pagella.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/README-TeX-Gyre-Schola.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/README-TeX-Gyre-Termes.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/goadb999.nam
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qag-hist.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qag-info.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qag-test.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qag-test.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qagb.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qagbi.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qagr.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qagri.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qbk-hist.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qbk-info.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qbk-test.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qbk-test.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qbkb.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qbkbi.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qbkr.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qbkri.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcr-hist.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcr-info.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcr-test.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcr-test.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcrb.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcrbi.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcrr.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcrri.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcs-hist.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcs-info.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcs-test.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcs-test.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcsb.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcsbi.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcsr.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qcsri.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhv-hist.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhv-info.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhv-test.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhv-test.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhvb.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhvbi.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhvcb.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhvcbi.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhvcr.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhvcri.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhvr.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qhvri.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qpl-hist.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qpl-info.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qpl-test.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qpl-test.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qplb.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qplbi.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qplr.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qplri.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qtm-hist.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qtm-info.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qtm-test.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qtm-test.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qtmb.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qtmbi.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qtmr.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qtmri.fea
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qzc-hist.txt
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qzc-info.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qzc-test.pdf
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qzc-test.tex
%doc %{_texmfdistdir}/doc/fonts/tex-gyre/qzcmi.fea

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

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

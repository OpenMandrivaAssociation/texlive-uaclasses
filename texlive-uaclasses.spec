# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/uaclasses
# catalog-date 2009-01-05 22:46:04 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-uaclasses
Version:	20090105
Release:	1
Summary:	University of Arizona thesis and dissertation format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uaclasses
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uaclasses.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uaclasses.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uaclasses.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX2e document class named 'ua-
thesis' for typesetting theses and dissertations in the
official format required by the University of Arizona.
Moreover, there is a fully compatible alternative document
class 'my-thesis' for private 'nice' copies of the
dissertation, and the respective title pages are available as
separate packages to work with any document class.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uaclasses/my-thesis.cls
%{_texmfdistdir}/tex/latex/uaclasses/my-title.sty
%{_texmfdistdir}/tex/latex/uaclasses/ua-thesis.cls
%{_texmfdistdir}/tex/latex/uaclasses/ua-title.sty
%doc %{_texmfdistdir}/doc/latex/uaclasses/README
%doc %{_texmfdistdir}/doc/latex/uaclasses/my-example.pdf
%doc %{_texmfdistdir}/doc/latex/uaclasses/ua-example.pdf
%doc %{_texmfdistdir}/doc/latex/uaclasses/ua-example.tex
#- source
%doc %{_texmfdistdir}/source/latex/uaclasses/ua-classes.dtx
%doc %{_texmfdistdir}/source/latex/uaclasses/ua-classes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

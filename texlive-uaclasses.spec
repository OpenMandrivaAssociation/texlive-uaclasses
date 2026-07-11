%global tl_name uaclasses
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	University of Arizona thesis and dissertation format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uaclasses
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uaclasses.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uaclasses.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uaclasses.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX2e document class named 'ua-thesis' for
typesetting theses and dissertations in the official format required by
the University of Arizona. Moreover, there is a fully compatible
alternative document class 'my-thesis' for private 'nice' copies of the
dissertation, and the respective title pages are available as separate
packages to work with any document class.


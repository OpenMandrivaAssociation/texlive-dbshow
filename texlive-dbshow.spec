%global tl_name dbshow
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	A package to store and display data with custom filters, orders, and styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dbshow
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dbshow.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dbshow.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dbshow.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides four core functions: data storage and display data
filtering data sorting data display All data is saved once and then you
can display these data with custom filters, orders and styles. The
package can be used, for example, to record and display something you'd
like to review, maybe the question you always answered incorrectly or
some forgettable knowledge. But obviously, the package is much more
powerful and extensible for more interesting tasks depending on the
individual.


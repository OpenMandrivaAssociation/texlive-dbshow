Name:		texlive-dbshow
Version:	61634
Release:	2
Summary:	A package to store and display data with custom filters, orders, and styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dbshow
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dbshow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dbshow.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dbshow.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides four core functions: data storage and
display data filtering data sorting data display All data is
saved once and then you can display these data with custom
filters, orders and styles. The package can be used, for
example, to record and display something you'd like to review,
maybe the question you always answered incorrectly or some
forgettable knowledge. But obviously, the package is much more
powerful and extensible for more interesting tasks depending on
the individual.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/dbshow
%{_texmfdistdir}/tex/latex/dbshow
%doc %{_texmfdistdir}/doc/latex/dbshow

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

%define __noautoreq 'perl\\('
%define __noautoprov 'perl\\('

%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define _cabal_setup Setup.lhs
%define _no_haddock 1
%define module Pugs

Summary:	A Perl 6 Implementation
Name:		%{module}
Version:	6.2.13.20130611
Release:	1
License:	BSD
Group:		Development/Other
Url:		http://hackage.haskell.org/package/Pugs
Source0:	http://hackage.haskell.org/package/%{module}-%{version}/%{module}-%{version}.tar.gz
BuildRequires:	cabal-install
BuildRequires:	haskell-macros
BuildRequires:	ghc-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(ncurses)

%description
A Perl 6 Implementation

%files
%{_docdir}/%{module}-%{version}
%{_datadir}/%{module}-%{version}
%{_bindir}/pugs
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
cabal update
cabal install
cabal configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-executable-stripping
cabal build
%_cabal_genscripts

%install
%_cabal_install
%_cabal_rpm_gen_deps


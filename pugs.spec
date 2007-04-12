%define name	pugs
%define version	6.2.13
%define	release	%mkrel 2
%define module  Perl6-Pugs

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A Perl 6 interpreter
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://www.pugscode.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel readline-devel ncurses-devel
BuildRequires:	ghc >= 6.4

%define _requires_exceptions perl(
%define _provides_exceptions perl(

%description
Pugs is an interpreter for Perl 6, written in Haskell. It aims to implement
the full Perl6 specification, as detailed in the Synopses.

This pugs is built without support for inline Haskell, and without parrot
embedding (thus you'll need parrot in your PATH to use Perl 6 rules support).

%prep
%setup -q -n %{module}-%{version}

%build
export PUGS_EMBED=perl5
%{__perl} Makefile.PL INSTALLDIRS=vendor
# // build is broken, (misc, pugs 6.2.13)
make

%check
# test take 4h, and fail as ttream first write the test, and then code
# but release without having all test working ( there is too much to do )
#make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# note that this is a transient Perl 6 lib directory.
rm -f %{buildroot}/usr/lib/perl6/*/perllocal.pod

# we don't really need the .hi files if we don't develop pugs-enabled haskell
# software. (We could relocate this in a -devel package though.)
rm -rf %{buildroot}/%_lib/Pugs-*

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README READTHEM VICTUALS examples
%{perl_vendorlib}/Perl6/*
%{perl_vendorlib}/Inline/*
%{_mandir}/*/*
%{_bindir}/*
%_prefix/lib/perl6



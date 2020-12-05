%global         debug_package %{nil}
%global         git_revision d80f262f894bfc1d8a8ba79fdc5d1c14f738a140
%global         git_revision_short %(echo %{git_revision} | head -c 7)
%global         build_timestamp %(date +"%Y%m%d")

Name:           neovim
Version:        0.5.0
Release:        %{build_timestamp}~%{git_revision_short}%{?dist}
Summary:        Neovim %{version} pre-release build

License:        Apache License Version 2.0
URL:            https://github.com/neovim/neovim
Source0:        %{url}/archive/%{git_revision}.tar.gz

BuildRequires:  ninja-build
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  patch
BuildRequires:  gettext

Recommends:     xsel

%description
Neovim is a refactor - and sometimes redactor - in the tradition of
Vim, which itself derives from Stevie. It is not a rewrite, but a
continuation and extension of Vim. Many rewrites, clones, emulators
and imitators exist; some are very clever, but none are Vim. Neovim
strives to be a superset of Vim, notwithstanding some intentionally
removed misfeatures; excepting those few and carefully-considered
excisions, Neovim is Vim. It is built for users who want the good
parts of Vim, without compromise, and more.

%prep
%autosetup -n %{name}-%{git_revision}

%build
%{__make} CMAKE_BUILD_TYPE=Release

%install
%{make_install} CMAKE_INSTALL_PREFIX=%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%license LICENSE
%doc BACKERS.md CONTRIBUTING.md README.md
%{_bindir}/nvim
%{_libdir}/nvim/parser/c.so
%{_mandir}/man1/nvim.1.gz
%{_datadir}/pixmaps/nvim.png
%{_datadir}/applications/*
%{_datadir}/locale/*
%{_datadir}/nvim/*

%changelog
* Tue Dec  1 15:16:59 EST 2020 Peter Wu - v0.5.0
- git commit d80f262f894bfc1d8a8ba79fdc5d1c14f738a140

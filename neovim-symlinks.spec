Name:           neovim-symlinks
Version:        1.0.0
Release:        1%{?dist}

Summary:        Symlinks for neovim
License:        MIT

BuildArch:      noarch

%description
Create symlinks for neovim
Replace vi & vim by linking relevant commands to neovim

BuildRequires:  bash
Requires:       neovim

Provides:       vi
Provides:       vim

Conflicts:      vi
Conflicts:      vim

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_mandir}/man1


echo -e '#!/bin/sh\nexec nvim -e "$@"'  > %{buildroot}%{_bindir}/ex
echo -e '#!/bin/sh\nexec nvim -RZ "$@"' > %{buildroot}%{_bindir}/rview
echo -e '#!/bin/sh\nexec nvim -Z "$@"'  > %{buildroot}%{_bindir}/rvim
echo -e '#!/bin/sh\nexec nvim -R "$@"'  > %{buildroot}%{_bindir}/view
echo -e '#!/bin/sh\nexec nvim -d "$@"'  > %{buildroot}%{_bindir}/vimdiff

%{__chmod} 0755 %{buildroot}%{_bindir}/*

for _f in vi vim; do
  %{__ln_s} %{_bindir}/nvim %{buildroot}%{_bindir}/${_f}
done

%{__ln_s} %{_mandir}/man1/nvim.1.gz %{buildroot}%{_mandir}/man1/vim.1.gz
%{__ln_s} %{_mandir}/man1/nvim.1.gz %{buildroot}%{_mandir}/man1/vi.1.gz

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/ex
%{_bindir}/rview
%{_bindir}/vi
%{_bindir}/view
%{_bindir}/rvim
%{_bindir}/vim
%{_bindir}/vimdiff
%{_mandir}/man1/*

%changelog
* Tue Dec  1 20:20:03 EST 2020 Peter Wu <peterwu@hotmail.com>
- New Release - v1.0.0

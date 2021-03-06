#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF893C674816AA95D (filipe@lains.me)
#
Name     : pypi-build
Version  : 0.8.0
Release  : 18
URL      : https://files.pythonhosted.org/packages/52/fa/931038182be739955cf83179d9b9a6ce9832bc5f9a917a006f765cb53a1f/build-0.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/fa/931038182be739955cf83179d9b9a6ce9832bc5f9a917a006f765cb53a1f/build-0.8.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/52/fa/931038182be739955cf83179d9b9a6ce9832bc5f9a917a006f765cb53a1f/build-0.8.0.tar.gz.asc
Summary  : A simple, correct PEP 517 build frontend
Group    : Development/Tools
License  : MIT
Requires: pypi-build-bin = %{version}-%{release}
Requires: pypi-build-license = %{version}-%{release}
Requires: pypi-build-python = %{version}-%{release}
Requires: pypi-build-python3 = %{version}-%{release}
Requires: pypi(packaging)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(colorama)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pep517)
BuildRequires : pypi(setuptools)

%description
# build
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pypa/build/main.svg)](https://results.pre-commit.ci/latest/github/pypa/build/main)
[![CI check](https://github.com/pypa/build/workflows/check/badge.svg)](https://github.com/pypa/build/actions)
[![CI test](https://github.com/pypa/build/actions/workflows/test.yml/badge.svg)](https://github.com/pypa/build/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/pypa/build/branch/main/graph/badge.svg)](https://codecov.io/gh/pypa/build)

%package bin
Summary: bin components for the pypi-build package.
Group: Binaries
Requires: pypi-build-license = %{version}-%{release}

%description bin
bin components for the pypi-build package.


%package license
Summary: license components for the pypi-build package.
Group: Default

%description license
license components for the pypi-build package.


%package python
Summary: python components for the pypi-build package.
Group: Default
Requires: pypi-build-python3 = %{version}-%{release}

%description python
python components for the pypi-build package.


%package python3
Summary: python3 components for the pypi-build package.
Group: Default
Requires: python3-core
Provides: pypi(build)
Requires: pypi(colorama)
Requires: pypi(packaging)
Requires: pypi(pep517)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-build package.


%prep
%setup -q -n build-0.8.0
cd %{_builddir}/build-0.8.0
pushd ..
cp -a build-0.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656362757
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-build
cp %{_builddir}/build-0.8.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-build/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyproject-build

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-build/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

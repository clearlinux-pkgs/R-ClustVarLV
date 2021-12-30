#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ClustVarLV
Version  : 2.0.1
Release  : 40
URL      : https://cran.r-project.org/src/contrib/ClustVarLV_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ClustVarLV_2.0.1.tar.gz
Summary  : Clustering of Variables Around Latent Variables
Group    : Development/Tools
License  : GPL-3.0
Requires: R-ClustVarLV-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppEigen
Requires: R-doParallel
Requires: R-foreach
Requires: R-iterators
Requires: R-plyr
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-doParallel
BuildRequires : R-foreach
BuildRequires : R-iterators
BuildRequires : R-plyr
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-ClustVarLV package.
Group: Libraries

%description lib
lib components for the R-ClustVarLV package.


%prep
%setup -q -c -n ClustVarLV
cd %{_builddir}/ClustVarLV

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589582758

%install
export SOURCE_DATE_EPOCH=1589582758
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ClustVarLV
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ClustVarLV
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ClustVarLV
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ClustVarLV || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ClustVarLV/DESCRIPTION
/usr/lib64/R/library/ClustVarLV/INDEX
/usr/lib64/R/library/ClustVarLV/Meta/Rd.rds
/usr/lib64/R/library/ClustVarLV/Meta/data.rds
/usr/lib64/R/library/ClustVarLV/Meta/features.rds
/usr/lib64/R/library/ClustVarLV/Meta/hsearch.rds
/usr/lib64/R/library/ClustVarLV/Meta/links.rds
/usr/lib64/R/library/ClustVarLV/Meta/nsInfo.rds
/usr/lib64/R/library/ClustVarLV/Meta/package.rds
/usr/lib64/R/library/ClustVarLV/Meta/vignette.rds
/usr/lib64/R/library/ClustVarLV/NAMESPACE
/usr/lib64/R/library/ClustVarLV/R/ClustVarLV
/usr/lib64/R/library/ClustVarLV/R/ClustVarLV.rdb
/usr/lib64/R/library/ClustVarLV/R/ClustVarLV.rdx
/usr/lib64/R/library/ClustVarLV/data/Rdata.rdb
/usr/lib64/R/library/ClustVarLV/data/Rdata.rds
/usr/lib64/R/library/ClustVarLV/data/Rdata.rdx
/usr/lib64/R/library/ClustVarLV/doc/Getting_started_with_ClustVarLV.R
/usr/lib64/R/library/ClustVarLV/doc/Getting_started_with_ClustVarLV.Rmd
/usr/lib64/R/library/ClustVarLV/doc/Getting_started_with_ClustVarLV.html
/usr/lib64/R/library/ClustVarLV/doc/clv3w-vignette.R
/usr/lib64/R/library/ClustVarLV/doc/clv3w-vignette.Rmd
/usr/lib64/R/library/ClustVarLV/doc/clv3w-vignette.html
/usr/lib64/R/library/ClustVarLV/doc/index.html
/usr/lib64/R/library/ClustVarLV/help/AnIndex
/usr/lib64/R/library/ClustVarLV/help/ClustVarLV.rdb
/usr/lib64/R/library/ClustVarLV/help/ClustVarLV.rdx
/usr/lib64/R/library/ClustVarLV/help/aliases.rds
/usr/lib64/R/library/ClustVarLV/help/paths.rds
/usr/lib64/R/library/ClustVarLV/html/00Index.html
/usr/lib64/R/library/ClustVarLV/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ClustVarLV/libs/ClustVarLV.so
/usr/lib64/R/library/ClustVarLV/libs/ClustVarLV.so.avx2
/usr/lib64/R/library/ClustVarLV/libs/ClustVarLV.so.avx512

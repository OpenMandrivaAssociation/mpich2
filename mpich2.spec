%define	name	mpich2
%define	version 1.0.4
%define subversion p1
%define release	%mkrel 7

%define	major		1.0.4
%define	libname		%mklibname mpich 2 %{major}
%define old_libname	%mklibname mpich 1
%define mpihome		/home/mpi

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	MPICH2 is a portable implementation of MPI
Source: 	http://www-unix.mcs.anl.gov/mpi/mpich/downloads/%{name}-%{version}%{subversion}.tar.bz2
Patch0:		%{name}-1.0.4.soname.patch
URL: 		http://www-unix.mcs.anl.gov/mpi/mpich/
License:	BSD-style 
Group: 		Development/Other
Requires: 	%{libname} = %{version}
Requires:	expect
Requires:	python
BuildRequires:	gcc-gfortran
BuildRequires:	python
BuildConflicts:	g95
Conflicts:	mpich >= 1.2
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
MPICH is a freely available, portable implementation of MPI, the Standard 
for message-passing libraries.
MPICH-A Portable Implementation of MPI is a MPI Standard conforming library 
that was developed by the Argonne National Laboratory. It allows different 
processes across a network of workstations to communicate using specific 
message passing functions. It includes librairies, parallel debuging tools 
and docs.

This package provides the libraries that use the standard p4 device.

%package doc
Summary:	Documentation for developing programs that will use MPICH
Group:		Development/Other

%description doc
MPICH is a freely available, portable implementation of MPI, the Standard 
for message-passing libraries.
MPICH-A Portable Implementation of MPI is a MPI Standard conforming library 
that was developed by the Argonne National Laboratory. It allows different 
processes across a network of workstations to communicate using specific 
message passing functions. It includes librairies, parallel debuging tools 
and docs.

This package provides the documentation needed to develop
applications using the MPICH libraries.

%package -n %{libname}
Summary:	Shared Librairies for MPICH
Group:		Development/Other
Conflicts:	%{old_libname} >= 1.2
Provides:	lib%{name} = %{version}-%{release}
Conflicts:	libmpich

%description  -n %{libname}
Shared Librairies for MPICH

%package -n %{libname}-devel
Summary:	Headers for developing programs that will use MPICH
Group:		Development/Other
Requires:	%{libname} = %{version}
Conflicts:	%{old_libname}-devel >= 1.2
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	lam-devel, mpich1-devel

%description -n %{libname}-devel
MPICH is a freely available, portable implementation of MPI, the Standard 
for message-passing libraries.
MPICH-A Portable Implementation of MPI is a MPI Standard conforming library 
that was developed by the Argonne National Laboratory. It allows different 
processes across a network of workstations to communicate using specific 
message passing functions. It includes librairies, parallel debuging tools 
and docs.

This package provides the static libraries and header files needed to compile
applications using the MPICH libraries.

%package -n mpi2cc
Summary:	The MPICH wrapper over the C compiler
Group:		Development/C
Conflicts:	mpicc >= 1.2, lam-devel
Requires:	gcc >= 3.2
Requires:	%{libname}-devel = %{version}

%description -n mpi2cc
MPICH is a freely available, portable implementation of MPI, the Standard 
for message-passing libraries.
MPICH-A Portable Implementation of MPI is a MPI Standard conforming library 
that was developed by the Argonne National Laboratory. It allows different 
processes across a network of workstations to communicate using specific 
message passing functions. It includes librairies, parallel debuging tools 
and docs.

This package provides the shell script mpicc, with headers, which allows to
compile C programs using the MPICH libraries.

%package -n mpi2cxx
Summary:	The MPICH wrapper over the C++ compiler
Conflicts:	mpic++ >= 1.2, lam-devel
Group:		Development/C++
Requires:	gcc-c++ >= 3.2
Requires:	%{libname}-devel = %{version}

%description -n mpi2cxx
MPICH is a freely available, portable implementation of MPI, the Standard 
for message-passing libraries.
MPICH-A Portable Implementation of MPI is a MPI Standard conforming library 
that was developed by the Argonne National Laboratory. It allows different 
processes across a network of workstations to communicate using specific 
message passing functions. It includes librairies, parallel debuging tools 
and docs.

This package provides the shell script mpiCC, with headers, which allows to
compile C++ programs using the MPICH libraries.

%package -n mpi2f77
Summary:	The MPICH wrapper over the Fortran 77 compiler
Group:		Development/Other
Conflicts:	mpif77 >= 1.2, lam-devel
Requires:	gcc-gfortran >= 3.2
Requires:	%{libname}-devel = %{version}

%description -n mpi2f77
MPICH is a freely available, portable implementation of MPI, the Standard 
for message-passing libraries.
MPICH-A Portable Implementation of MPI is a MPI Standard conforming library 
that was developed by the Argonne National Laboratory. It allows different 
processes across a network of workstations to communicate using specific 
message passing functions. It includes librairies, parallel debuging tools 
and docs.

This package provides the shell script mpif77, with headers, which allows to
compile Fortran 77 (NOT Fortran 90!) programs using the MPICH libraries.

%package -n mpi2f90
Summary:	The MPICH wrapper over the Fortran 90 compiler
Group:		Development/Other
Requires:	gcc-gfortran >= 3.2
Requires:	%{libname}-devel = %{version}

%description -n mpi2f90
MPICH is a freely available, portable implementation of MPI, the Standard 
for message-passing libraries.
MPICH-A Portable Implementation of MPI is a MPI Standard conforming library 
that was developed by the Argonne National Laboratory. It allows different 
processes across a network of workstations to communicate using specific 
message passing functions. It includes librairies, parallel debuging tools 
and docs.

This package provides the shell script mpif90, with headers, which allows to
compile Fortran 90 (NOT Fortran 77!) programs using the MPICH libraries.

%prep
%setup -q -n %{name}-%{version}%{subversion}
%patch0 -p 1

%build
export F90=/usr/bin/gfortran

%configure \
    --datadir=%{_datadir}/mpich/ \
    --with-docdir=%{_datadir}/doc/%{name}-doc-%{version} \
    --with-htmldir=%{_datadir}/doc/%{name}-doc-%{version}/www \
    --enable-cache \
    --with-mpe \
    --enable-cxx \
    --with-arch=LINUX \
    --enable-sharedlibs=gcc \
    --disable-weak-symbols
make

%install
rm -rf %{buildroot}

%makeinstall_std

# fix end of lines
perl -pi -e 'tr/\r//d;' \
    %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/www/index.htm \
    %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/www/www1/index.htm \
    %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/www/www3/index.htm

# fix configuration
rm -f %{buildroot}%{_prefix}/etc/*.in
sed -i -e '1,2d' %{buildroot}%{_sysconfdir}/*.conf

# move other examples under %{_docdir}
mv %{buildroot}%{_datadir}/mpich %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/examples

# Cleaning uncessary files 
rm -f %{buildroot}%{_libdir}/*.jar
rm -f %{buildroot}%{_libdir}/*.o
rm -rf %{buildroot}%{_prefix}/sbin
rm -rf %{buildroot}%{_datadir}/logfiles
rm -rf %{buildroot}%{_bindir}/clog*
rm -rf %{buildroot}%{_bindir}/slog*
rm -rf %{buildroot}%{_bindir}/jumpshot
rm -rf %{buildroot}%{_bindir}/logconvertor
rm -f %{buildroot}%{_bindir}/rlogTOslog2
rm -f %{buildroot}%{_bindir}/rlog_check_timeorder
rm -f %{buildroot}%{_bindir}/rlog_print
rm -f %{buildroot}%{_bindir}/rlogprint
rm -f %{buildroot}%{_bindir}/traceTOslog2.in
rm -f %{buildroot}%{_bindir}/traceprint.in
rm -f %{buildroot}%{_libdir}/libTraceInput.la

cat > README.urpmi <<EOF
Post-installation procedure:
- create a user with constant uid/gid and shared home directory on all nodes
- ensure this user has rsh/ssh access to all nodes
For instance, a solution could be:
	# groupadd -g 12384 -r -f mpi 
	# useradd -u 12384 -g mpi -d %{mpihome} -r -s /bin/bash mpi -p "" -m
	# mkpasswd -l 32 | passwd --stdin mpi 2>&1 > /dev/null
	# ssh-keygen -f %{mpihome}/.ssh/id_dsa -t dsa -N "" 2>&1 > /dev/null
	# chown mpi:mpi %{mpihome}/.ssh/id_dsa
	# chmod 600 %{mpihome}/.ssh/id_dsa
EOF

%clean
rm -rf %{buildroot}

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYRIGHT README.urpmi
%{_bindir}/mpd*
%{_bindir}/mpi*
%{_mandir}/man1/MPI.1*
%{_mandir}/man1/mpiexec.1.*
%config(noreplace) %{_sysconfdir}/mpe_*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*-%{major}.so

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYRIGHT
%{_mandir}/man3/*.3*
%{_includedir}/*.h
%{_includedir}/*.mod
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/lib*-%{major}.so

%files doc
%defattr(-,root,root)
%{_datadir}/doc/%{name}-doc-%{version}

%files -n mpi2cc
%defattr(-,root,root)
%doc COPYRIGHT
%{_bindir}/mpicc
%config(noreplace) %{_sysconfdir}/mpicc.conf
%{_mandir}/man1/mpicc.1*

%files -n mpi2cxx
%defattr(-,root,root)
%doc COPYRIGHT
%{_bindir}/mpicxx
%config(noreplace) %{_sysconfdir}/mpicxx.conf
%{_mandir}/man1/mpicxx.1*

%files -n mpi2f77
%defattr(-,root,root)
%doc COPYRIGHT
%config(noreplace) %{_sysconfdir}/mpif77.conf
%{_bindir}/mpif77
%{_mandir}/man1/mpif77.1*

%files -n mpi2f90
%defattr(-,root,root)
%doc COPYRIGHT
%config(noreplace) %{_sysconfdir}/mpif90.conf
%{_bindir}/mpif90
%{_mandir}/man1/mpif90.1*



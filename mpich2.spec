%define	major		1.2
%define	libname		%mklibname mpich 2 %{major}
%define develname 	%mklibname mpich 2 -d
%define old_libname	%mklibname mpich 1
%define mpihome		/home/mpi


Name: 		mpich2
Version: 	1.2.1
Release: 	2
Summary: 	Portable implementation of MPI
Source0: 	http://www-unix.mcs.anl.gov/mpi/mpich/downloads/%{name}-%{version}.tar.gz
Patch0:		%{name}-1.0.7.soname.patch
Patch1:		mpich2-1.0.8-fix-str-fmt.patch
Patch2:		mpich2-modules.patch
Patch3:		mpich2_mpiexec.c.patch
URL: 		http://www-unix.mcs.anl.gov/mpi/mpich/
License:	BSD-style 
Group:		System/Cluster
Requires: 	%{libname} = %{version}
Requires:	expect
Requires:	python
BuildRequires:	gcc-gfortran
BuildRequires:	python
BuildConflicts:	g95
BuildRequires:	libx11-devel
Conflicts:	mpich >= 1.2

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
Group:		System/Cluster

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
Group:		System/Cluster
Conflicts:	%{old_libname} >= 1.2
Provides:	lib%{name} = %{EVRD}
Conflicts:	libmpich

%description  -n %{libname}
Shared Librairies for MPICH

%package -n %{develname}
Summary:	Headers for developing programs that will use MPICH
Group:		System/Cluster
Requires:	%{libname} = %{version}
Conflicts:	%{old_libname}-devel >= 1.2
Provides:	lib%{name}-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	lam-devel, mpich1-devel
Obsoletes:	%mklibname -d mpich 2 1.0.4
Obsoletes:	%mklibname -d mpich 2 1.0.5

%description -n %{develname}
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
Requires:	%{develname} = %{version}

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
Requires:	%{develname} = %{version}

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
Group:		System/Cluster
Conflicts:	mpif77 >= 1.2, lam-devel
Requires:	gcc-gfortran >= 3.2
Requires:	%{develname} = %{version}

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
Group:		System/Cluster
Requires:	gcc-gfortran >= 3.2
Requires:	%{develname} = %{version}

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
%setup -q
#%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p1

%build
export F90=/usr/bin/gfortran
export F77=/usr/bin/gfortran

%configure2_5x \
	--datadir=%{_datadir}/mpich/ \
	--docdir=%{_datadir}/doc/%{name}-doc-%{version} \
	--htmldir=%{_datadir}/doc/%{name}-doc-%{version}/www \
	--enable-cache \
	--enable-f77 \
	--enable-f90 \
	--enable-cxx \
	--enable-romio \
	--enable-smpcoll \
	--enable-async-progress \
	--enable-mpe \
	--enable-threads=default \
	--with-mpe \
	--with-arch=LINUX \
	--enable-sharedlibs=gcc \
	--disable-weak-symbols

#	--enable-nmpi-as-mpi \
make

%install
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

%files
%doc COPYRIGHT README.urpmi
%{_bindir}/check_callstack
%{_bindir}/mpd*
%{_bindir}/mpi*
%{_bindir}/pmi_proxy 
%{_bindir}/parkill
%{_mandir}/man1/mpd*.1*
%{_mandir}/man1/Zeroconf.1*
%{_mandir}/man1/mpiexec.1*
%{_mandir}/man1/MPI.1*
%{_mandir}/man4/MPE*
%config(noreplace) %{_sysconfdir}/mpe_*
%config(noreplace) %{_sysconfdir}/mpixxx_opts.conf
%exclude %{_bindir}/mpicc
%exclude %{_bindir}/mpicxx
%exclude %{_bindir}/mpif77
%exclude %{_bindir}/mpif90

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.1

%files -n %{develname}
%doc COPYRIGHT
%{_mandir}/man3/*.3*
%{_includedir}/*.h
%{_includedir}/*.mod
%{_includedir}/primitives/opa*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_datadir}/doc/%{name}-doc-%{version}

%files -n mpi2cc
%doc COPYRIGHT
%{_bindir}/mpicc
%config(noreplace) %{_sysconfdir}/mpicc.conf
%{_mandir}/man1/mpicc.1*

%files -n mpi2cxx
%doc COPYRIGHT
%{_bindir}/mpicxx
%config(noreplace) %{_sysconfdir}/mpicxx.conf
%{_mandir}/man1/mpicxx.1*

%files -n mpi2f77
%doc COPYRIGHT
%config(noreplace) %{_sysconfdir}/mpif77.conf
%{_bindir}/mpif77
%{_mandir}/man1/mpif77.1*

%files -n mpi2f90
%doc COPYRIGHT
%config(noreplace) %{_sysconfdir}/mpif90.conf
%{_bindir}/mpif90
%{_mandir}/man1/mpif90.1*




%changelog
* Mon Feb 08 2010 Antoine Ginies <aginies@mandriva.com> 1.2.1-1mdv2010.1
+ Revision: 502336
- fix mpiexec format not a string literal and no format arguments
- new version 1.2.1
- release 1.2.1 (modules patch from fedora)

* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.8-2mdv2010.0
+ Revision: 440144
- rebuild

* Mon Feb 09 2009 Funda Wang <fwang@mandriva.org> 1.0.8-1mdv2009.1
+ Revision: 338655
- fix str fmt
- New version 1.0.8

* Fri Aug 22 2008 Funda Wang <fwang@mandriva.org> 1.0.7-2mdv2009.0
+ Revision: 275037
- fix requires on devel package

* Sun Jul 20 2008 Funda Wang <fwang@mandriva.org> 1.0.7-1mdv2009.0
+ Revision: 238928
- rediff soname patch
- update file list
- new devel package policy
- New version 1.0.7

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.5-3mdv2008.1
+ Revision: 170989
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jun 22 2007 Nicolas Vigier <nvigier@mandriva.com> 1.0.5-2mdv2008.0
+ Revision: 42959
- Change group to System/Cluster

* Tue May 22 2007 Antoine Ginies <aginies@mandriva.com> 1.0.5-1mdv2008.0
+ Revision: 29783
- add missing binairies mpecc, mpefc and parkill
- release 1.0.5p4


* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-7mdv2007.0
+ Revision: 84791
- new release
- really fix soname patch

* Tue Nov 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-6mdv2007.1
+ Revision: 84109
- rediff and fixed soname patch

* Fri Nov 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-5mdv2007.1
+ Revision: 80787
- bump release
- buildrequires python
- Import mpich2

* Thu Sep 07 2006 Erwan Velu <erwan@seanodes.com> 1.0.4-3mdv2007.0
- Buildrequires python (needed by mpdboot)

* Fri Sep 01 2006 Erwan Velu <erwan@seanodes.com> 1.0.4-2mdk
- The day before ulteo
- Fixing Conflicts with lam & mpich

* Tue Aug 22 2006 Erwan Velu <erwan@seanodes.com> 1.0.4-1mdk
- 1.0.4p1
- Removing patch0, merged upstream
- Removing chrpath buildrequires as cpi example is not provided under binary form
- Adding some stuff from ghuibo
- Setting f90 to gfortran

* Mon May 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-2mdk
- fix major in lib package name
- fix devel package provides

* Wed May 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-1mdk
- new version
- spec cleanup
- don't mess with /etc/bashrc, use profile.d
- use standard configure macro
- use -p for ldconfig invocation in %%post
- no more rsh requirement, as either rsh or ssh can be used
- no more user creation in %%post, as it was too simplist to work, but advertise
  post-installation procedure through README.urpmi
- cleanup documentation
- no more useless shebang in configuration files
- fix summary
- fix group
- leverage versioned interdependencies
- drop useless explicit provides
- drop rpath in example
- add soname to libraries

* Sat Nov 26 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.0.2-3mdk
- fix requires (#16327)

* Sat Jul 23 2005 Austin Acton <austin@mandriva.org> 1.0.2-2mdk
- fix library name
- make lib64 friendly

* Mon Jul 04 2005 Lev Givon <lev@columbia.edu> 1.0.2-1mdk
- upgrade to mpich2 1.0.2

* Mon Mar 21 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.0.1-2mdk
- add conflict with mpich-1.2.X
- rename mpic++ to mpi2cxx

* Fri Mar 18 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.0.1-1mdk
- release mpich2 1.0.1

* Wed Jul 28 2004 Erwan Velu <erwan@mandrakesoft.com> 1.2.5.2-5mdk
- Rebuild

* Sat Jun 26 2004 Erwan Velu <erwan@mandrakesoft.com> 1.2.5.2-4mdk
- Disabling java in jumpshot

* Wed Jun 16 2004 Erwan Velu <erwan@mandrakesoft.com> 1.2.5.2-3mdk
- Fixing requires

* Sat Jun 12 2004 Erwan Velu <erwan@mandrakesoft.com> 1.2.5.2-2mdk
- Fixing path for buildroot path removing
- Using a new test program
- Requires libmpich1 on mpich

* Sun Jan 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.5.2-1mdk
- 1.2.5.2
- cosmetics
- don't rm -rf /home/mandrake/rpm/tmp/mpich2-1.0.4 at the beginning of %%prep
- no .bz2 ending for man pages in file list
- fix typo in Fortran interface for MPI_Wtime (P4)
- Fix to the MPI-IO Fortran interface (P5)
- work around rsh test that might stall (P6)
- fix unpackaged files
- fix permissions for docs


Name:           ffmpeg-release-64bit-static
Version:        3.3.2
Release:        1%{?dist}
BuildArch:      x86_64
URL:            https://www.johnvansickle.com/ffmpeg/
Source0:        https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz
License:        GPL3
Summary:        A complete, cross-platform solution to record, convert and stream audio and video.

%description
Extract original archive, then deploy binaries only to /usr/bin
https://www.johnvansickle.com/ffmpeg/

%prep
%setup -n ffmpeg-%{version}-64bit-static

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 0755 %{_builddir}/ffmpeg-%{version}-64bit-static/ffmpeg       $RPM_BUILD_ROOT/usr/bin/
install -m 0755 %{_builddir}/ffmpeg-%{version}-64bit-static/ffmpeg-10bit $RPM_BUILD_ROOT/usr/bin/
install -m 0755 %{_builddir}/ffmpeg-%{version}-64bit-static/ffprobe      $RPM_BUILD_ROOT/usr/bin/
install -m 0755 %{_builddir}/ffmpeg-%{version}-64bit-static/ffserver     $RPM_BUILD_ROOT/usr/bin/
install -m 0755 %{_builddir}/ffmpeg-%{version}-64bit-static/qt-faststart $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/ffmpeg
/usr/bin/ffmpeg-10bit
/usr/bin/ffprobe
/usr/bin/ffserver
/usr/bin/qt-faststart

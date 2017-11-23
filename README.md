## rpm-ffmpeg-release-64bit-static

## Quick build on CentOS 7

```bash
yum -y install rpm-build rpmdevtools

rpmdev-setuptree

wget -nc -P /root/rpmbuild/SOURCES/ "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz"
wget -nc -P /root/rpmbuild/SPECS/ "https://raw.githubusercontent.com/DRN88/rpm-ffmpeg-release-64bit-static/master/rpm-ffmpeg-release-64bit-static.spec"

rpmbuild -bb /root/rpmbuild/SPECS/rpm-ffmpeg-release-64bit-static.spec
```

## Quick build on Fedora 27

```bash
dnf -y --refresh install rpm-build rpmdevtools

rpmdev-setuptree

wget -nc -P /root/rpmbuild/SOURCES/ "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz"
wget -nc -P /root/rpmbuild/SPECS/ "https://raw.githubusercontent.com/DRN88/rpm-ffmpeg-release-64bit-static/master/rpm-ffmpeg-release-64bit-static.spec"

rpmbuild -bb /root/rpmbuild/SPECS/rpm-ffmpeg-release-64bit-static.spec
```

### Artifacts

```bash
[root@lxfedora27test01 ~]# tree /root/rpmbuild/RPMS/
/root/rpmbuild/RPMS/
└── x86_64
    └── ffmpeg-release-64bit-static-3.4-1.fc27.x86_64.rpm

1 directory, 1 file
```

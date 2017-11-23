## rpm-ffmpeg-release-64bit-static

## Quick build on CentOS 7

```bash
yum -y install rpm-build rpmdevtools

rpmdev-setuptree

wget 'https://raw.githubusercontent.com/DRN88/rpm-ffmpeg-release-64bit-static/master/rpm-ffmpeg-release-64bit-static.spec' -O /root/rpmbuild/SPECS/rpm-ffmpeg-release-64bit-static.spec

spectool -g -R /root/rpmbuild/SPECS/rpm-ffmpeg-release-64bit-static.spec
rpmbuild -bb /root/rpmbuild/SPECS/rpm-ffmpeg-release-64bit-static.spec
```

## Quick build on Fedora 27

```bash
dnf -y --refresh install rpm-build rpmdevtools

rpmdev-setuptree

wget 'https://raw.githubusercontent.com/DRN88/rpm-ffmpeg-release-64bit-static/master/rpm-ffmpeg-release-64bit-static.spec' -O /root/rpmbuild/SPECS/rpm-ffmpeg-release-64bit-static.spec

spectool -g -R /root/rpmbuild/SPECS/rpm-ffmpeg-release-64bit-static.spec
rpmbuild -bb /root/rpmbuild/SPECS/rpm-ffmpeg-release-64bit-static.spec
```

### Artifacts

```bash
[root@lxbuilder01 ~]# tree /root/rpmbuild/RPMS/
/root/rpmbuild/RPMS/
└── x86_64
    └── ffmpeg-release-64bit-static-3.3.2-1.el7.centos.x86_64.rpm

1 directory, 1 file
```

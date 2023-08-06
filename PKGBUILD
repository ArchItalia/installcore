# Maintainer: Jonathan Sanfilippo  <jonalinux dot uk at gmail dot com>

pkgname=installcore
pkgver=1.8
pkgrel=1
pkgdesc="installcore script"
arch=('any')
license=('GPL')


package() {
       mkdir -p "$pkgdir/usr/bin/"
       cp -rp  inc-files "$pkgdir/usr/bin/"
       chmod -R 755 inc-files
       mkdir -p "$pkgdir/usr/share/applications"
       mkdir -p "$pkgdir/etc/xdg/autostart/"
       cp -rp installcore.desktop "$pkgdir/usr/share/applications/"
       cp -rp installcore.desktop "$pkgdir/etc/xdg/autostart/"
       install -Dm755 -t "$pkgdir/usr/bin/" inc1
       install -Dm755 -t "$pkgdir/usr/bin/" installcore
}

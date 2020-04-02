# Running VS Code extension tests in Windows Subsystem for Linux

Set up wsl with Ubuntu-18.04 distro. Install Node and NPM.

1. Clone the repo in WSL
1. Run `npm install` and `npm test`

Got this error:

```bash
.vscode-test/vscode-1.43.2/VSCode-linux-x64/code: error while loading shared libraries: libX11-xcb.so.1: cannot open shared object file: No such file or directory
```

Followed [https://askubuntu.com/questions/1123722/error-while-loading-shared-libraries-libx11-xcb-so-1-cannot-open-shared-objec](this).

Eventually, I had to install all of these (I went one by one to find the minimal set):

```bash
sudo apt-get install x11-common \ 
  libx11-xcb1 \ 
  libxcomposite1 \
  libxcursor1 \
  libxdamage1 \
  libxi6 \
  libxtst6 \
  libnss3 \
  libgtk-3-0 \
  libxss1 \
  libasound2 
```

Then `npm test` gets further, but hits another error:

```bash
(code:3121): Gtk-WARNING **: 09:14:00.878: cannot open display:

Exit code:   1
Done
```

Trying hints from
https://blog.root.cz/petrkrcmar/gtk-warning-cannot-open-display/

```bash
export DISPLAY=:0.0
```

Trying hints from:
https://askubuntu.com/questions/1123722/error-while-loading-shared-libraries-libx11-xcb-so-1-cannot-open-shared-objec

```bash
export DISPLAY=<your windows ip>:0
```
Use `ipconfig` on Windows to find the IP address. If you have VPN installed, there may be many virtual adapters.

Still getting

```bash
(code:3265): Gtk-WARNING **: 09:21:36.493: cannot open display: 192.168.xxx.xxx:0

Exit code:   1
```

## Other links

https://github.com/containers/toolbox/issues/217
https://medium.com/@cloverinks/how-to-fix-puppetteer-error-ibx11-xcb-so-1-on-ubuntu-152c336368


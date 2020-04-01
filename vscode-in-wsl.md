# Running VS Code extension tests in Windows Subsystem for Linux

Set up wsl with Ubuntu-18.04 distro. Install Node and NPM.

1. Clone the repo in WSL
1. Run `npm install` and `npm test`

Got this error:

```bash
.vscode-test/vscode-1.43.2/VSCode-linux-x64/code: error while loading shared libraries: libX11-xcb.so.1: cannot open shared object file: No such file or directory
```

Followed [https://askubuntu.com/questions/1123722/error-while-loading-shared-libraries-libx11-xcb-so-1-cannot-open-shared-objec](this).

```bash
sudo apt install x11-common
```

No effect.

sudo apt install --assume-yes libx11-xcb1

libXcomposite.so.1: cannot open shared object file: No such file or directory

## Other links

https://github.com/containers/toolbox/issues/217

sudo apt-get install libxcomposite1

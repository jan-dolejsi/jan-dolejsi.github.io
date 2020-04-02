# Running VS Code extension tests in Windows Subsystem for Linux

The quest is to run vscode-tests (as in https://github.com/microsoft/vscode-extension-samples/tree/master/helloworld-test-sample) on wsl to locally reproduce build failures.

Set up wsl with Ubuntu-18.04 distro. Install, Git Node and NPM.

1. Clone the repo inside WSL
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

Still getting this error:

```bash
(code:3265): Gtk-WARNING **: 09:21:36.493: cannot open display: 192.168.xxx.xxx:0

Exit code:   1
```

Then I realized that I followed the [Visual Studio > Working with Extensions > Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) guide, 
which on GitHub using the **GabrielBB/xvfb-action@v1.0** build task to run my `npm test`. 
Looking at the build log file, it seems to first call:

```bash
/usr/bin/sudo apt-get install xvfb
```

And then it runs the test by `xvfb-run`:

```bash
/usr/bin/xvfb-run --auto-servernum npm test
```

I did exactly that. But then I am still getting following errors into the output:

```bash
> node ./out/test/runTest.js

Found .vscode-test/vscode-1.43.2. Skipping download.
Warning: 'sandbox' is not in the list of known options, but still passed to Electron/Chromium.

[main 2020-04-02T08:40:03.893Z] [File Watcher (node.js)] Error: ENOENT: no such file or directory, stat '/home/<user>/.config/Code/User'

[main 2020-04-02T08:40:04.346Z] update#setState idle

bash: cannot set terminal process group (-1): Invalid argument
bash: no job control in this shell

[main 2020-04-02T08:40:34.347Z] update#setState checking for updates

[main 2020-04-02T08:40:35.324Z] update#setState idle
```

And it hangs forever.

Now I am wondering what do these errors mean:

```bash
bash: cannot set terminal process group (-1): Invalid argument
bash: no job control in this shell
```

## Other links

https://github.com/containers/toolbox/issues/217
https://medium.com/@cloverinks/how-to-fix-puppetteer-error-ibx11-xcb-so-1-on-ubuntu-152c336368


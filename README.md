# sticker convertor

🔈: **Only static stickers conversation supported** due to WeChat can not display the gif converted by dynamic apng stickers properly.

🎉: But I has found a way to fix it (more can see [this](http://apngdis.sourceforge.net/)), waiting for scripting.


## dependency

- windows (actually my dev env)
- python3
- [image magick](https://www.imagemagick.org/)

## build exe

1. Create a one-file bundled executable.

    ```bash
    pyinstaller -F main.p utils.py [...]
    ```

2. Copy `main.exe` to root dir.
3. Delete build floder (no use).

## usage

Run `main.exe` in the root dir, then the png images in `image` floder will be converted to gif stickers in `dist` floder.

`root_path` is current path, which means if run `/src/main.py` will read `/src/image` floder.

## TODO

- [ ] Auto parse sticker package
- [ ] Drag and drop images to convert (exe)
- [ ] GUI version (setting path, using system file selector)
- [ ] Support dynamic apng

# Building and Publishing

After changes you need to `build` the project and
then `upload` the new version.

## 1. Make changes

- Make any changes necessary 
- `Update the Version!` in the `setup.cfg` file
- Test those changes
- Commit the changes
- Push the changes

## 2. Build

```bash
python3 -m build
```
You will need the [build module](https://github.com/pypa/build) for this. 

This will update the files in the `/dist` folder which
are uploaded in the next step. This has to be done
**every time**.

## 3. Upload

```bash
twine upload dist/*
```
For uploading I am using [Twine](https://twine.readthedocs.io/en/latest/).
This will need to be installed first.

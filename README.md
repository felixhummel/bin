```sh
cd $HOME
git clone https://github.com/felixhummel/bin.git
```

Enable bash completion with [my
structure](https://github.com/felixhummel/configs):
```sh
ln -s ~/bin/completion.bash ~/.bash/home-bin-completion
```

For `music` script:
```sh
uv venv -p 3.12
uv pip install 'libfelix[music,cli]>=0.5'
```

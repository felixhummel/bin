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
sudo apt-get -y install build-essential libdbus-1-dev cmake libglib2.0-dev python3-dev
cd ~/bin
mise trust
uv sync
```

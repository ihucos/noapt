# noapt
Is a small wrapper around `plash`, that lets you install ubuntu packages in your home folder. It does not acutaly need an ubuntu system and it can be used by non-privileged users.

## Install
```
pip3 install noapt --user
```

## Example
```
$ noapt                                                                                              
missing argument: programm name                                                                                                
$ noapt git                                                                                          
## searching package for: git                                                                                                  
## caching package: git                                                                                                        
<cut output>
Setting up git (1:2.15.1-1ubuntu2) ...                                                                                         
Processing triggers for libc-bin (2.27-0ubuntu2) ...                                                                           
--:                                                                                                                            
## executable: ~/bin/git                                                                                                       
## disk usage: 80M                                                                                                             
## to uninstall run: plash rm --eval-file ~/bin/git && rm ~/bin/git                                                                     
$ ~/bin/git --version                                                                            
git version 2.15.1                                                                                                             
```
## How does that work?
`noapt` itself is just ~50 lines intense but comparably robust shell scripting. The heavy lifting is done by [plash](https://github.com/ihucos/plash/), which is a container engine.

## Use cases
* Run non LTS packages in a LTS system
* Use Ubuntu packages in another distribution
* You don't have root access
* You don't like to use root access very often
* Install programs without cluttering your system
* Dont't bother about package names, caching meta data and other subtelities of your package manager: just type `noapt <program-name>`
* `noapt ag` is shorter than `sudo apt install silversearcher-ag`

## Updating installed packages
No really nice solution yet: delete all build cache with `plash purge` and it will be rebuiled on demand.

## The bad parts
* On my system 1.3 seconds startup time is just too much. That is absolutely optimizable, it comes mainly from slow python imports.
* I think fuse being slow is not too bad, the main work is expected to be done in /home, which is rbind mounted from container to host
* unionfs-fuse does not work perfectly with this setup: https://github.com/rpodgorny/unionfs-fuse/issues/78
* ~50 lines shell scripting
* It's not magic: the package runs in an isolated container where `/home` and `/tmp` is mounted to the host. It will not work with anything overly complicated.


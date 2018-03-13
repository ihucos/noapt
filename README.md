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
## to uninstall run: plash rm -I ~/bin/git && rm ~/bin/git                                                                     
$ ~/bin/git --version                                                                            
git version 2.15.1                                                                                                             
```
## How does that work?
`noapt` itself is just ~50 lines intense but comparably robust shell scripting. The heavy lifiting is done by [plash](https://github.com/ihucos/plash/), which is a container engine.

## Use cases
* Run non LTS packages in a LTS system
* Use Ubuntu packages in another distribution
* You don't have root access
* You don't like to use root access very often
* Install programs without cluttering your system
* Dont't bother about package names, just type `noapt $executablename`

## Updating
No really nice solution yet: delete all build cache with `plash purge` and it will be rebuiled on demand.

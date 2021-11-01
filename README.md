# A set of Ansilbe playbooks for deploynebt of a Kubernetes cluster node

The set is published as an example of tools that I applied during my self-learning.

`kube-playbook.yml` is a combined playbook to add a Kubernetes cluster node to an existing cluster.

## Git filters

There are two filters for `yml/yaml` files.

`.git/config`

```
[filter "nocommit_yaml"]
        clean = awk -f .nocommit.awk
        smudge = python .set_values.py --source_file noncommitted_values.yml
```
### Clean filter

`.noncommit.awk` drops values of keys between `#nocommit-begin` and `#nocommit-end` lines while commit.
For example, a file `group_vars/init.yml`:

```
#nocommit-begin
ansible_user: USERNAME
ansible_password: PASSWORD
ansible_become_pass: PASSWORD
#nocommit-end
```

The commited content of the file `group_vars/init.yml`:
```
#nocommit-begin
ansible_user: 
ansible_password: 
ansible_become_pass: 
#nocommit-end
```

### Smudge filter

`.set_values.py` substitutes values of keys between `#nocommit-begin` and `#nocommit-end` lines while checkout.

The values are at `--source_file noncommitted_values.yml`

For example, the pairs of the keys and the values at `noncommited_values.yml`:

```
ansible_user: USERNAME
ansible_password: PASSWORD
ansible_become_pass: PASSWORD
```

A file `group_vars/init.yml` inside a git repository:

```
#nocommit-begin
ansible_user:  
ansible_password:  
ansible_become_pass:  
#nocommit-end
```

The file `group_vars/init.yml` after checkout:
```
#nocommit-begin
ansible_user: USERNAME
ansible_password: PASSWORD
ansible_become_pass: PASSWORD
#nocommit-end
```

---
---
---
# GIT HOW TO
---
## Make Repo
---

1. Move to a the directory that you want to want to make a Repo
2. Run
 
Command
```bash
git init
```

---
## Update Remote Repo
---

1. Check status

Command
```bash
git status
```

[[Vaccine]]2. Stage files to be commited.

Command
```bash
get add .
```

3. Commit changes. 

Command
```bash
git commit -m "mm/dd/yyyy" 
```

4. Push updated Local Repo to Remote Repo

Command
```bash
git push origin master 
```

5. Add username and Key
	1.  Username is `w0lfister`
	2. Use access token found at **Settings** => **Developer Settings** => **Personal Access Token** => **Generate New Token** (Give your password) => **Fillup the form** => click **Generate token** => **Copy the generated Token**.
	3.  After using token store it to use later.

```bash
$ git config --global credential.helper cache
```
6. Remove creds
```bash
$ git config --global --unset credential.helper
$ git config --system --unset credential.helpe
```


---
## Clone Remote Repo
___
1. Get Repo with htts

```bash
git clone https://github.com/W0LFISTER/OSCP.git
```


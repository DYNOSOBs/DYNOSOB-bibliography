# Bibliography
A repository that contains a shared bibliography for the group.

## How to clone the repository

To clone the repository to your computer you need to open a terminal, navigate
to the location you want to the project, and run the following command:

```shell
git clone git@github.com:DYNOSOBs/DYNOSOB-bibliography.git
```

You can also download the project using the download button on the top right corner.

## How to add new entries

To add an entry to the `bibtex.bib` you need to create a new file for the
entry in the folder `assets`. The file can be of any format but preferably use
`txt`.

In the newly created file add your entry, and please use the key convention:

```shell
last_name_of_first_author:journal_abbreviation:year
```

journal abbreviations are in `journals.md`. Please edit these accordingly as
well.

An example of an entry:

```shell
@comment{A paper on the evolution of extortion}
@article{hilbe:PNAS:2013,
  title={Evolution of extortion in iterated prisoner’s dilemma games},
  author={Hilbe, Christian and Nowak, Martin A and Sigmund, Karl},
  journal={Proceedings of the National Academy of Sciences},
  volume={110},
  number={17},
  pages={6913--6918},
  year={2013},
  publisher={National Acad Sciences},
}
```

## How to add comments

**CURRENTLY COMMENTS ARE NOT BEING WRITTEN IN THE BIB FILE**

To add a comment to your entry use the format `@comment{<your text>}` and make
sure your comment is above the entry as shown in the example.


## Do not edit the `bibtex.bib`

To avoid conflict and other issues do not edit the file `bibtex.bib`. The file
is automatically generated each time someone adds a new entry in `assets`.

That does mean that you need to `pull` after each time you `push` to bring
down the updated `bibtex.bib`.


## How to update the repository using git

Before you start working make sure your copy is up to date. Command:

```shell
git pull origin master
```

Once you changed a file you need to prepare them for a commit using the command `add`:

```shell
git add `assets/hilde_2013.txt`
```

To commit:

```shell
git commit -m "Your message"
```

or just

```shell
git commit
```

which will open up an editor for you to write your commit.

Once everything is committed push your changes to `GitHub` using the command:

```shell
git push origin master
```

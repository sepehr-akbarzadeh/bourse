# Education

## Project Detail

You can find all technologies we used in our project into these files:
* Version: 0.0.0
* Back-End: Django2.4
* Language: Python3.7
* Front-End: ReactJs
* OS: Linux (Ubuntu18.04 dist.)
* Platforms: (Web, Android)
* Android: Native Java
* DevOps Pipline
  * Ansible
  * Docker 3.x
  * Git
  * Jenkins
  * Zabbix
  * OpenLdap

## Git commit Rules

A commit should be a wrapper for related changes. For example, fixing two different bugs should produce two separate commits. Small commits make it easier for other developers to understand the changes and roll them back if something went wrong. With tools like the staging area and the ability to stage only parts of a file, Git makes it easy to create very granular commits.

### Commit Often
Committing often keeps your commits small and, again, helps you commit only related changes. Moreover, it allows you to share your code more frequently with others. That way it‘s easier for everyone to integrate changes regularly and avoid having merge conflicts. Having large commits and sharing them infrequently, in contrast, makes it hard to solve conflicts.

### Don't Commit Half-Done Work

You should only commit code when a logical component is completed. Split a feature‘s implementation into logical chunks that can be completed quickly so that you can commit often. If you‘re tempted to commit just because you need a clean working copy (to check out a branch, pull in changes, etc.) consider using Git‘s «Stash» feature instead.

### Test Your Code Before You Commit

Resist the temptation to commit something that you «think» is completed. Test it thoroughly to make sure it really is completed and has no side effects (as far as one can tell). While committing half-baked things in your local repository only requires you to forgive yourself, having your code tested is even more important when it comes to pushing/sharing your code with others.

### Write Good Commit Messages

Begin your message with a short summary of your changes (up to 50 characters as a guideline). Separate it from the following body by including a blank line. The body of your message should provide detailed answers to the following questions: – What was the motivation for the change? – How does it differ from the previous implementation? Use the imperative, present tense («change», not «changed» or «changes») to be consistent with generated messages from commands like git merge. Having your files backed up on a remote server is a nice side effect of having a version control system. But you should not use your VCS like it was a backup system. When doing version control, you should pay attention to committing semantically (see «related changes») - you shouldn‘t just cram in files.

### Use Branches

Branching is one of Git‘s most powerful features - and this is not by accident: quick and easy branching was a central requirement from day one. Branches are the perfect tool to help you avoid mixing up different lines of development. You should use branches extensively in your development workflows: for new features, bug fixes, ideas...

### Agree on A Workflow

Git lets you pick from a lot of different workflows: long-running branches, topic branches, merge or rebase, git-flow... Which one you choose depends on a couple of factors: your project, your overall development and deployment workflows and (maybe most importantly) on your and your teammates‘ personal preferences. However you choose to work, just make sure to agree on a common workflow that everyone follows.

The following document is based on experience doing code development, bug troubleshooting and code review across a number of projects using GIT, including libvirt, QEMU and OpenStack Nova. Examination of other open source projects such as the Kernel, CoreUtils, GNULIB and more suggested they all follow a fairly common practice. It is motivated by a desire to improve the quality of the Nova GIT history. Quality is a hard term to define in computing; one man's "Thing of Beauty" is another man's "Evil Hack". We can, however, come up with some general guidelines for what to do, or conversely what not to do, when publishing GIT commits for merge with a project, in this case, OpenStack.

#### This topic can be split into two areas of concern

* The structured set/split of the code changes
* The information provided in the commit message

### Formatting Rules
* Capitalized, short (50 chars or less) summary

* More detailed explanatory text, if necessary. Wrap it to about 72 characters. In some contexts, the first line is treated as the subject of an email and the rest of the text as the body. The blank line separating the summary from the body is critical (unless you omit the body entirely); tools like rebase can get confused if you run the two together.

* **Always leave the second line blank.**

* Write your commit message in the imperative: "Fix bug" and not "Fixed bug" or "Fixes bug." This convention matches up with commit messages generated by commands like git merge and git revert.

* Further paragraphs come after blank lines.

    * Bullet points are okay, too
    * Typically a hyphen or asterisk is used for the bullet, preceded by a single space, with blank lines in between, but conventions vary here
    * Use a hanging indent

### Examples of good practice


**Example 1** (no description, only summary)
`
  commit 3114a97ba188895daff4a3d337b2c73855d4632d
  Author: [removed]
  Date:   Mon Jun 11 17:16:10 2012 +0100

    Update default policies for KVM guest PIT & RTC timers
`

**Example 2** (description as bullet points)
`
  commit ae878fc8b9761d099a4145617e4a48cbeb390623
  Author: [removed]
  Date:   Fri Jun 1 01:44:02 2012 +0000

    Refactor libvirt create calls

     - Minimize duplicated code for create

     - Make wait_for_destroy happen on shutdown instead of undefine

     - Allow for destruction of an instance while leaving the domain
`

**Example 3** (description as plain text)
`
  commit 31336b35b4604f70150d0073d77dbf63b9bf7598
  Author: [removed]
  Date:   Wed Jun 6 22:45:25 2012 -0400

    Add CPU arch filter scheduler support

    In a mixed environment of running different CPU architectures,
    one would not want to run an ARM instance on a X86_64 host and
    vice versa.

    This scheduler filter option will prevent instances running
    on a host that it is not intended for.

    The libvirt driver queries the guest capabilities of the
    host and stores the guest arches in the permitted_instances_types
    list in the cpu_info dict of the host.

    The Xen equivalent will be done later in another commit.

    The arch filter will compare the instance arch against
    the permitted_instances_types of a host
    and filter out invalid hosts.

    Also adds ARM as a valid arch to the filter.

    The ArchFilter is not turned on by default.
`

[Git CheatSheet](https://github.com/trein/dev-best-practices/wiki/Git-Tips)
[Main Reference](https://git-scm.com/docs)


## Documentation Rules

Like every open-source project, we are always looking for volunteers to help us with programming. Writing documentation knowledge is required. Treating documentation as code is becoming a major theme in the software industry. This is coming from both sides, with developers starting to treat documentation as a priority alongside tests and code, and writers seeing a lot of value in integrating more into the development process. This marrying of cultures isn’t simple, but having the proper tools for the job makes both sides happy with the process and the results that get produced.

A lot of developer tools don’t work well for writers. Sphinx and Read the Docs are unique in this ecosystem, in that they have powerful features that both writers and developers want, in one convenient package.

### Doc Pages

It is a developer focused platform, but it has most of the features that technical writers have come to expect in a tool as well. This blending of worlds makes it the best suited platform for teams that want both writers and developers contributing to product and API documentation

#### We need:

* Each Django application must have a seperated section.
  * each application needs a brief story about what is it and how team can work with.
  * each application needs a test documentation.
  * needs a devops helper to tell devops engineer how he can run the project.
  * if there is a config file it must explain to devops engineer.

* DevOps must have a seperated section.
  * A tutorial section for each new volunteer come into our team.
  * A seperate section for each subject on DevOps.
  * A seperate section to describe whole devops pipline.

* Database permissions:
 * CREATE DATABASE <db_name>;
 * CREATE USER <user_name> WITH PASSWORD '1234';
 * ALTER ROLE <user_name> SET client_encoding TO 'utf8';
 * ALTER ROLE <user_name> SET default_transaction_isolation TO 'read committed';
 * ALTER ROLE <user_name> SET timezone TO 'UTC';
 * GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <user_name>;
 * ALTER USER <user_name> CREATEDB;
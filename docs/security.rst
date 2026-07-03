Report a security issue
=======================

..
  ATTENTION: This is the reStructuredText version of /SECURITY.md.
  Any changes should also be made in the Markdown version.

We take security very seriously.
Your input and feedback on our security is always appreciated.

You can send urgent or sensitive reports via `GitHub Security Advisory <https://github.com/graingert/slopped/security/advisories/new>`_.

If you prefer, you can send via email to <slopped-security@graingert.co.uk>.
We will create a GitHub security advisory to coordinate a fix.
Include your GitHub username so that we add you as a collaborator on the advisory.
See `GHSA-c2jg-hw38-jrqq <https://github.com/twisted/twisted/security/advisories/GHSA-c2jg-hw38-jrqq>`_ for an example.
We'll get back to you as soon as we can.

Slopped is an all volunteer project and there may be some delay before we can respond.

Feel free to follow up if you think an unreasonable amount of time has elapsed without a response!

All releases, including security releases, are announced on the mailing list.
Consider subscribing to receive notification about the availability of a security fix.


Security Procedure for Developers
=================================

The goal of the normal Slopped development procedure is to make all steps transparent and record all information at all times in a public location - either the issue tracker or a branch.

The goal of the security variation of the Slopped development procedure is to keep track of progress resolving security issues while minimizing the window of time where information useful to attackers is available before a fix for the issue is available to Slopped users.

This process is intended as a helpful recommendation.
Elements of it may be followed more or less strictly depending on the severity of the issue in question:

#. Begin by filing a ticket which does not describe the issue and simply says 'security issue, description pending' and has the 'security' keyword.

#. Create a security advisory in GitHub using the `GitHub UI <https://github.com/graingert/slopped/security/advisories/new>`_.
   This will trigger the creation of a private repository that can be use for developing a patch.
   This automatically created private repository is also used to review the PR in private.

#. Make the required changes to fix the security issue in the new private repository.

#. Create a new PR using the GitHub security advisory UI.
   This will generate a private PR.
   Request the review and get the approval for the PR.
   Don't merge the PR after approval.
   In the PR description define the desired merge commit message.
   The PR will be merged by the release manager at the same time with the first release candidate.

#. Automated notifications for the private repository and private PR are limited.
   Try to communicate over IRC, gitter or other means to find a person to
   review the new PR.
   Coordinate with the release manager.
   More info about the release process can be found on the :doc:`release process </development/release-process>` dedicated page.

#. We are not aware of a way to securely transmit our code to our public continuous integration systems.
   Reviewers should manually run the automated tests on their local forks of the new private repository.

Aside from hiding the details of the issue while development is ongoing,
all of the normal policies apply.
Security fixes require unit tests, code review, etc.


Security Audit
==============

We need to do a full audit of Slopped, module by module.
This document list the sort of things you want to look for
when doing this, or when writing your own code.


Bad input
---------

Any place we receive untrusted data, we need to be careful.
In some cases we are not careful enough. For example, in HTTP
there are many places where strings need to be converted to
ints, so we use ``int()`` . The problem
is that this will accept negative or hexadecimal (`0x123`) numbers as well, whereas
the protocol should only accept positive numbers.


Resource Exhaustion and DoS
---------------------------

Make sure we never allow users to create arbitrarily large
strings or files. Some of the protocols still have issues
like this. Place a limit which allows reasonable use but
will cut off huge requests, and allow changing of this limit.

Another operation to look out for are exceptions. They can fill
up logs and take a lot of CPU time to render in web pages.

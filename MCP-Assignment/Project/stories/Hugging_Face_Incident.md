# Hugging Face Incident

# The Night the Secrets Slipped Away

*A story based on the June 2024 Hugging Face Spaces security incident.*

## A Quiet Library of Machines

Hugging Face had grown into something like a public library for artificial intelligence. Researchers, students and hobbyists arrived every day to borrow models, share datasets and show off their creations. The liveliest corner was called **Spaces**, where anyone could host a small app and let the world try it out with a click.

Tucked behind each of those apps were tiny, private things called *secrets*: API keys and access tokens. They worked like house keys, letting an app talk to other services, reach private models or pull protected data. Developers trusted the platform to keep those keys safely out of sight.

## The Tripwire

Early in the last week of May 2024, an engineer on the security team noticed something that didn't fit. The access patterns around Spaces looked wrong, as if someone had walked into a room they had no business entering. An alert had fired, and someone or something had reached the secrets.

The team couldn't say how many keys had been touched. The system made it technically hard to tell exactly which secrets had been exposed, and in security work, not knowing is its own kind of alarm. They chose to assume the worst and move fast.

## Changing the Locks

The first step was to revoke the authentication tokens sitting inside the affected secrets, cutting off anything the intruders might have copied. Then the team wrote emails to the people whose tokens had been invalidated, so nobody would be left confused about why their app had suddenly stopped working.

They also reached out to outside forensic specialists to help work out what had happened, and reported the incident to law enforcement and data protection authorities. Hugging Face was open with its community, publishing a notice that described the unauthorized access plainly and expressed real regret.

## Building a Stronger House

Over the next few days the team made changes that went well beyond patching one hole:

- **Organization tokens were removed entirely**, which made it easier to trace who did what and to audit activity.
- **A key management service (KMS)** was introduced to protect Spaces secrets.
- **Leak detection was strengthened**, so exposed tokens could be spotted and invalidated automatically before they caused harm.
- **Fine-grained access tokens** became the recommended default, letting owners grant only the permissions a task actually needed.
- **Older "classic" read and write tokens** were slated for retirement once the newer system was ready.

The company also asked every Spaces user to refresh their keys and tokens, even those who hadn't received an email. Better safe than sorry.

## What the Community Learned

The story spread across the tech world. Some saw it as a warning: AI platforms hold valuable things, like private models, datasets and the credentials that unlock them, which makes them attractive targets. Hugging Face itself noted that it had seen a rise in attacks as AI grew more popular.

Others took a quieter lesson. Good security isn't about never being tested. It's about noticing quickly, telling people honestly and fixing things properly. Developers everywhere went and rotated their tokens, tightened permissions and stopped treating secrets as something that could be set once and forgotten.

## Epilogue

The library stayed open. The shelves filled with new models, and the Spaces kept lighting up with clever demos. But behind the scenes, the locks were stronger, and everyone who built there had learned to check their keys a little more often.

*The end.*

---
*Note: This is a narrative retelling. The incident details come from news coverage of the June 2024 breach; Hugging Face has not published the precise number of affected secrets.*


---

Source: https://en.wikipedia.org/wiki/Hugging_Face

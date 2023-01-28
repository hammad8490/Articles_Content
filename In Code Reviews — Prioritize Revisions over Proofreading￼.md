Title: In Code Reviews — Prioritize Revisions over Proofreading 
Slug: in-code-reviews-prioritize-revisions-over-proofreading
Tags: General Info
Image: in-code-reviews-prioritize-revisions-over-proofreading.jpeg
Summary: There are two distinct forms of feedback in code reviews: revising and proofreading.
Date: 2022-01-1 10:00


There are two distinct forms of feedback in code reviews: revising and proofreading.

I've seen over-emphasis on proofreading when I was at Google, on every team I contributed to. It is also clear in many other engineering cultures.

I've found the most descriptive names of these two concepts comes from journalism: revising and proofreading. There aren't really good terms in software engineering culture. Structure vs style might be one way, but I don't think it quite captures the important pieces. I contend that revising is much more important, and that many engineering cultures place too much value on proofreading.

Revising feedback comes in aggregate and does not refer to a single line, and usually not even a method. Asking for revision is a call to change approach and overall structure. It could include "abstract this tuple to its own class", "simplify this api to fewer methods", or "take out this indirection, no need for an extra layer of abstraction here". Revising will usually require the author to think about the problem while not typing at a keyboard.

Proofreading feedback on the other hand, usually refers to a single line or a few lines. It includes making variable names more descriptive, breaking out helper functions, or changing from do-while to for. Fixing these changes gets tedious, and is very localized. Following style guides is a large source of proofreading feedback, as style guides are often strict about line length and the case style of variables and methods.

Take for example, this commit:

https://github.com/mvpengineer/dataproblems/commit/4b844a45ecf2f55cd2d41ae00c8c41c5471b637c

Revising feedback could include:
	Pull past_users out to a persistent storage, like cloud SQL.
	Add failure pathway for api calls.
Proofreading feedback might be:
	Remove past_users from users before iterating in line 44.
	Use proper spaces between comma separated variables in line 24.
	tokens, atoken, and atokens (line 24) can be confusing. Pick more descriptive names.

This example is small, so it's tough to show meaningful revising feedback.

Revising your code is important for many reasons. The type of mistakes that happen at a high level are more permanent and costly than those localized to a singular method. If your database schema misses the mark, or the API is sloppy, the work to fix it is huge. It might only be addressed weeks or months after the offending code goes in. By that point, many more modules have been built on top of the incorrect abstractions. Major refactoring is necessary to re-do the original code. Many times, the mistakes are lived with, and the user gets a sub-optimal experience. The work to fix every layer of the stack becomes too costly.

Mistakes in variable naming or other proofreading issues are generally localized to a single file. This means they are easily fixed later, but more importantly, they don't affect the system as a whole. If the mistake matters, it is easily fixed. If it doesn't matter, it stays forever, and no one cares. Junior engineers can think through a method that has single letter variables. They can reason about two for loops that could have been integrated into one. These problems are within so few lines of code, it takes a few seconds to determine what's happening.

Conversely, proofread code in the wrong abstraction gets thrown out upon refactoring. The proofreading effort is lost, because the code is now deleted. Had it been revised instead, it would only been written once, and sloppiness that needs fixing can be fixed on leisure time. Since engineers almost always prefer writing new code over editing old (even in a culture of such proofreading), it's important we stand on a firm foundation of well thought out abstractions.

At Google, I observed the most senior engineers, and their thinking was focused on understanding the 
large overly complex systems — finding ways to abstract them more correctly for cleaner thinking for the junior engineers. Simplifications of large abstractions were fodder for promotions. This underscores the relative company priority. However, the need for these large refactors could have been short circuited by good revision of code in the first place.

You can see the effects of the feedback on the maintainability of the code in our example. If we only fixed the revisions, we'd have a more functional and robust codebase. Fixing the proofreading changes, though, we would have slightly more readable code, saving us 10 seconds when reviewing the code in the future.

Subtle mistakes can crop up from sloppy naming and bad code hygiene, so proofing is not without merit. The two are also not mutually exclusive. But I think revising is more important to focus on.

My argument here is similar to advocating "do the right thing" over "do the thing right". It seems to me engineers over prioritize the details by orders of magnitude while missing the mark on creating something useful.

Do the right thing when reviewing code. Leave revision feedback and ignore the nitpicks. We'll all have more useful products as a result. And if you didn't see that "essential" is misspelled in my header image, I've proved my point.

<br><br>
Do the right thing when reviewing code. Leave revision feedback and ignore the nitpicks. We'll all have more useful products as a result. And if you didn't see that "essential" is misspelled in my header image, I've proved my point.
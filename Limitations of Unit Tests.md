Title: Limitations of Unit Tests
Slug: limitations-of-unit-tests
Tags: General Info, MVP Practices
Image: limitations-of-unit-tests.png
Summary: Some developers are dogmatic using test driven development (TDD) philosophy. For MVPs, I think this is the wrong approach. Here I lay out some considerations for a solid development culture while you build your business. I will specifically focus on unit tests, tests that validate atomic components of an app.
Date: 2022-12-19 10:00

Some developers are dogmatic using test driven development (TDD) philosophy. For MVPs, I think this is the wrong approach. Here I lay out some considerations for a solid development culture while you build your business. I will specifically focus on unit tests, tests that validate atomic components of an app.

## Benefits
Test coverage generally reduces bugs. Code is more predictable and less mysterious. Largely, you won't look back at the code and say "I have no idea why this works", which is surprisingly common. It can improve code structure, by forcing yourself to create atomic methods that are easy to pass around interface arguments, the application code is better organized for understanding. This makes it more robust and readable by incoming engineers. Writing in strict TDD may clarify requirements earlier in the process, because TDD states that tests are written before application code, and therefore functionality is made clear before spending time writing. Test coverage can be a meaningful metric, but potentially a vanity metric for third parties to gain buy in with "95% test coverage".

## Drawbacks
Time and energy. Unit tests are an investment. They often take 3-5 lines of code per line of test coverage. This means your functional app may take 2-6 times longer to build, with marginal improvements to robustness. The key tradeoff to make here is looking at how fast the application code is shifting. For requirements that are clear and unaltering, unit tests are a good investment. Some businesses can plan for code that will remain largely unchanged for multiple years. I saw this at Google, and it is a good strategy for them. For MVPs, on the other hand, unit tests can be a liability. Full pages of functionality get thrown out or back to the drawing board. Libraries change, apis and interfaces shift, each requires a major refactor in the test code. More time spent, and more opportunity for a competitor to move faster than you. Secondly, it is often difficult to set up unit tests that provide meaningful insight into the functionality of the code. Without knowing what you don't know, you might just be confirming it works as you expect it to work. This does nothing to catch the edge cases or logic errors that will show up at an unexpected time. There are other forms of testing that will get you many of the benefits of a robust system, especially before launching to real users. Acceptance testing is a main one.

<br><br>
All in all, for MVPs, unit tests seem more like a liability than an asset. I recommend heavy acceptance testing for user facing features, and no unit testing until a beta version where there is value in stability. Reach out if you have questions on how to maintain a healthy development culture during your MVP build.
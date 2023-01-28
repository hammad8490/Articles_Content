Title: Testing Your MVP
Slug: testing-your-mvp
Tags: MVP Development, MVP Practices
Image: testing-your-mvp.png
Summary: MVPs are constantly changing to adapt to the market and needs of users. You have to be very judicious in your testing, so that you don't waste valuable cycles on things that will be thrown out soon after writing, or something that just lengthens development time beyond what the market can bear. You don't want to be crushed by a competitor because you were writing duplicate unit tests for your backend that will be rewritten in a month. That said, I'm going to go through the major types of testing, and when they'll be useful in your product lifecycle.
Date: 2022-01-16 10:00

MVPs are constantly changing to adapt to the market and needs of users. You have to be very judicious in your testing, so that you don't waste valuable cycles on things that will be thrown out soon after writing, or something that just lengthens development time beyond what the market can bear. You don't want to be crushed by a competitor because you were writing duplicate unit tests for your backend that will be rewritten in a month. That said, I'm going to go through the major types of testing, and when they'll be useful in your product lifecycle.

## Unit Tests
These are the most basic tests for individual code functions and simple logic errors. They are usually what are written first in test driven development. In my experience even up to the most senior of engineers, these tests can be helpful, but are often a duplication of effort. Doubling and tripling the number of lines of code to ensure the edge cases of systems are working. Making sure your site doesn't fail on strange inputs matters, but at what cost? When building an MVP, I generally advise against investing resources into unit tests beyond the most mathematically heavy and precise functions. Leaving out unit tests lets you move faster and adapt to the changing needs of the market.

## Integration Tests
These tests cover the interface and main component interactions. How is the database interacting with the app interacting with the data stream or third party APIs. Coverage here can be helpful, because when one of these interfaces goes down, much of the app is out of commission. But don't do too much — focus on the main touch points, not new features. These tests can be especially helpful if the external API or third party library you're depending on changes beneath you. You may mock out your app interactions to press against the external libraries to see if they change or break.

## User Acceptance Testing
This is the most important form of testing in my opinion. It covers both whether you're actually solving a problem — getting users to use the product and rate its efficacy in solving a problem of theirs. As well as QA testing, which is whether the app is behaving as desired. You want to create user journeys, or paths that are core to the user experience to walk through on each release. Did a change to the "follow" button somehow break the sign up flow of your social network? Not that strange, but you won't know unless you consistently test the "sign up" user journey on each release. You might be satisfied with degrading gracefully, less than optimal performance or experience, as long as key operations can be completed on the site.

## Load Testing
This testing makes sure you can handle the amount of users you anticipate, or possibly attacks on the site designed to mimic large user volume. You can do this by creating a large number of mock users and create automated flows to hit the important endpoints of the system. See how it reacts. Does your database fall over, or are requests throttled and handled when resources become available? Have you created an adaptable backend that spins up more resources when the load balancer becomes overwhelmed? What behavior do you want, and what's required by the marketing team for launch day?

<br><br>
All in all, there's lots to consider in testing your MVP, usually, I recommend focusing on UAT, and load testing for launches. But integration tests and unit tests have their place as the app becomes more mature. If you need help creating your testing strategy and determining how to allocate your resources to stability, reach out.